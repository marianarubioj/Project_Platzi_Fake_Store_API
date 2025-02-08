import sender_stand_request, data

def test_get_all_products():
    response = sender_stand_request.get_all_products()
    assert response.status_code == 200
    print("Status Code:", response.status_code)
    current_body = response.json()
    print(current_body)
    return current_body


#def test_get_info_by_product():



