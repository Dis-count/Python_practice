import  requests
import time

def translate(url,info):

    data = {}  # 字典  请求方式 post

    data['i'] = info  # 字符串类型
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'false'

    result = requests.post(url,data = data).json()

    return result['translateResult'][0][0]['tgt']

if __name__ ==  '__main__':

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    while 1:
        info = input('please input the content(q for end):')

        if info == 'q':
            break
        else:
            result = translate(url,info)
            print(result)
            time.sleep(3)
            continue
