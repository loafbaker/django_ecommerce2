django_ecommerce2
=================

An improved e-commerce app built within django framework

Run in django 1.9.4 and python 2.7.6

# Setup

Install all the required libraries

    pip install -r requirements.txt

Rebuild database

    rm db.sqlite3
    python manage.py migrate
    python manage.py createsuperuser

Collect static files

    python manage.py collectstatic

Run web server

    python manage.py runserver

Finally, you can view the web app with your local browser by accessing http://localhost:8000/

# Private Settings

Before you enable all the functions in django_ecommerce2, you have to reset a few parameters in the setting file `django_ecommerce2/settings.py`.

1. If you want to activate the email function for your server, you need to refill your own parameters for the following line codes.

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yourgmail@gmail.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

2. if you want to run on Braintree application, you have to replace the following definitions with your own Braintree API keys.

```python
BRAINTREE_PUBLIC = 'your-braintree-public-key'
BRAINTREE_PRIVATE = 'your-braintree-private-key'
BRAINTREE_MERCHANT_ID = 'your-braintree-merchant-id'
BRAINTREE_ENVIRONMENT = 'Sandbox-or-Production'
```

# Version Control

Ver.1   [Basic Template](../../tree/086876c197cec682ba202168e2260eda4a942be9)

Ver.2   [Products App](../../tree/4f3251004f29b20addc412802afc5ccb3dd2e258)

Ver.3   [Product Detail View](../../tree/9d01d36277152bbfb7ec3d8b9e79af0694c83b0d)

Ver.4   [List View](../../tree/b94c4a912b42054ad3e6c9a08b476f6f001360de)

Ver.5   [Using Links for Model Instances](../../tree/40edd2c1b1ee6740c249f5e234f973586cb6b7dd)

Ver.6   [Model Managers](../../tree/6ec459823379f71cb35028449877ad8de58d0b11)

Ver.7   [Product Variations](../../tree/0a03b123da89698cb7ffb2b100745d2548bcc2a0)

Ver.8   [Post Save Signal for Variations](../../tree/9f8af3071f77638b66b7881012970d464ebe9491)

Ver.9   [Product Detail Layout](../../tree/e9f7a5ec5776e4505c1aee1d4449f7fbacf7af35)

Ver.10   [Image Uploads](../../tree/62a29cccf24ec1fd07d95e3a6469d70e0d92dd4c)

Ver.11   [Search Query](../../tree/bf2a75c092220c50a523520ba2b89ba7607b3958)

Ver.12   [Formset for Inventory](../../tree/d69646c743571a61a8e4efcbb22802f34c4a63be)

Ver.13   [Login Required Mixins](../../tree/a5ba2382638b286049ea0eb4f4b5e93f10e22cf3)

Ver.14   [Django Messages](../../tree/c89ffeebd6158b32b31e003ea5440eca46ca7b78)

Ver.15   [Social Share](../../tree/385de2f6c8ce35bda14bd850c0a5e07d6b613381)

Ver.16   [Dynamic Update Price with jQuery](../../tree/2407f99ed7c7532f393e5b25a2f60fb640b4bcc8)

Ver.17   [Single Variation Price](../../tree/62b82551f387ec9aabf6c51fe7abd2b5a5442bad)

Ver.18   [Product Categories](../../tree/fc9983963a8bdfd4fffd90d222203acf257a7335)

Ver.19   [Category Detial View](../../tree/7326fc7a50e77d4b9b01a7b2c22b92286da24065)

Ver.20   [Related Products](../../tree/63044ea74568af081da40e82463563c1e21c3c5d)

Ver.21   [Random Queryset & Improve UI](../../tree/8caff80a980b86bde64d96c935a81adf78d99fc6)

Ver.22   [Django Template Include with Variable](../../tree/fadf4226136c30771842a634cdfee77e027af9b1)

Ver.23   [Featured Product on Homepage](../../tree/7e19c21fa3b79d008bebcd308e55509d620341e5)

Ver.24   [Login as Dropdown Menu](../../tree/65745ff26fce6edce2ad4949a598c0c76275d34c)

Ver.25   [Shopping Cart Icon](../../tree/854d0f652c4f44574eab1cb9edccfed591f77d7e)

Ver.26   [Product Lists on Homepage](../../tree/a7cff334892cbbad8d32ea2d4420c94a6b12947a)

Ver.27   [Product Editing with Django Admin Inlines](../../tree/6cb781747bf1d5db898f278a491345850364dd3b)

Ver.28   [Carts App & ManyToMany Through](../../tree/be63dbdfe840629364becf6380fb105b21c3bc67)

Ver.29   [Cart in a CBV & Django Sessions](../../tree/60b068bc51fe7b51667d9e884cb399f25d828fbf)

Ver.30   [Render Cart View](../../tree/f13d068a9854c2304c0849605a0ca33ac414fbf9)

Ver.31   [Add to Cart & Update Cart View](../../tree/386d37dbfdc1a17ff07d70869e3b512584b56db7)

Ver.32   [Cart Line Item Total & Subtotal](../../tree/599e35fd57be23704076e7771026460bf9f37253)

Ver.33   [Ajax](../../tree/d460896f40e8a707bc12e1394c1c9f55c83b983b)

Ver.34   [jQuery Flash Message](../../tree/cbb0152063a9cc75dad7717384bca10355e4d937)

Ver.35   [Display Message from Server](../../tree/ae5003710564b1b86134fd64c9a2155967642f33)

Ver.36   [Empty Cart](../../tree/6b32822ee3cbb97c085963f0671bcc55e8465c6c)

Ver.37   [Cart Count in Navbar](../../tree/fde5a942ae6574a2e5868b8c742e8cf6fc7fe7ed)

