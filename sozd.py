import configuration

import requests

import data

#создание курьера

def post_new_kur(kur_body):
    return requests.post(configuration.URL_SERVICE + configuration.creat_kur_path,
                        json=kur_body,
                        headers=data.headers)


def create_kurs():
    for d in range(5):
        f=data.kur_body
        f["login"] = f"ninja{d}"
        res = post_new_kur(f)


#create_kurs()

#создание заказа

def post_new_older(older_body):
    return requests.post(configuration.URL_SERVICE + configuration.creat_order_path,
                        json=older_body,
                        headers=data.headers)

def create_olders():
    for d in range(10):
        f=data.order_body
        f["address"] = f"Konoha, 142 apt.{d+1}"
        res = post_new_older(f)
        #res = post_new_older(data.order_body)

create_olders()        