from bs4 import BeautifulSoup
import requests

web = input("Выберете сайт(ссылка): ")
elem = input("Выберете элемент: ")
class1 = input("Выберете класс: ")

req = requests.get(web)
print(req.status_code)

file = open("news.txt", "w" , encoding='utf-8')

soup = BeautifulSoup(req.text , "html.parser")
news = soup.findAll(elem, class_=class1)
img = soup.findAll("img")
for i in news:
    file.write(i.text +"\n")
    print(i.text)
'''for i in img:
    try:
       print(img["src"])
    except:
        print("Эта картинка без src")'''