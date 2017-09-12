# Под windows
import requests, time, os

# Валюта
currency = "BTC_BCH"
# Цена продажи
need_price = "0.20000000"

# Функция для обращения к API и парса стоимости валюты
def poloniex(currency):
    maid = requests.get("https://poloniex.com/public?command=" + "returnTicker")

    all_currency = maid.json()
    btc_maid = all_currency[currency]
    
    print ("#" * 20)
    print ("Валюта: "+ currency, '\n')
    print ("Текущая стоимость", btc_maid["last"], "btc","\n","Ждем стоимость", need_price, "btc")
    print (" ### Пора продавать ###") if btc_maid["last"]> need_price else print (" Продавать рано")
    return btc_maid["last"]

    

# Приветствие и настройка программы
print ("""Добро пожаловать в пробную версию frend API poloniex!

На данный момент реализованна только функция отслеживания стоимости криптовалюты
по выбранному критерию 'стоимость'.
В следующей версии планируется сделать автоматическую покупку/продажу валюты """, "\n")

print ("Отобразить список всех валют? ")

answer = input("да/нет ")

if answer == "да":
     maid = requests.get("https://poloniex.com/public?command=" + "returnTicker")
     all_currency = maid.json()
     all_currency = all_currency.keys()
     for i in all_currency:
         print (i)
     
currency = input("Валюта для отслеживания? ")
need_price = input("Предупредить о превышении стоимости: (число) ")

# переменная для выявления максимальной стоимости валюты
max_price = 0
count = 0

while 1:
    count += 1
    price = poloniex(currency)
    price = float(price)

    max_price = price if price > max_price else max_price
    print (" Максимальная стоимость:", max_price, "btc", "\n" )
    
    time.sleep(1)
    os.system("cls") if count >= 5 else 0

    if count == 5:
        count = 0
