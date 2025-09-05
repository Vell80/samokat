# Валентина Мурова 33-когорта, инженер по тестированию +

import configuration

import requests

import data


#создание заказа

def post_new_older(older_body):
    return requests.post(configuration.URL_SERVICE + configuration.creat_order_path,
                        json=older_body,
                        headers=data.headers)


 
# получение заказа по номеру трека

def get_older_from_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.find_order_from_track_path + str(track),
                        headers=data.headers)


