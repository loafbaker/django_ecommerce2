from rest_framework import serializers

from carts.mixins import TokenMixin
from .models import UserAddress, Order


class OrderSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = [
            'id',
            'user_checkout',
            'shipping_address',
            'billing_address',
            'subtotal',
            'shipping_total_price',
            'order_price',
        ]

    def get_subtotal(self, obj):
        return obj.cart.subtotal

class FinalizeOrderSerializer(serializers.Serializer):
    order_token = serializers.CharField()
    order_id = serializers.IntegerField(required=False)
    user_checkout_id = serializers.IntegerField(required=False)
    payment_method_nonce = serializers.CharField()

    def validate(self, data):
        order_token = data.get('order_token')

        # 1. Validate order token and order id
        try:
            order_data = TokenMixin().parse_token(order_token)
            order_id = order_data.get('order_id')
            order = Order.objects.get(id=order_id)
        except:
            raise serializers.ValidationError('This is not a valid order.')

        data['order_id'] = order_id  # Omit the original order_id key

        # 2. Validate user checkout id
        try:
            user_checkout_id = order_data.get('user_checkout_id')
        except:
            user_checkout_id = data.get('user_checkout_id')

        if order.user_checkout.id != user_checkout_id:
            raise serializers.ValidationError('The order is not owned by this user or the order token is expired.')
        else:
            data['user_checkout_id'] = user_checkout_id

        # 3. Handle the nonce
        payment_method_nonce = data.get('payment_method_nonce')
        if payment_method_nonce is None:
            raise serializers.ValidationError('This is not a valid nonce.')

        return data


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = [
            'id',
            'user_checkout',
            'type',
            'street',
            'city',
            'state',
            'zipcode',
        ]