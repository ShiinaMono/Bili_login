from cgitb import reset
from lib2to3.pgen2 import token
from modulefinder import packagePathMap
import requests as r
import os, sys , time
import json
from MyQR import myqr
from PIL import Image
import matplotlib.pyplot as plt
from urllib.parse import urlparse
from ttt import imggg

a = os.path.exists('./config')
if a == False :
    path = "./config"
    os.mkdir(path)

def getpic():
    headers = {
            'User_Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
    }
    url = "https://passport.bilibili.com/qrcode/getLoginUrl"
    result = r.get(url, headers=headers)
    pdd = result.text
    with open('./config/config.json', 'w') as f:
        f.write(pdd)
    with open('./config/config.json', 'r') as config:
        af = json.load(config)
    ddt = af.get("data").get("url")
    oauthkey = af.get("data").get("oauthKey")
    myqr.run(
        words=ddt,
        colorized=True,
        save_name="./config/scanme.png"
    )
    return ddt, oauthkey


def post(oauthkey):
    headers = {
        "Content-Type" : "application/x-www-form-urlencoded" ,
        'User_Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
    }
    url = "https://passport.bilibili.com/qrcode/getLoginInfo"
    data = {
        "oauthKey": oauthkey
    }
    # test = r.post(url, data=data,headers=headers)
    # pdd = test.text
    plp = r.Session()
    pdd = plp.post(url, data=data,headers=headers)
    plpp = pdd.text
    with open('./config/data.json', 'w') as f:
        f.write(plpp)
    with open('./config/data.json', 'r') as config:
        af = json.load(config)
    trust = af.get("data")
    uuu = af.get("data").get("url")
    print(trust)
    return trust,uuu
    # return trust

def token(uuu):
    result = urlparse(uuu,allow_fragments=False)
    result_query = result.query
    a = ''.join(result_query)
    b = a.split('&')
    uuiidd = b[0].split('=')
    uid = uuiidd[1]
    sess = b[3].split('=')
    sessdata = sess[1]
    bili = b[4].split('=')
    bilijct = bili[1]
    # print(uid,sessdata)
    return uid,sessdata,bilijct
# def turnpic(ddt):
#     myqr.run(
#         words=ddt,
#         colorized=True,
#         save_name="1.jpg"
#     )

def main():
    while True:
        ddt, oauthkey = getpic()
        imggg()
        trust,uuu = post(oauthkey)
        s = isinstance(trust,int)
        if s == False:
            print("已登陆")
            uid,sessdata,bilijct = token(uuu)         
            break
        elif s == "-5" :
            print("已扫描二维码，等待确认15s")
            time.sleep(15)
            continue
        elif s == "-2" :
            print("二维码已过期")
            time.sleep(5)
            continue
        elif s == "-4" :
            print("二维码未扫描")
            time.sleep(15)
        # print(trust)
    return uid,sessdata,bilijct

# def youxiang(sessdata) :
#     headers = {
#         'User_Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36" ,
#         "SESSDATA": sessdata ,
#         "Content-Type" : "application/x-www-form-urlencoded"
#     }
#     url = 'https://api.bilibili.com/x/web-interface/card'
#     data = {
#         "mid" : 2 
#     }
#     result = r.get(url,headers=headers)
#     result_text = result.text
#     print(result_text)


if __name__ == "__main__":
    # main()
    uid,sessdata,bilijct=main()
    # youxiang(sessdata)
