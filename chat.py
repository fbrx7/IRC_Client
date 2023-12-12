import socket
import time
import threading
server = 'irc.libera.chat'
port = 6665
botnick = 'pyBot777'
Channel = '#web_bot_test7'

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect((server, port))

def sendr():

    while True:
    
        user_msg = input('type: ')
        Client.send(bytes(f'PRIVMSG {Channel} :{user_msg}', 'UTF-8'))


def recver():

    while True:

        txt = Client.recv(1024).decode()
        if txt.find('PING') != -1:
            Client.send(bytes('PONG ' + txt.split()[1] + '\r\n', "UTF-8"))
        print (txt)

def Auth(botnick, Channel):

    
    Client.send(bytes(f'USER {botnick} {botnick} {botnick} :THISFROMPYTHON \r\n', 'UTF-8'))
    Client.send(bytes(f'NICK {botnick} \r\n', 'UTF-8'))
    Client.send(bytes(f'NICKSERV IDENTIFY botnickpass botpass \r\n', 'UTF-8'))
    time.sleep(5)

    Client.send(bytes(f'JOIN {Channel} \r\n', 'UTF-8'))
    
    print ('Sending all Commands')


def main(server, port, botnick, Channel):

    print ('Auth will run now....')
    Auth(botnick=botnick, Channel=Channel)
    thread = threading.Thread(target=recver)
    thread2 = threading.Thread(target=sendr)
    thread.start()
    thread2.start()
    print ('Thread started')
main(server, port, botnick, Channel)