Ver.38   [Cart Total & Taxes](../../tree/9395fe3dea0e5939d155a02f4049f6ddd8e53bae)

Ver.39   [Checkout View](../../tree/9b03250d702f81a03fc52b134af93be7c459e3bf)

Ver.40   [Orders App & Checkout for Guest](../../tree/14c7ee66a9528aa2cf0cde3c4026946045b530d6)

Ver.41   [UserAddress Model & View](../../tree/275df9629cca1d96bb29911555fec5c2f13e2021)

Ver.42   [Order Model](../../tree/49ca84365d3bd84b586b2049b2e5dab278b39eb8)

Ver.43   [Crafting the Order](../../tree/39f1c4d98ed6133508a1fa78ea413ca70de63f11)

Ver.44   [Custom Mixin for Cart & Order](../../tree/d1902ef3c7c70d0e73132d1f69cfbc9f52b1a939)

Ver.45   [Checkout Finalize View & Order List](../../tree/231f5b2efc49287d8dddd41daa88b2dcae1141ed)

Ver.46   [Order Detail](../../tree/c0c0e1f1801b8deebbd0118985e74032ea1fff37)

Ver.47   [Braintree & Customer ID](../../tree/97a70d970229da1bebab0c3b214813d38dd5873d)

Ver.48   [Braintree Instance Methods](../../tree/cd80ba62037eff4767031983e5f74ac8e7252dd5)

Ver.49   [Run Braintree Transaction](../../tree/60f16abaff5189fbce4b6765c1f6f7890aba236c)

Ver.50   [UI Updates](../../tree/eb384f243449f53153ca342987673a1eefe895e7)

Ver.51   [Advanced Filter for Product List](../../tree/eb6fa98c41cf82d83194f5fcaa80b7ddc73a325b)

**Release 1   [v1.0](../../tree/v1.0)** _(Stable Ver.)_

Ver.53   [REST framework Installation](../../tree/c06ba4568547436707183cf19b9eaf4208c64d86)

Ver.54   [Model Serializers & API List View](../../tree/2b5617a6beca64e0e9d8c80530cdb4ef5ae25000)

Ver.55   [API Retrieve View & URL](../../tree/456ade2ab067edcdc55079516e7d1349b60aeb68)

Ver.56   [Product & Variation Serializers](../../tree/a86d1e54537423c6a196f35c19b71ebfa68d2668)

Ver.57   [Product List & Retrieve View](../../tree/0370f3d95472b98bcc6d03837cc43bbc9de1844b)

Ver.58   [Permissions](../../tree/8dc6f528fc552bf361e151a90928b418ccb2b16a)

Ver.59   [Authentication](../../tree/2cdc011fce2ac35c817cb26c11b88700b9a59d45)

Ver.60   [Pagination](../../tree/0a5a48ca4a6d30cb6231fe6ffc0d4c92adb74cc2)

Ver.61   [Filtering the API](../../tree/8cc0b8c64c8ab46570504fe85aceffbc9d86fe07)

Ver.62   [Using a Base API View](../../tree/fe07b9455b0c91929b105dd5185b436b5346e4d9)

Ver.63   [User Checkout](../../tree/cf667f6cc6f3c06bd1e00cc3e30eba7310cac957)

Ver.64   [Auth with JWT Tokens](../../tree/2a0750778263d774142cf15b04892ec73d593291)

Ver.65   [Testing JWT Tokens with Python Requests](../../tree/56d1b814ecdab374abe0e99f32ff10b15a6c9068)

Ver.66   [JWT Tokens Refresh](../../tree/1ce9fa387b8a7494ed67b395ce5c4c36921db943)

Ver.67   [Cart API View & Token](../../tree/e35c7b2fee224538bb40699053ff3b1137b605b2)

Ver.68   [Update Cart in API & Test](../../tree/6348aeba99ed187ee1d695ae647a93f081365e27)

Ver.69   [Display Cart Items](../../tree/dc68726411c0f48d76852e83a9ad477f7a625b9c)

Ver.70   [Token Mixin](../../tree/9b90e8c87717f268f5a9945c631d7ff8bd2285d5)

Ver.71   [Initiate Checkout API View & CartToken Mixin](../../tree/9849d08259615f80c891431caedeb1fdcb6e3946)

Ver.72   [Order Serializer & Add User to Checkout](../../tree/bc79d4764095c6eef57b0137bb32906472761174)

Ver.73   [User Address Create & List](../../tree/292551d06c09afa134d5a55ca785600547dd407c)

Ver.74   [Finalize Checkout API View](../../tree/1afb87da9c09e7d3b42bf0caf38de078b11f252a)

Ver.75   [Custom Serializer & Validation & API Test for Checkout](../../tree/bdafa9eb61c3e95ff12b87cf08956d5f808bd6f8)

Ver.76   [Order from Validated Data](../../tree/48d3bb10c78a7c3c3a4d03e80ae310dccc45d404)

Ver.77   [Finalize Order Serializer](../../tree/227fabdf8b8dde7a34081baa369ea2648b1eb600)

Ver.78   [Finalize Order API View](../../tree/601527f7b596b77b593152bc114c8efdd570b3eb)

Ver.79   [Get Client Token](../../tree/1a7d5c95f268569dd23c139e79ee35dab86956b0)

Ver.80   [Payment Transactions](../../tree/5b4de4db99402c41f3106def608bd52318371244)

Ver.81   [Django CORS Headers](../../tree/0c300d4add2ec55cf4042a6c6e9207bca52ec4a9)

Ver.82   [Order List & Retrieve API](../../tree/26197db25bbda929639b9bc7f4d4f38387bacb35)

Current Ver.   API Home Final