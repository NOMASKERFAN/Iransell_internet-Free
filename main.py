"""
Version -> 1.0.0
Devloper -> Danial-ErfanDost
"""
import os
from typing import Optional
from iransell.config import Banner
from iransell.Refrer import MyIrancell


Banner()

def main(token: str , log:bool , loop:int , sleep:int) -> None:
    if log and loop and sleep:
        Account:Optional[MyIrancell] = MyIrancell(file_log=log)
        Account.set_token(token=token)
        Account.run(loop=loop , sleep=sleep)
    else:
        Account:Optional[MyIrancell] = MyIrancell()
        Account.set_token(token=token)
        Account.run()


name_file = "token.tk"
token = None

if os.path.exists(name_file):
    with open(name_file, "r") as file:
        token = file.readline().strip()

log_file = input("log ?:")
try_loop = int(input("loop ? :"))
sleep = int(input("sleep ?:"))

if token and len(token) > 50:
    main(token=token , log=log_file , loop=try_loop , sleep=sleep)
else:
    token = input("Enter token: ").strip()
    main(token=token , log=log_file , loop=try_loop , sleep=sleep)