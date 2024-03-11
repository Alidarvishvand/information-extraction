import requests
import json
from bs4 import BeautifulSoup

session = requests.Session()
response = session.get("https://www.farsroid.com/clash-of-clans/")
        
if response.status_code == 200:
    allcomments = []
    for i in range(750, 801):
        data = {"action":"ma_comment_pagination","post_id":12350,"page":i}
        url = "https://www.farsroid.com/wp-admin/admin-ajax.php"
        api_response = session.post(url, data=data)
        if api_response.status_code == 200:
            print("Success")
            html = api_response.json()["html"]
            html_parsed = BeautifulSoup(html)
            all_li = html_parsed.body.find_all("li")
            for li in all_li:
                try:
                    comment = {}
                    comment["author"] = li.find("span", {"class": "author"}).text
                    comment["date"] = li.find("span", {"class": "date"}).text
                    comment["model"] = li.find("span", {"class": "model"}).text
                    comment["android"] = li.find("span", {"class": "android"}).text
                    comment["comment"] = li.find("div", {"class": "comment-body-text"}).text
                    allcomments.append(comment)
                except AttributeError:
                    pass
    # print(json.dumps(allcomments, ensure_ascii=False))
    print("*****done******")
    with open('E:\data.json', 'w', encoding='utf8') as f:
        json.dump(allcomments, f, indent=4, ensure_ascii=False)

