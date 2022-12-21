import re

from lxml import etree


import requests

urls = [# 越江时代
        "https://www.njhouse.com.cn/spf/detail?prjid=2986150",
        # 华发四季
        "https://www.njhouse.com.cn/spf/detail?prjid=3189150",
        # 颐和四季府
        "https://www.njhouse.com.cn/spf/detail?prjid=3339250",
        # 颐和铂岸江景
        "https://www.njhouse.com.cn/spf/detail?prjid=2803150"
        ]

ans = ""
for i, url in enumerate(urls):
  payload={}
  headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en,zh;q=0.9,zh-CN;q=0.8,en-US;q=0.7',
    'Cookie': 'PHPSESSID=d094529eba1128822580ebccba346417; PHPSESSID_NS_Sig=oenCV6ibzT4puVS9; Hm_lvt_74660749e276ec1c82174d6ac415c6fb=1670892769; Hm_lpvt_74660749e276ec1c82174d6ac415c6fb=1670941081'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)
  # dom = etree.HTML(response.text)
  pattern = '<td width="236"> (.*?)套'
  rengou = re.search(pattern, response.text).group(1)
  print(rengou)
  pattern = '<td> (.*?)套</td>'
  chengjiao = re.search(pattern, response.text).group(1)
  print(chengjiao)
  if i == 0:
    ans += "【越江时代】今日认购{}，今日成交{};".format(rengou, chengjiao)
  elif i == 1:
    ans += "【华发四季雅筑】今日认购{}，今日成交{};".format(rengou, chengjiao)
  elif i == 2:
    ans += "【颐和四季府】今日认购{}，今日成交{};".format(rengou, chengjiao)
  elif i == 3:
    ans += "【颐和铂岸江景】今日认购{}，今日成交{};".format(rengou, chengjiao)


url = "https://sctapi.ftqq.com/SCT187578TzNBx8qc2wcyOowLpyuNTKy2I.send?title=\"{}\"&desp={}, {}".format(ans, ans, '\n'.join(urls))
print(url)
payload={}
headers = {}

# response = requests.request("POST", url, headers=headers, data=payload)
