#import numpy
#import scipy
import time
import threading
import os
#import asyncio
from image_match.goldberg import ImageSignature
import requests
#from settings import *
from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
settings = open('settings.txt').read().split("\n")
owner_id = settings[0]
#access_token = settings[1]
url = settings[2]
results1 = open('urls.txt', 'w')
off = 0
link_list = []
count = []
s = 0 #start
e = 200 #end
gis = ImageSignature()
a = gis.generate_signature(url)
access_token = os.environ.get('token1')
token = '635777694:AAHbmfWqecHTjz5R1--ZMOT3rRwuNexQknk'

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    a = requests.post(url)

def th_f(start,end):
    for i in range(start,end):
        try:
            print(i)
            last_msg = len(link_list)//200*200-2
            print('Last  ', last_msg)
            if i == last_msg:
                #221730817
                chat_id = str(221730817)
                send_message(chat_id,f'Заканчиваю работу...')
                print('Заканчиваю работу')
            n = link_list[i]
            b = gis.generate_signature(n)
            raznica = gis.normalized_distance(a, b)
            if raznica <0.4:
                print('Возможно совпадение. Отправил ссылку в телеграм')
                chat_id=str(221730817)
                message = link_list[i]
                send_message(chat_id, f'Нашел эту картинку в вашей группе. Сравните ее с той, что вы вставляли в программу! {message}')
        except:
            continue



def get_count():
    global off, count
    url ='https://api.vk.com/method/wall.get?'
    params = {'owner_id' : owner_id,
              'access_token': access_token,
              'offset' : '0',
              'v':'5.101',
              'count':'100'}
    r = requests.post(url,params=params)
    base = r.json()
    count = base['response']['count']
    return count

def get_posts(offset):
    global off, count
    url ='https://api.vk.com/method/wall.get?'
    params = {'owner_id' : owner_id,
              'access_token': access_token,
              'offset' : offset,
              'v':'5.101',
              'count':'100'}
    r = requests.post(url,params=params)
    base = r.json()
    count = base['response']['count']

    for i in range(0,count):
        try:
            a = base['response']['items'][i]['attachments']
            att_count = len(base['response']['items'][i]['attachments'])
            for j in range(0,att_count):
                try:
                    b = base['response']['items'][i]['attachments'][j]['photo']['sizes'][0]['url']
                    link_list.append(b)
                except:
                    continue
        except:
            continue
    off += 100

if __name__ == "__main__":
    threads = list()
    dlina = get_count()
    dlina = dlina//100
    print(f'Будем искать  {url}')
    print('Собираю все посты из группы...')
    for i in range(0,dlina):
        get_posts(off)
    print(len(link_list))

    print('Ищу одинаковые или похожие картинки...')

    for index in range(len(link_list) // 200):
        threading.Thread(target=th_f, args=(s, e)).start()
        s += 200
        e += 200
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
    time.sleep(1000)
