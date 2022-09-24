from fileinput import filename
from urllib.parse import urlparse
import urllib.request , os
import requests , json
from PIL import Image
import matplotlib.pyplot as plt

def top():
    filename = gettop()
    img = Image.open(filename)
    plt.figure(figsize=(4,4))
    plt.ion()
    plt.axis('off')
    plt.imshow(img)
    mnmn = plt.get_current_fig_manager()
    # mnmn.window.wm_geometry("+380+380")
    plt.pause(3)
    plt.ioff()
    plt.clf()
    plt.close()

def gettop():
    with open('./config/data.json', 'r') as config:
        af = json.load(config)
    trust = af.get("data")
    uuu = af.get("data").get("url")
    result = urlparse(uuu,allow_fragments=False)
    result_query = result.query
    a = ''.join(result_query)
    b = a.split('&')
    uuiidd = b[0].split('=')
    uid = uuiidd[1]
    url = f'https://tenapi.cn/bilibili/?uid={uid}'
    result = requests.get(url)
    jr = result.text
    pic_url = json.loads(jr)
    abc = pic_url.get('data').get('avatar')
    path = './config'
    filename = f'{path}/{uid}.png'
    urllib.request.urlretrieve(abc,filename=filename)
    return filename

if __name__ == "__main__":

    top()
