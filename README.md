# What is cartodb-python? #

This fork uses UltraJSON, gevent and geventhttpclient but doesn't support OAUTH yet

The cartodb-python project is a Python client for the [CartoDB SQL API](http://developers.cartodb.com/api/sql.html) that supports [authentication using OAuth](http://developers.cartodb.com/api/authentication.html).

# Installation #

Clone the repository by using:

```bash
git clone git@github.com:yoinup/cartodb-python.git
```

And them, move to dir and install it in your virtualenv

```bash
python setup.py install
```

# Usage example #

The following example requires your **CartoDB API consumer key and consumer secret** or the **API KEY**. Refer to the [CartoDB Authentication documentation](http://developers.cartodb.com/documentation/cartodb-apis.html#authentication) for details.


## using API KEY

You can get you api key in https://YOUR_USER.cartodb.com/your_apps/api_key

```python
from cartodb import CartoDBAPIKey

user =  'me@mail.com'
API_KEY ='YOUR_CARTODB_API_KEY'
cartodb_domain = 'YOUR_CARTODB_DOMAIN'

cl = CartoDBAPIKey(API_KEY, cartodb_domain)
try:
    print cl.sql('select * from mytable')
except CartoDBAPIKey.CartoDBException as e:
    print ("some error ocurred", e)
```

# running tests

clone the repo, create a secret.py from secret.py.example, fill the variables and execute:

```base
python setup.py test
```

