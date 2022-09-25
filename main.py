# from scripts.qrcode import main as qrmain
from scripts.touxiang import gettop,top
from scripts.input import puup
import uuid 
from scripts import qrcode
from scripts import post


# print(uid,sessdata,uuid)

if __name__ == "__main__" :
    uuid_r = uuid.uuid1
    uid,sessdata,bilijct = qrcode.main()
    headers = {
            'Connection': 'close', 'User-Agent': 'Mozilla/5.0',
            'Cookie': f'uid="{uid}";_uuid="{uuid_r}";SESSDATA="{sessdata}"'
        }
    year = puup()
    post.main(year,headers,uid)
    top()