import requests
import os
import sys
import time
import psutil
import platform
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import requests
import time
from time import strftime
import os
import requests
import urllib.parse
from time import strftime
import os
from datetime import datetime
from time import sleep, strftime
import datetime
import uuid
import json
import sys
import random
import string
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import threading
from colorama import init, Fore  # Đảm bảo rằng thư viện colorama được import đúng cách

# Định nghĩa các màu
trang = Fore.WHITE
xanh_la = Fore.GREEN
xanh_duong = Fore.BLUE
do = Fore.RED
vang = Fore.YELLOW
tim = Fore.MAGENTA
xanhnhat = Fore.CYAN
reset = Fore.RESET
purple = "\033[1;35m"
bold = "\033[1m"
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
cyan = "\033[96m"

# Đánh dấu bản quyền
HĐ_tool = trang + trang + "[ " + do + "Bản quyền" + trang + " ] => "
mquang = trang + trang + "[ " + do + "Quảng cáo" + trang + " ] => "
thanh = trang + trang + '-------------------------------------------------------------------------'

# Hàm xóa màn hình
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Lấy ngày giờ hiện tại

# Lấy địa chỉ IP công cộng

# Lấy thông tin vị trí từ IP
        
# Hàm lấy thông tin hệ điều hành

# Lấy thông tin RAM (đã sử dụng và còn lại)


# Lấy thời tiết từ OpenWeatherMap

# Function to display banner with dynamic data
clear_screen()
banner(sokey)
# Hàm chính

username = input(f"{Colorate.Diagonal(Colors.blue_to_red, 'Nhập Username: ')}{reset}")
nd = input(f"{Colorate.Diagonal(Colors.blue_to_green, 'Nhập Nội Dung: ')}{reset}").replace(" ", " ")
so_lan = int(input(f"{Colorate.Diagonal(Colors.blue_to_purple, 'Nhập số lần gửi: ')}{reset}"))

url = "https://ngl.link/api/submit"
headers = {
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent": "Mozilla/5.0",
    "origin": "https://ngl.link",
    "referer": f"https://ngl.link/{username}"
}

for i in range(so_lan):
    data = {
        "username": username,
        "question": nd,
        "deviceId": str(uuid.uuid4()),
        "gameSlug": "",
        "referrer": ""
    }
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200 and "questionId" in response.json():
        print(f"{Fore.GREEN}Đã gửi {Fore.YELLOW}{i + 1} {Fore.CYAN}lần {Fore.MAGENTA}Nội Dung: '{nd}' {Fore.WHITE}Đến: '{username}' {Fore.GREEN}Trạng Thái: Thành Công {Fore.RESET}")
    elif "Could not find user" in response.text:
        print(f"{Fore.RED}Username Sai Hoặc Không Hợp Lệ!{Fore.RESET}")
        break
    else:
        print(f"{Fore.GREEN}Đã gửi {Fore.YELLOW}{i + 1} {Fore.CYAN}lần {Fore.MAGENTA}Nội Dung: '{nd}' {Fore.WHITE}Đến: '{username}' {Fore.GREEN}Trạng Thái: {Fore.RED} Thất Bại{Fore.RESET}")
