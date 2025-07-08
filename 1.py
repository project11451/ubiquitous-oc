import requests
from bs4 import BeautifulSoup
import os

def get_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip_info = response.json()
        return ip_info['ip']
    except requests.RequestException as e:
        print(f"Error fetching IP address: {e}")
        return None

url = "http://www.baidu.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
response = requests.get(url, headers=headers)
page_info = response.text
soup = BeautifulSoup(page_info, 'html.parser')
# 建议先打印所有a标签，调试用
print([a for a in soup.find_all('a')])
titles = soup.find_all('a', class_='title')
article_titles = [title.get_text() for title in titles]

output_dir = r"D:\lgz"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "articles.txt"), "w", encoding="utf-8") as file:
    for title in article_titles:
        file.write(title.string + '\n')
        file.write("http：//www.baidu.com"+title.get('href')+'\n\n')
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import http.cookiejar
import urllib.request

url = "http://www.baidu.com"
response1 = urllib.request.urlopen(url)
print("第一种方法")
#获取状态码，200表示成功
print(response1.getcode())
#获取网页内容的长度
print(len(response1.read()))

print("第二种方法")
request = urllib.request.Request(url)
#模拟Mozilla浏览器进行爬虫
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法")
cookie = http.cookiejar.CookieJar()
#加入urllib.request处理cookie的能力
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(len(response3.read()))
print(cookie)