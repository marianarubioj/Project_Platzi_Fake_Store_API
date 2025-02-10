import data
import sender_stand_request
import requests

def test_get_all_products():
    response = sender_stand_request.get_all_products()
    assert response.status_code == 200
    return response.json()

def test_get_all_products_by_id():
    response = sender_stand_request.get_all_products_by_id()
    products_id= response.json()
    for product_id in products_id:
        assert 'id' in product_id, f"Product_id{product_id} doesn't have an id key"
    ids = [product_id ['id'] for product_id in products_id]
    assert response.status_code == 200
    return ids

def test_get_a_product_by_id(id="7"):
    response = sender_stand_request.get_product_by_id(id)
    assert response.status_code == 200
    return response.json()


def test_get_all_products_by_title():
    response = sender_stand_request.get_all_products_by_title()
    products_title = response.json()
    for product_title in products_title:
        assert "title" in product_title, f"product_id{product_title} doesn't have an title key"
    titles = [product_title['title'] for product_title in products_title]
    assert response.status_code == 200
    return titles

def test_get_product_by_title():
    title = data.product_title
    response = sender_stand_request.get_product_by_title(title)
    current_body = response.json()
    print(f"Request URL: {response.url}")
    assert response.status_code == 200
    if current_body:
        product_title = current_body[0]
        assert product_title['title'] == title, f"the title is {product_title['title']}"
    if __name__  == "__main__":
        test_get_product_by_title()
    return current_body

def test_post_product():
    product_body = data.product_body
    response = sender_stand_request.post_product(product_body)
    assert response.status_code == 201
    return response.json()

def test_put_product():
    product_created = test_post_product()
    product_id = product_created['id']
    response = sender_stand_request.put_product(product_id, data.updated_product_body)
    assert response.status_code == 200
    return response.json()
