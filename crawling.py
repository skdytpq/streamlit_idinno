import requests
import pip
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image
import pandas as pd
import re


def url(cat,value):
    review_num = []
    review = []
    url_list = []
    img_list = []
    page = 1
    if cat == '무신사':
        while page < value:

            url = f'https://www.musinsa.com/search/musinsa/goods?q=%EC%8B%A0%EB%B0%9C&list_kind=small&sortCode=pop&sub_sort=&page={page}&display_cnt=0&saleGoods=&includeSoldOut=&setupGoods=&popular=&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&campaignId=&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&groupSale=&d_cat_cd=&attribute=&plusDeliveryYn'
            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
            response = requests.get(url, headers=headers)

            try:
                if response.status_code == 200:
                    html = response.text
                    soup = BeautifulSoup(response.text, 'html.parser')
                    for i in range(len(url)):
                        review_num_soup = soup.select('li > div.li_inner > div.article_info > p.point > span.count')[i].get_text()
                        review_num.append(review_num_soup)

                        review_soup = soup.select('li > div.li_inner > div.article_info > p.point > span.img-score > span')[i]['style'].split()[0]
                        review_soup = re.sub(r'[^0-9]', '', review_soup)
                        review.append(review_soup)
                        
                        url = soup.select('li > div.li_inner > div.list_img > a')[i]['href']
                        url_list.append(url)
                        
                        img_src = 'http:' + soup.select('li > div.li_inner > div.list_img > a > img')[i]['data-original']
                        urllib.request.urlretrieve(img_src, f"imagedir/page{page}_shoe{i}.jpg")
                        img_list.append(img_src)
                        
                        
                        
                                
            except:
                #info = {'리뷰 개수' : review_num , '리뷰 점수' : review, '상품 링크' : url_list}
                #c = pd.DataFrame(data = info)
                #c.to_csv('imagedir/image_info.csv')
                False
            page += 1
        return img_list
