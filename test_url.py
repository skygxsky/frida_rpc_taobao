import requests
from urllib.parse import unquote, quote, urlencode


def test1():
    """
    今日爆款
    :return:
    """
    url = 'https://guide-acs.m.taobao.com/gw/mtop.tmall.kangaroo.core.service.route.aldlampservicefixedres/1.0/?data=%7B%22debug%22%3A%22false%22%2C%22params%22%3A%22%7B%5C%22pageName%5C%22%3A%5C%22440%5C%22%2C%5C%22pageNum%5C%22%3A1%2C%5C%22pageSize%5C%22%3A20%2C%5C%22bizId%5C%22%3A%5C%2220200109%5C%22%2C%5C%22resId%5C%22%3A%5C%226783431%5C%22%2C%5C%22version%5C%22%3A1%2C%5C%22backupParams%5C%22%3A%5C%22pageName%2CpageNum%2CpageSize%2Cversion%5C%22%7D%22%7D'
    headers = {'x-extdata': 'openappkey%3DDEFAULT_AUTH', 'x-features': '1051',
               'x-sgext': 'JAFKd8NxaJRPHPoc%2FTEBzHQ%3D', 'c-launch-info': '1,0,1631862698082,1631862038000,2',
               'x-page-name': 'com.taobao.windmill.bundle.TBWMLActivity', 'x-location': '118.185256%2C24.489316',
               'user-agent': 'MTOPSDK%2F3.1.1.7+%28Android%3B6.0.1%3BHuawei%3BNexus+6P%29',
               'x-ttid': '10007875%40taobao_android_9.12.0', 'x-region-channel': 'CN', 'x-appkey': '21646297',
               'x-nq': 'WIFI',
               'x-mini-wua': 'HHnB_jXzaCe7FXRZMlTickUWtNGZ8q%2FzGXdyu67G3f1ROM5V4T6xt8odSewSu2EysZ4JqpRNmCvJi4GsKYc6qpX3e4E%2BM2OrPqdOQ%2FXg2OQxG7suqX61R%2BdGgn2ewj4qzDbCwO9T6kOCG7f%2BGBP%2BIrhWfOw%3D%3D',
               'x-c-traceid': 'YUQ9E5VlN9gDAFZzei6OeEqP16318626980820489128972', 'x-app-conf-v': '0',
               'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'A-SLIDER-Q': 'appKey%3D21646297%26ver%3D1631861416506', 'x-bx-version': '6.5.12', 'x-pv': '6.3',
               'x-t': '1631862698', 'x-app-ver': '9.12.0', 'f-refer': 'mtop',
               'x-ua': 'Nexus+6P%28Android%2F6.0.1%29+AliApp%28TB%2F9.12.0%29+Weex%2F0.26.4.45+1440x2392',
               'Cookie': 'thw=cn; enc=fkWScIm66IZo%2BDuZwNFWbJosq7SpeOuCRsg3S3ladoYfqqrWYEGveJGDrokaYHha%2Ba2tbsfMyCpt%2Fawt6RPrd8xJ%2F8X6kjwCP9zZ0fZ3kigL4e0Zj02Edsx7LVIvvBxP',
               'x-nettype': 'WIFI', 'x-utdid': 'YUQ9E5VlN9gDAFZzei6OeEqP', 'x-umt': 'o7wAJRVLPMop2wJ78vtlpjp7kOuRFohw',
               'a-orange-dq': 'appKey=21646297&appVersion=9.12.0&clientAppIndexVersion=1120210917145800647',
               'x-devid': 'AloI4YMLRb5pW22VJsCeMOtsitGnrHORub81cr2bVUHY',
               'x-sign': 'azYBCM002xAAJYAGf%2Fg%2BRtzYLukUxYAFgWZUQ5ebTyzc6JAJugEzwj17gCI%2FKnWAMQ%2BJBuzsxoVzT6QJ0DTEsSFBIpWgJYAFgCWABY',
               'x-page-url': 'https%3A%2F%2Fsnipcode.taobao.com%2F12017757%2Fpages%2Findex%2Findex.js%3Futparam%3D%257B%2522ranger_buckets_native%2522%253A%2522tsp2189_11190_normaluser01%2522%257D%26spm%3Da2141.1.iconsv5.2%26scm%3D1007.home_icon.juhs.d',
               'Host': 'guide-acs.m.taobao.com', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive'}
    response = requests.get(url,headers=headers).json()
    print(response)
    print(unquote(url))
print(unquote('https://guide-acs.m.taobao.com/gw/mtop.tmall.kangaroo.core.service.route.aldlampservicefixedres/1.0/?data=%7B%22debug%22%3A%22false%22%2C%22params%22%3A%22%7B%5C%22pageName%5C%22%3A%5C%22530%5C%22%2C%5C%22pageNum%5C%22%3A2%2C%5C%22pageSize%5C%22%3A20%2C%5C%22bizId%5C%22%3A%5C%2220200109%5C%22%2C%5C%22resId%5C%22%3A%5C%226783431%5C%22%2C%5C%22version%5C%22%3A1%2C%5C%22backupParams%5C%22%3A%5C%22pageName%2CpageNum%2CpageSize%2Cversion%5C%22%7D%22%7D'))

if __name__ == '__main__':
    test1()
