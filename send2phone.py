#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

barklink = "https://test.bark/key"
skey = "SCUxxxxxxxxxxxxx"
wj={
    "链接":"",
    "ID":"",
    "问题ID":"",
    "填空ID":""
}

rjson={
	"survey_id": wj["ID"],
	"answer_survey":""
}


base_headers = {
    "Host": "wj.qq.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
    "Origin": "https://wj.qq.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": wj["链接"],
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
}

def send2bark(title, content):
    try:
        msg = "{0}/推送标题/{1}/{2}".format(barklink, title, content)
        link = msg
        res = requests.get(link,verify=False)
    except Exception as e:
        print('Reason:', e)
        return
    return
    
def send2s(title, content):
    try:
        link = "https://sc.ftqq.com/{0}.send".format(skey)
        d = {'text': title, 'desp': content}
        res = requests.post(link, data=d , verify=False)
    except Exception as e:
        print('Reason:', e)
        return
    return
    
def send2BarkAndWJ(title, content):
    try:
        msg = "{0}/推送标题/{1}/{2}?url=https://wj.qq.com".format(barklink, title, content)
        link = msg
        requests.get(link,verify=False)
        s = "{\"id\":\"123456\",\"survey_type\":0,\"jsonLoadTime\":3,\"time\":1587372438,\"ua\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36\",\"referrer\":\"https://wj.qq.com/mine.html\",\"openid\":\"\",\"pages\":[{\"id\":\"1\",\"questions\":[{\"id\":\"qID\",\"type\":\"text_multiple\",\"blanks\":[{\"id\":\"fID\",\"value\":\"dasdas\"}]}]}],\"latitude\":\"\",\"longitude\":\"\",\"is_update\":false}"
        s = s.replace("123456", wj["ID"])
        s = s.replace("qID", wj["问题ID"])
        s = s.replace("fID", wj["填空ID"])
        s = s.replace("dasdas", title+"  "+content)

        rjson["answer_survey"] = s
        requests.post("https://wj.qq.com/sur/collect_answer", 
                      headers={**base_headers,}, 
                      json=rjson, 
                      verify=False)
    except Exception as e:
        print('Reason:', e)

    return
