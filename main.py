from bs4 import BeautifulSoup
import requests
import json
data_final = []

for page in range(1,5):
    url = f"https://parsinger.ru/html/index4_page_{page}.html"
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    for card in soup.find_all('div', class_="item"):
        name = card.find('a', class_="name_item").text.strip()
        description = [x.text.split(":")[1].strip() for x in card.find('div',class_='description').find_all('li')]
        price = card.find('p', class_="price").text.strip()
        data = {'Наименование': name,
                'Бренд': description[0],
                'Форм-фактор': description[1],
                'Ёмкость': description[2],
                'Объем буферной памяти': description[3],
                'Цена': price}
        data_final.append(data)
print(data_final)
print(len(data_final))

with open("file.json", 'w', encoding='utf-8') as file:
    json.dump(data_final, file, indent =4, ensure_ascii=False)
