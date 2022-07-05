#importing all the required libraries 
import bs4
import urllib3
import smtplib
import time

prices_list = []

def check_price():
    url = 'https://www.amazon.in/Boat-BassHeads-900-Wired-Headphone/dp/B074ZF7PVZ/ref=sr_1_1_sspa?crid=318UWGHIA2C7Q&keywords=headphones&qid=1656511713&sprefix=head%2Caps%2C440&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTldCOTVZU043SVBUJmVuY3J5cHRlZElkPUEwODg2MjQwMkpBRUtTM0M2N1NXVyZlbmNyeXB0ZWRBZElkPUEwMDExNDI2M0lHUTJUSkI5WUoyUyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1'

    sauce=urllib3.PoolManager().request('GET',url)
    soup = bs4.BeautifulSoup(sauce.data, "html.parser")

    prices = soup.find(id="color_name_0_price").get_text()
    # print(prices)
    prices = float(prices.replace(",", "").replace("₹", ""))
    prices_list.append(prices)
    return prices



def send_email(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("projectworkcdc2022@gmail.com","vrdsytkutganifca")
    s.sendmail("projectworkcdc2022@gmail.com", "muskanap298@gmail.com", message)
    s.quit()



def price_decrease_check(price_list):
    if prices_list[-1] < prices_list[-2]:
        return True
    else:
        return False

 

count = 1
while True:
    current_price = check_price()
    if count > 1:
        flag = price_decrease_check(prices_list)
        if flag:
            decrease = prices_list[-2] - prices_list[-1]
            message = f"The price has decrease please check the item. The price decrease by {decrease} rupees and the new price is {current_price}."
            send_email(message)
            time.sleep(43000)
    count += 1