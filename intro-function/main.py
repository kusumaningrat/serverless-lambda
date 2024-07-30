import json

def buy(event, context):

    name = event['name']
    price = event['price']
    description = event['description']
    username = event['username']

    product = buyProduct(name, price, description, username)

    data = json.dumps(product)

    message = "Thank you {} for buying {} with price {}\n".format(username, name, price)

    return {
        'message': message,
        'data': data
    }

def products(name, price, description):
    return {
        'name': name,
        'price': price,
        'description': description
    }

def buyProduct(name, price, description, username):
    product = products(name, price, description)
    
    print(product)
    return product
