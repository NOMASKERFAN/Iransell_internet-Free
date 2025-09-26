"""
Version -> 1.0.0
Devloper -> Danial-ErfanDost
"""
import os
from typing import Optional
from config import Banner
from Refrer import MyIrancell





Banner()

def main(token: str):
    Account:Optional[MyIrancell] = MyIrancell()
    Account.set_token(token=token)
    Account.run(sleep=1)

name_file = "token.tk"
token = None

if os.path.exists(name_file):
    with open(name_file, "r") as file:
        token = file.readline().strip()

if token and len(token) > 50:
    main(token=token)
else:
    token = input("Enter token: ").strip()
    main(token=token)