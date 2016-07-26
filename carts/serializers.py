from rest_framework import serializers

from products.models import Variation
from orders.models import UserAddress, UserCheckout
from .mixins import TokenMixin
from .models import CartItem, Cart


class CartVariationSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = Variation
        fields = [
            'id',
            'title',
            'price',
            'product',
        ]

    def get_product(self, obj):
        return obj.product.title


class CartItemSerializer(serializers.ModelSerializer):
    # item = CartVariationSerializer(read_only=True)
    item_id = serializers.SerializerMethodField()
    item_title = serializers.SerializerMethodField()
    product_id = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = [
            'item_id',
            'item_title',
            'product_id',
            'price',
            'quantity',
            'line_item_total',
        ]

    def get_item_id(self, obj):
        return obj.item.id

    def get_item_title(self, obj):
        return '%s - %s' % (obj.item.product.title, obj.item.title)

    def get_product_id(self, obj):
        return obj.item.product.id

    def get_price(self, obj):
        return obj.item.price

class CheckoutSerializer(serializers.Serializer):
    user_checkout_token = serializers.CharField()
    user_checkout_id = serializers.IntegerField(required=False)
    cart_token = serializers.CharField()
    cart_id = serializers.IntegerField(required=False)
    billing_address_id = serializers.IntegerField()
    shipping_address_id = serializers.IntegerField()

    # For custom field validation, user validate_<fieldname>(self, value) function,
    # and return the valid object for the field or raise an error.
    def validate(self, data):
        user_checkout_token = data.get('user_checkout_token')
        cart_token = data.get('cart_token')
        billing_address_id = data.get('billing_address_id')
        shipping_address_id = data.get('shipping_address_id')

        # 1. User checkout validation
        try:
            user_checkout_data = TokenMixin().parse_token(user_checkout_token)
            user_checkout_id = user_checkout_data.get('user_checkout_id')
        except:
            user_checkout_id = data.get('user_checkout_id')

        try:
            user_checkout = UserCheckout.objects.get(id=user_checkout_id)
            data['user_checkout_id'] = user_checkout_id
        except:
            raise serializers.ValidationError('This is not a valid user')

        # 2. Cart validation
        try:
            cart_data = TokenMixin().parse_token(cart_token)
            cart_id = cart_data.get('cart_id')
        except:
            cart_id = data.get('cart_id')

        try:
            cart = Cart.objects.get(id=cart_id)
            data['cart_id'] = cart_id
        except:
            raise serializers.ValidationError('This is not a valid cart.')

        if cart.cartitem_set.count() == 0:
            raise serializers.ValidationError('The cart is empty. Please add some items first.')

        # 3. Billing address validation

        try:
            billing_address = UserAddress.objects.get(user_checkout=user_checkout, type='billing', id=billing_address_id)
        except:
            raise serializers.ValidationError('This billing address is not valid for the user.')

        # 4. Shipping address validation
        try:
            shipping_address = UserAddress.objects.get(user_checkout=user_checkout, type='shipping', id=shipping_address_id)
        except:
            raise serializers.ValidationError('This shipping address is not valid for the user.')

        return data
