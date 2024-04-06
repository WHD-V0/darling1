from lxml import etree
import requests
# 发送的地址
url = 'https://nba.hupu.com/stats/players'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}

# 发送请求
resp = requests.get(url,headers = headers)

# 处理结果
e = etree.HTML(resp.text)

# 解析响应的数据
nus = e.xpath('//table[@class="players_table"]//tr/td[1]/text()')
names = e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
teams = e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
fts = e.xpath('//table[@class="players_table"]//tr/td[4]/text()')

with open('nba.txt','w',encoding='utf-8') as f :
# 是否保存
    for nu,name,team,ft in zip(nus,names,teams,fts):
        f.write(f'排名：{nu}  姓名：{name}  球队：{team}  罚球：{ft}\n')