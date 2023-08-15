import requests
import time
from time import sleep
from bs4 import BeautifulSoup as bs
from discord_webhook import DiscordWebhook, DiscordEmbed



start_time = time.time()


header= {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
url= 'https://finance.yahoo.com/quote/LLL.AX/'

r = requests.get(url, headers=header)
soup = bs(r.text, 'html.parser')


price = ""

content=""
webhook = DiscordWebhook(url='YOUR-WEBHOOK-URL', username="ASX:LLL", content=content)
embed = DiscordEmbed(title="Leo Lithium Limited (LLL.AX)", color=242424, url="https://finance.yahoo.com/quote/LLL.AX/")
embed.set_footer(text="")
embed.set_timestamp()
embed.add_embed_field(name="Current", value=price, inline=False)
embed.add_embed_field(name="Change", value="0.0000", inline=False)
embed.add_embed_field(name="Open", value="1.1400")
embed.add_embed_field(name="Previous Close", value="1.1400")
embed.set_image(url="https://leolithium.com/wp-content/uploads/LeoLithiumRegisteredLogoRetina.png")

webhook.add_embed(embed)
response = webhook.execute()
sleep(5)

while r.status_code == 200:
    price_new = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    if price_new == price:
        print("No change")
    else:
        print(price_new)
        webhook.delete()
        
        content=""
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1141104818732159016/nY4Ky4CvhLUCKjGPpHnxsXbaIQ_a2l5TOwhvrmJzx0op5AgSnHs5NYXN_abttqulljoz', username="ASX:LLL", content=content)
        embed = DiscordEmbed(title="Leo Lithium Limited (LLL.AX)", color=242424, url="https://finance.yahoo.com/quote/LLL.AX/")
        embed.set_footer(text="")
        embed.set_timestamp()
        embed.add_embed_field(name="Current", value=price_new, inline=False)
        embed.add_embed_field(name="Change", value="0.0000", inline=False)
        embed.add_embed_field(name="Open", value="1.1400")
        embed.add_embed_field(name="Previous Close", value="1.1400")
        embed.set_image(url="https://leolithium.com/wp-content/uploads/LeoLithiumRegisteredLogoRetina.png")
        
        webhook.add_embed(embed)
        response = webhook.execute()
        
        price = price_new
    sleep(30)
else:
    print("Site not available")
    

    

