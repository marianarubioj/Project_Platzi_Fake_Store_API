import pytest
import requests
import data
import configuration as c

#Get all products
def get_all_products():
    response = requests.get(c.URL_SERVICE + c.GET_PRODUCTS)
    return response

#Get a single product through the id key
def get_a_product_by_id(id):
    response = requests.get(c.URL_SERVICE + c.GET_PRODUCTS + id)
    return response


#Get the value of a product key
def get_info_by_product():
    response = requests.get(c.URL_SERVICE + c.GET_PRODUCTS)
    response_status_code = response.status_code
    response_body = response.json()
    assert response_status_code == 200, "The status to get product's price isn't 200"
    price_tshirt = response_body[0]["price"]
    title_shirt = response_body[0]["title"]
    return price_tshirt, title_shirt

#Create a product
def post_product(body):
    response = requests.post(c.URL_SERVICE + c.CREATE_PRODUCTS, json=body)
    response_status_code = response.status_code
    assert response_status_code == 201, "The status to create a product isn't 201"
    return response.json()

r = post_product(data.product_body)
print(r)