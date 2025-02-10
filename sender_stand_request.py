from http.client import responses

import requests
import configuration as c

#Get all products
def get_all_products():
    response = requests.get(c.URL_SERVICE + c.GET_PRODUCTS)
    return response

def get_all_products_by_id():
    response = requests.get(c.URL_SERVICE + c.GET_PRODUCTS)
    return response

#Get a single product through the id key
def get_product_by_id(id):
    response = requests.get(c.URL_SERVICE + c.GET_PRODUCTS + id)
    return response

def get_all_products_by_title():
    response = requests.get(c.URL_SERVICE + c.GET_PRODUCTS)
    return response

#Get a single product through the title key
def get_product_by_title(title):
    params = {
        'title': title
    }
    response = requests.get(c.URL_SERVICE + c.GET_PRODUCTS, params=params)
    return response

#Create a product
def post_product(body):
    response = requests.post(c.URL_SERVICE + c.CREATE_PRODUCTS, json=body)
    return response

def put_product(id, body):
    response = requests.put(c.URL_SERVICE + c.GET_PRODUCTS + str(id), json=body)
    return response

def delete_created_product(id):
    response = requests.delete(c.URL_SERVICE + c.GET_PRODUCTS + str(id))
    return response

def delete_product(id):
    response = requests.delete(c.URL_SERVICE + c.GET_PRODUCTS + id)
    return response