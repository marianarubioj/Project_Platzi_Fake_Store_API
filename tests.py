import sender_stand_request, data
from data import product_id
from sender_stand_request import get_a_product_by_id


def test_get_all_products():
    response = sender_stand_request.get_all_products()
    current_body = response.json()
    assert response.status_code == 200
    return current_body

def test_get_a_product_by_id(id="7"):
    response = sender_stand_request.get_a_product_by_id(id)
    current_body = response.json()
    assert response.status_code == 200
    return current_body


#def test_get_info_by_product():



