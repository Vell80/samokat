# Валентина Мурова 33-когорта, инженер по тестированию +

import data

import sender_stand_request


# запрос на получение заказа по треку

def assertion_code_200():
    response_pno=sender_stand_request.post_new_older(data.order_body)
    track=response_pno.json()["track"]
    return sender_stand_request.get_older_from_track(track).status_code


# проверка, что код ответа равен 200

def test_get_order_from_track_code_200():
    assert assertion_code_200()==data.status_code_200



    