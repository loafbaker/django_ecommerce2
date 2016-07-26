import requests
import json

base_url = 'http://127.0.0.1:8000/api/'

login_url = base_url + 'auth/token/'

products_url = base_url + 'products/'

refresh_url = login_url + 'refresh/'

cart_url = base_url + 'cart/'

user_checkout_url = base_url + 'user/checkout/'

user_address_url = base_url + 'user/address/'

user_address_create_url = user_address_url + 'create/'

checkout_url = base_url + 'checkout/'

# requests.post(login_url, data=None, headers=None, params=None)

def user_product_api_test():
    """
    Run login, product, refresh, cart api test
    :return: (No return)
    """
    # Auth test
    data = {
        'username': 'testuser',
        'password': 'test1234',
    }
    login_r = requests.post(login_url, data=data)

    json_data = login_r.json() #login_r.text

    print(json.dumps(json_data, indent=2))

    token = json_data['token']

    # Retrive products test

    headers = {
        'Authorization': 'JWT %s' % (token)
    }
    p_r = requests.get(products_url, headers=headers)

    prod_json_data = p_r.json()
    print (json.dumps(prod_json_data, indent=2))

    # Refresh URL token

    data = {
        'token': token
    }
    refresh_r = requests.post(refresh_url, data=data)

    print(refresh_r.json())

    token = refresh_r.json()['token']

    # Cart URL test
    cart_r = requests.get(cart_url)

    print(cart_r.json())

def create_cart():
    """
    Create a new cart with API
    :return: Cart token
    """
    # Create cart
    cart_r = requests.get(cart_url)
    # Get cart token
    cart_token = cart_r.json()['token']
    return cart_token

def get_user_checkout_token(email):
    """
    Retrive or create a user checkout token with API
    :return: User checkout token
    N.B. Currently can only handle non-registered user email
    """
    data = {
        'email': email,
    }
    user_checkout_r = requests.post(user_checkout_url, data=data)
    user_checkout_token = user_checkout_r.json()['user_checkout_token']
    return user_checkout_token

def get_user_checkout_id(email):
    """
    Retrive or create a user checkout id with API
    :return: User checkout id
    N.B. Currently can only handle non-registered user email
    """
    data = {
        'email': email,
    }
    user_checkout_r = requests.post(user_checkout_url, data=data)
    user_checkout_id = user_checkout_r.json()['user_checkout_id']
    return user_checkout_id

def checkout_api_test(email=None, user_auth=None):
    """
    :param email: User checkout email (must be a non-registered user)
    :param user_auth: (Currently not used)
    :return: (No return)
    N.B. Currently can only handle non-registered user email
    """
    # Create a new cart and get its token
    cart_token = create_cart()
    # Add items to cart
    new_cart_url = cart_url + '?token=' + cart_token + '&item_id=2&qty=5'
    new_cart_r = requests.get(new_cart_url)
    # Get user checkout token
    if email:
        user_checkout_token = get_user_checkout_token(email)
        new_user_address_url = user_address_url + '?user_checkout_token=' + user_checkout_token + '&limit=5'
        new_user_address_r = requests.get(new_user_address_url)
        new_user_address_data = new_user_address_r.json()
        if new_user_address_data['count'] >= 2:
            # Assume if the user has more than two addresses, then at least one address
            # for billing and at least one for shipping
            billing_addresses = [addr for addr in new_user_address_data['results'] if addr['type'] == 'billing']
            billing_address_id = billing_addresses[0]['id']
            shipping_addresses = [addr for addr in new_user_address_data['results'] if addr['type'] == 'shipping']
            shipping_address_id = shipping_addresses[0]['id']
        else:
            user_checkout_id = get_user_checkout_id(email)
            data = {
                'user_checkout': user_checkout_id,
                'type': 'billing',
                'street': '2016 Donald Ave.',
                'city': 'Newport Beach',
                'state': 'CA',
                'zipcode': 92304,
            }
            billing_address_create_r = requests.post(user_address_create_url, data=data)
            billing_address_id = billing_address_create_r.json()['id']
            data = {
                'user_checkout': user_checkout_id,
                'type': 'shipping',
                'street': '2016 Donald Ave.',
                'city': 'Newport Beach',
                'state': 'CA',
                'zipcode': 92304,
            }
            shipping_address_create_r = requests.post(user_address_create_url, data=data)
            shipping_address_id = shipping_address_create_r.json()['id']
        # Run checkout
        data = {
            'user_checkout_token': user_checkout_token,
            'cart_token': cart_token,
            'billing_address_id': billing_address_id,
            'shipping_address_id': shipping_address_id,
        }
        print(data)
        order_r = requests.post(checkout_url, data=data)
        print(order_r.text)


if __name__ == '__main__':
    # user_product_api_test()
    checkout_api_test(email='dirac@gmail.com')