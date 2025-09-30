from pyfiglet import figlet_format
from colorama import Fore, Style



def Banner():
    title = figlet_format("IRANCELL Tools", font="slant")
    print(Fore.LIGHTCYAN_EX + title)

    print(Fore.YELLOW + "═" * 60)
    print(Fore.MAGENTA + " 📲 Tool    : " + Fore.WHITE + "Irancell Fake Referral Sender")
    print(Fore.MAGENTA + " 🔗 Target  : " + Fore.WHITE + "my.irancell.ir API")
    print(Fore.MAGENTA + "  ✔ Version : " + Fore.WHITE + "1.0.0")
    print(Fore.MAGENTA + " 👨‍💻 Author  : " + Fore.WHITE + "Danial-ErfanDost")
    print(Fore.YELLOW + "═" * 60 + Style.RESET_ALL)




def log(data: str , name: str = "numbers", mode: str = "a") -> None:
    if not data:
        return 

    filename = f"{name}.txt"

    with open(filename, mode) as file:
        file.write(data + "\n")