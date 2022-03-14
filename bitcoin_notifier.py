import requests
import time
from plyer import notification
import datetime


bitcoin_rate = None

now = datetime.datetime.now()
now = now.strftime("%d/%m %H:%M")

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

while True:
    try:
        response = requests.get(URL,
          headers={"Accept": "application/json"},
        )
        data = response.json()
        bpi = data['bpi']
        USD = bpi['USD']
        bitcoin_rate = int(USD['rate_float'])

        print("[+] We are live [+]")

    except:
        print('Something is wrong, Do you have Internet!')


    notification.notify(
            #title of the notification,
            title = f"Bitcoin Price Alert!! {now}",

            #the body of the notification
            message = f"Current Bitcoin Price is {bitcoin_rate}",

            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = "bitcoin.ico",

            # the notification stays for 60 seconds
            timeout  = 60
        )

        #notification repeats after every 5 Minutes
    time.sleep(30)
