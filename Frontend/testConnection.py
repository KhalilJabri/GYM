# import requests
import socket

url = 'http://www.google.com'
timeout = 1
CC, LC = 0, 0
while True:
    # try :
    #     requests.get(url=url, timeout=timeout)
    #     if CC == 0:
    #         print('connected.')
    #         CC+=1
    #         if LC == 1:
    #             LC -=1
    # except :
    #     if LC == 0:
    #         print('lost connection !!')
    #         LC+=1
    #         if CC == 1:
    #             CC -=1
    try:
        socket.create_connection(('Google.com',80))
        if CC == 0:
            print('connected.')
            CC+=1
            if LC == 1:
                LC -=1
    except OSError:
        if LC == 0:
            print('lost connection !!')
            LC+=1
            if CC == 1:
                CC -=1