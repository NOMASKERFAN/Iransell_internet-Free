from random import sample
from requests import post
import requests.exceptions
from colorama import Fore
from config import log
import time



class MyIrancell:
    def __init__(self, token: str = "", file_log: bool = False) -> None:
        """Config Account"""
        self.__token = token
        self.file_log = file_log
        self.__data = {
            'application_name': 'NGMI',
            'friend_numbers': '98'
        }

        self.__header_check_number = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'fa',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://my.irancell.ir/sim/profile',
            'x-app-version': '9.53.0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Authorization': self.__token,
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
        }

        self.__header_send = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'fa',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/json',
            'Referer': 'https://my.irancell.ir/invite/confirm',
            'x-app-version': '9.53.0',
            'Origin': 'https://my.irancell.ir',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Authorization': self.__token,
            'Connection': 'keep-alive',
            'Priority': 'u=0'
        }

    def __str__(self):
        return f"Token={self.__token[:10]}..., Logging={self.file_log}"


    def __repr__(self):
        return f"{self.__class__.__name__}(token='{self.__token[:6]}...', file_log={self.file_log})"


    def set_token(self, token: str):
        """Set account token"""
        if not token:
            raise ValueError("Token cannot be empty!")
        self.__token = token
        self.__header_check_number['Authorization'] = self.__token
        self.__header_send['Authorization'] = self.__token
        return "Token set successfully"

    def get_token(self):
        """Get current token"""
        return self.__token

    def __random_number(self):
        """Generate random mobile number"""
        return '933' + ''.join(sample('1234567890', 7))

    def __find_number(self, number: str):
        """Send request to check the number"""
        self.__data['friend_number'] = '98' + number
        url = 'https://my.irancell.ir/api/gift/v1/refer_a_friend'
        return post(url, json=self.__data, headers=self.__header_check_number)

    def __send_url(self):
        """Send referral notification"""
        url = 'https://my.irancell.ir/api/gift/v1/refer_a_friend/notify'
        return post(url, json=self.__data, headers=self.__header_send)

    def run(self, loop: int = 20, sleep: int = 0) -> str:
        """Start the process"""
        numbers = []
        if not self.get_token():
            exit("Token not set.")

        for _ in range(loop + 1):
            try:
                number = self.__random_number()
                response = self.__find_number(number=number)
                if response.text == '{"message":"done"}':
                    print(f"{Fore.YELLOW}Found number : {Fore.LIGHTBLACK_EX}{number}")
                    if self.__send_url().text == '{"message":"done"}':
                        if self.file_log:
                            log(data=number)
                        numbers.append(number)
                        print(f"{Fore.GREEN}Send URL {Fore.MAGENTA}")
                        print(Fore.LIGHTWHITE_EX + "-" * 40)
                        if sleep > 0:
                            time.sleep(sleep)
            except requests.exceptions.ConnectionError:
                exit("Check your internet connection.")
        print(len(numbers))