from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def Root():
  return """
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title></title>
	<meta charset="utf-8" />
</head>
<body onload="window.location.href ='docs';">
</body>
<html>
"""

@app.get("/api/ScrapyMonotaro")
async def ScrapyMonotaro(target_url: str = None):
  try:
    # 引数なしの場合に固定ページをリクエスト
    if target_url:
        scrapy_url = target_url
    else:
        scrapy_url = "https://www.monotaro.com/p/3710/2536/"
    
    # 項目値を取得するためのXPATH指定
    items={
            '品名' : 'normalize-space(//h1[@class="ProductName u-FontSize--Xlg"]//span/text())',
            '注文コード' : 'normalize-space(//span[contains(text(), "注文コード")]/parent::span/text())',
            '注文コード２' : 'normalize-space(//span[contains(text(), "注文コード")]/following-sibling::span/text())',
            '品番' : 'normalize-space(//span[contains(text(), "品番")]/parent::span/text())',
            '品番２' : 'normalize-space(//span[contains(text(), "品番")]/following-sibling::span/text())',
            '販売価格(税別)' : 'normalize-space(//span[@class="Price Price--Lg"]/text())'
    }
    
    # スクレーピング処理
    itemData = req.getItemData(scrapy_url, items)
    
    # 取得データ編集
    if len(itemData['注文コード']) == 0:
       itemData['注文コード'] = itemData['注文コード２']
    if len(itemData['品番']) == 0:
       itemData['品番'] = itemData['品番２']

    # 取得データ返却   
    response = {'status': 200, 'data' : {'url' :scrapy_url, 'items' : itemData}}
    return response
  
  except Exception as e:
    # 例外発生時に例外情報返却
    response = {'status': 500, 'data' : {'error.type' : type(e), 'error.args' : e.args, 'error.message' : e}}
    print(response)
    return response
  
@app.delete("/api/ScrapyMonotaro")
async def ScrapyMonotaroReset():
  req.page_cashe = {}
  response = {'status': 200, 'data' : {'msg' : 'キャッシュデータクリア'}}
  return response


# スクレーピングエンジン
from lxml import html
import requests
import time

class ScrapyHtmlRequest():
    REQEST_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    INTERVAL_TIME=3  # リスクエス間隔は3秒に仮置き
    last_processed_time = 0
    page_cashe = {}
    page_cashe_switch = True

    def __init__(self, interval_time=3, page_cashe_switch=True):
        self.INTERVAL_TIME = interval_time
        self.last_processed_time = 0
        self.page_cashe = {}
        self.page_cashe_switch = page_cashe_switch

    def requestHtml(self, target_url):
        if target_url in self.page_cashe:
            page = self.page_cashe[target_url]
            print('url:[{}] キャッシュリターン'.format(page.url))

        else:
            # 前回の処理時間からの経過時間
            elapsed_time = time.time() - self.last_processed_time
            # 経過時間がリクエスト間隔よりも短い場合にリクエストを待ち合わせる
            if elapsed_time < self.INTERVAL_TIME:
                print('リクエスト待機時間：{:.3f}'.format(self.INTERVAL_TIME - elapsed_time))
                time.sleep(self.INTERVAL_TIME - elapsed_time)
            
            page=requests.get(target_url, headers=self.REQEST_HEADERS)
            print(page.encoding)
            page.encoding = page.apparent_encoding
            print(page.encoding)

            self.last_processed_time = time.time()
            print('url:[{}] [{} {}] [{}]'.format(page.url, page.status_code, page.reason, page.elapsed))
            
            if self.page_cashe_switch:
                self.page_cashe[target_url]=page

        html_parser = html.HTMLParser(encoding=page.encoding)
        return html.fromstring(page.content, parser=html_parser)
    
    def getItemData(self, url, items):
        response=self.requestHtml(url)
        item_data={}
        for key in items.keys():
            if len(items[key]) > 0:
                try:
                    item_data[key]=response.xpath(items[key])
                except Exception as e:
                    print(e)
                    item_data[key]=''
        return item_data
        
req=ScrapyHtmlRequest()
