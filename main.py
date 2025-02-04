import requests
import data

#Get all products
def get_all_products():
    response = requests.get(data.url + data.get_products)
    response_status_code = response.status_code
    assert response_status_code == 200, "The status to get a product isn't 200"
    return response.json()

#Get a single product through the id key
def get_a_product_by_id(id):
    response = requests.get(data.url + data.get_products + id)
    response_status_code = response.status_code
    assert type(id) == str
    assert response_status_code == 200, "The status to get a product through the id isn't 200"
    return response.json()

#Get the value of a product key
def get_info_by_product():
    response = requests.get(data.url + data.get_products)
    response_status_code = response.status_code
    response_body = response.json()
    price_tshirt = response_body[0]["price"]
    title_shirt = response_body[0]["title"]
    assert response_status_code == 200, "The status to get product's price isn't 200"
    return price_tshirt, title_shirt

#Create a product
def post_product(body):
    response = requests.post(data.url + data.post_product, json=body)
    response_status_code = response.status_code
    assert response_status_code == 201, "The status to create a product isn't 201"
    return response.json()

r = post_product(data.product_body)
print(r)