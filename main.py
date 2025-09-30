"""
Version -> 1.0.0
Devloper -> Danial-ErfanDost
"""
import os
from typing import Optional
from irancell.config import Banner
from irancell.Refrer import MyIrancell


Banner()

def main(token: str , log:bool , loop:int , sleep:int) -> None:
    if token and log:
        Account:Optional[MyIrancell] = MyIrancell(file_log=log)
        Account.set_token(token=token)
        Account.run(loop=loop , sleep=sleep)
    elif token:
        Account:Optional[MyIrancell] = MyIrancell()
        Account.set_token(token=token)
        Account.run(loop=loop , sleep=sleep)
    
    else:
        exit("token not finde".title())


name_file = "token.tk"
token = None

if os.path.exists(name_file):
    with open(name_file, "r") as file:
        token = file.readline().strip()

log_file = bool(input("log [True or False  ] enter ?:"))
try_loop = int(input("loop ? :"))
sleep = int(input("sleep ?:"))

if token and len(token) > 50:
    main(token=token , log=log_file , loop=try_loop , sleep=sleep)
else:
    token = input("Enter token: ").strip()
    main(token=token , log=log_file , loop=try_loop , sleep=sleep)