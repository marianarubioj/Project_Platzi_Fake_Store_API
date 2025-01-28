import requests
import data



#Obtener todos los productos
def get_all_products():
    response = requests.get(data.url + data.get_all_products)
    response_status_code = response.status_code
    assert response_status_code == 200
    return response.json()


#Obtener un producto por medio de la clave id
def get_a_product_by_id(id):
    response = requests.get(data.url + data.get_all_products + id)
    response_status_code = response.status_code
    assert type(id) == str
    assert response_status_code == 200, "El status no es 200"
    return response.json()

r_one_product = get_a_product_by_id("1")
print(r_one_product)
