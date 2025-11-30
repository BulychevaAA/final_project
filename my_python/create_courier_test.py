import sender_stand_request

def test_create_courier():
    create_courier_response = sender_stand_request.create_courier()
    assert create_courier_response.status_code == 201
    print("Курьер создан успешно!")

test_create_courier()