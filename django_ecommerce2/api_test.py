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

checkout_finalize_url = checkout_url + 'finalize/'

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
        order_token = order_r.json()['order_token']
        return order_token
    else:
        return None

def checkout_finalize_api_test(order_token):
    new_checkout_finalize_url = checkout_finalize_url + '?order_token=' + order_token
    new_checkout_finalize_r = requests.get(new_checkout_finalize_url)
    print(new_checkout_finalize_r.text)
    braintree_client_token = new_checkout_finalize_r.json()['braintree_client_token']
    return braintree_client_token


def write_payment_test_page(braintree_client_token, filename='api_test_payment.html'):
    base_file_content = \
"""
<!DOCTYPE html>
<!-- Run python local server with 'python -m SimpleHTTPServer 8080' -->
<!-- Then run open this payment test page in a modern browser -->
<!-- http://localhost:8080/api_test_payment.html -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
    <title>API Test Payment</title>
</head>
<body>
  <div class="container">
    <h1>Payment test</h1>
    <form id="checkout"  method="POST" action=".">
      <div id="payment-form"></div>
      <input type="submit" value="Pay test" class="btn btn-default">
    </form>
  </div> <!-- /container -->

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
  <script src="https://js.braintreegateway.com/v2/braintree.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  <script>
  var clientToken = "%s";
  braintree.setup(clientToken, "dropin", {
    container: "payment-form",
    onPaymentMethodReceived: function (obj) {
      console.log(obj.nonce)
    }
  });
  </script>
</body>
</html>
"""
    f = open(filename, 'w')
    f.write(base_file_content % braintree_client_token)
    f.close()
    print('File %s is written. Finish online payment through a browser' % filename)


if __name__ == '__main__':
    # 0. Utilities test
    # user_product_api_test()
    # 1. Get the order_token & braintree client token
    order_token = checkout_api_test(email='dirac@gmail.com')
    braintree_client_token = checkout_finalize_api_test(order_token)
    # 2. Write a HTML file and finish the payment through browser
    write_payment_test_page(braintree_client_token)
    # 3. Follow the instructions and finish the test
    print('First, run python HTTP server')
    print('\tpython -m SimpleHTTPServer 8080')
    print('Second, open the local modern browser (firefox, chrome) and open the url')
    print('\thttp://localhost:8080/api_test_payment.html')
    print('Third, open the development console in the browser (Press \'F12\' and choose the \'Console\' tab')
    print('Fourth, finish credit card payment online with test card information')
    print('\tCard number: 4111 1111 1111 1111')
    print('\tExpired: (Arbitrary)')
    print('Fifth, copy the payment method nonce in the console and replace the both json keys below:')
    print('{')
    print('    "order_token": "%s",' % order_token)
    print('    "payment_method_nonce": "<your-own-payment-method-nonce>"')
    print('}')
    print('Sixth, post the json data to checkout finalize url (/api/checkout/finalize/).')
    print('\tIf return data has a \'success\' key of True and a 8-char-long valid \'transaction_id\',')
    print('\tthen the checkout finalize API test is succeed!')