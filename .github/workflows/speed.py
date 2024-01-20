import websocket
import ssl
import os
import json
import gzip
import requests
from time import sleep
import random
import concurrent.futures
from telegram import Bot
import colorama
from colorama import Fore

colorama.init(autoreset=True)

created = 0
failed = 0

L = '\033[1;33m'
C = "\033[1;97m"
B = '\033[2;36m'
Y = '\033[1;34m'
X = '\037'
G = '\033[1;32m'
R = '\033[1;31m'

# شكل لتزيين الإخراج
decoration = f'''
▄▀▀ █▀▄ █▀▀ █▀▀ █▀▄ 
░▀▄ █░█ █▀▀ █▀▀ █░█ 
▀▀░ █▀░ ▀▀▀ ▀▀▀ ▀▀░ 
'''

print(Y + 'مرحبًا بك في أداة إنشاء حسابات Safeum')
print(Y + 'أرسل لي رسالة على تليجرام: @l_s_i_i')
print(C + "∞" * 60)

# اطلب التوكن والايدي عند تشغيل الأداة
token = input(f'{L}أدخل توكن بوت التليجرام الخاص بك: ')
id = input(f'{L}أدخل معرف المستخدم الخاص بك على تليجرام: ')

os.system('clear')

bot = Bot(token=token)

# رسالة ترحيب
welcome_message = f'''
{Fore.GREEN}========================================
{Fore.GREEN}مرحبًا بك في أداة إنشاء حسابات Safeum!
{Fore.GREEN}========================================
{Fore.CYAN}أنشئ حسابات مجانية لتطبيق Safeum.
{Fore.CYAN}سيتم إرسال الحسابات التي تم إنشاؤها إلى تليجرام الخاص بك.
{Fore.CYAN}========================================
{decoration}
'''

print(welcome_message)

import time

time.sleep(5)

def generate_username(length=15):
    ch = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
    return random.choice('qwertyuioplkjhgfdsazxcvbnm') + ''.join(random.choice(ch) for i in range(length - 1))

def create():
    global created
    global failed
    user = generate_username(15)
    password = 'hhhh'  # كلمة المرور

    tlg = f'''
⋘─────━𓆩ᔆ ᴾ ᴱ ᴱ ᴰ ™ 𝓼𓆪‏━─────⋙
˛ U𝗌𝖾𝗋  : {user}
˛ 𝖯𝖺𝗌𝗌𝗐𝗈𝗋𝖽 : {password}
⋘─────━𓁥@l_s_I_I������������━─────⋙

BY : @l_s_i_i | @speed_24_1
'''

    headers = {
        "app": "com.safeum.android",
        "host": None,
        "remoteIp": "134.209.93.148",
        "remotePort": str(8080),
        "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
        "time": "2023-04-30 12:13:32",
        "url": "wss://51.79.208.190/Auth"
    }

    data0 = {
        "action": "Register",
        "subaction": "Desktop",
        "locale": "en_GB",
        "gmt": "+02",
        "password": {
            "m1x": "503c73d12b354f86ff9706b2114704380876f59f1444133e62ca27b5ee8127cc",
            "m1y": "6387ae32b7087257452ae27fc8a925ddd6ba31d955639838249c02b3de175dfc",
            "m2": "219d1d9b049550f26a6c7b7914a44da1b5c931eff8692dbfe3127eeb1a922fcf",
            "iv": "e38cb9e83aef6ceb60a7a71493317903",
            "message": "0d99759f972c527722a18a74b3e0b3c6060fe1be3ad53581a7692ff67b7bb651a18cde40552972d6d0b1482e119abde6203f5ab4985940da19bb998bb73f523806ed67cc6c9dbd310fd59fedee420f32"
        },
        "magicword": {
            "m1x": "04eb364e4ef79f31f3e95df2a956e9c72ddc7b8ed4bf965f4cea42739dbe8a4a",
            "m1y": "ef1608faa151cb7989b0ba7f57b39822d7b282511a77c4d7a33afe8165bdc1ab",
            "m2": "4b4d1468bfaf01a82c574ea71c44052d3ecb7c2866a2ced102d0a1a55901c94b",
            "iv": "b31d0165dde6b3d204263d6ea4b96789",
            "message": "8c6ec7ce0b9108d882bb076be6e49fe2"
        },
        "magicwordhint": "0000",
        "login": str(user),
        "devicename": "Xiaomi Redmi Note 8 Pro",
        "softwareversion": "1.1.0.1380",
        "nickname": "hvtctchnjvfxfx",
        "os": "AND",
        "deviceuid": "c72d110c1ae40d50",
        "devicepushuid": "*dxT6B6Solm0:APA91bHqL8wxzlyKHckKxMDz66HmUqmxCPAVKBDrs8KcxCAjwdpxIPTCfRmeEw8Jks_q13vOSFsOVjCVhb-CqqKmTUsaiS7YOYHQS_pbH1g6P4N-jlnRzySQwGvqMP1gxRVksHiOXKKP",
        "osversion": "and_11.0.0",
        "id": "1734805704"
    }

    ws = websocket.create_connection("wss://51.79.208.190/Auth", header=headers, sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.send(json.dumps(data0))
    result = ws.recv()
    decoded_data = gzip.decompress(result)

    if '"comment":"Exists"' in str(decoded_data):
        failed += 1
    elif '"status":"Success"' in str(decoded_data):
        created += 1
        bot.send_message(chat_id=id, text=tlg)
        # إضافة الحساب الناجح إلى ملف
        with open('successful_accounts_speed.txt', 'a', encoding='utf-8') as file:
            file.write(f"{tlg}\n")
    elif '"comment":"Retry"' in str(decoded_data):
        failed += 1
    else:
        print(decoded_data)

# تحديث الكود لاستخدام multithreading
executor = concurrent.futures.ThreadPoolExecutor(max_workers=600)

while True:
    executor.submit(create)
    os.system('clear')
    print(C + "أنشئ حسابًا مجانيًا لتطبيق Safeum")
    print(L + "\u221e" * 60)
    print(G + ' ناجحة : ' + str(created))
    print(R + ' عدد المحاولات : ' + str(failed))
    print(L + "\u221e" * 60)
    print(C + f"حسابي في تليجرام: @l_s_i_i | قناتي في تليجرام: @l_s_i_i")
