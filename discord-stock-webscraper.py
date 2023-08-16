import requests
import time
from time import sleep
from bs4 import BeautifulSoup as bs
from discord_webhook import DiscordWebhook, DiscordEmbed



start_time = time.time()


header= {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
url= 'https://de.finance.yahoo.com/quote/LAC/'

r = requests.get(url, headers=header)
soup = bs(r.text, 'html.parser')


price = ""
change = soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[1].text
prev_close = soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)'}).text
open = soup.find('table', {'class':'W(100%)'}).find_all('td')[3].text

content=""
webhook = DiscordWebhook(url='YOUR-WEBHOOK-URL', username="stock-data", content=content)
embed = DiscordEmbed(title=soup.title.text, color=242424, url=url)
embed.set_footer(text="")
embed.set_timestamp()
embed.add_embed_field(name="Current", value=price, inline=False)
embed.add_embed_field(name="Change", value=change, inline=False)
embed.add_embed_field(name="Open", value=open)
embed.add_embed_field(name="Previous Close", value=prev_close)
embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/8/8f/Yahoo%21_Finance_logo_2021.png")

webhook.add_embed(embed)
response = webhook.execute()
sleep(2)

while r.status_code == 200:
    price_new = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    if price_new == price:
        print("No change")
    else:
        print(price_new)
        webhook.delete()
        
        content=""
        webhook = DiscordWebhook(url='YOUR_WEBHOOK_URL', username="stock_data", content=content)
        embed = DiscordEmbed(title="Leo Lithium Limited (LLL.AX)", color=242424, url="https://finance.yahoo.com/quote/LLL.AX/")
        embed.set_footer(text="")
        embed.set_timestamp()
        embed.add_embed_field(name="Current", value=price_new, inline=False)
        embed.add_embed_field(name="Change", value=change, inline=False)
        embed.add_embed_field(name="Open", value=open)
        embed.add_embed_field(name="Previous Close", value=prev_close)
        embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/8/8f/Yahoo%21_Finance_logo_2021.png")
        
        webhook.add_embed(embed)
        response = webhook.execute()
        
        price = price_new
    sleep(30)
else:
    print("Data not available")
    

    

