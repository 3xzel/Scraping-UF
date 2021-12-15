from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.bcentral.cl"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

mo = soup.find_all("p", class_="basic-text fs-1 f-opensans-bold text-center c-blue-nb-7 mb-0")

moneda = list()

count = 0
for i in mo:
    if count < 4:
        moneda.append(i.text)
    else:
        break
    count += 1

va = soup.find_all("p", class_="basic-text fs-2 f-opensans-bold text-center c-blue-nb-2")

valor = list()

count = 0
for i in va:
    if count < 4:
        valor.append(i.text)
    else:
        break
    count += 1

df = pd.DataFrame({'Nombre': moneda, 'Valor': valor}, columns=['Nombre', 'Valor'], index = list(range(1,5)))
print(df)
df.to_csv('Informe.csv', index=False)
