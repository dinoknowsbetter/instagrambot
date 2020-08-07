import requests
import time
import json
from dhooks import Webhook, Embed


oldurl = '1'
newurl = '2'
caption = ''
thumbnail = ''
hook = Webhook(' PUT YOUR WEBHOOK URL HERE ')    

while True:
    response = requests.get('https://apis.duncte123.me/insta/dinoknowsbetter') #update your username here
    response.raise_for_status()
    jsonResponse = response.json()
    print("last post results in...")
    newurl = jsonResponse["images"][0]["page_url"]
    caption = jsonResponse["images"][0]["caption"]
    thumbnail = jsonResponse["images"][0]["url"]
    profilepic = jsonResponse["user"]["profile_pic_url"]
    print(newurl)
    if newurl != oldurl:
        oldurl = newurl
        print('Pushing a notification to discord for the new IG post: ' + newurl)
        embed = Embed(
            description='**DinoKnowsBetter** just posted on _instagram_ :eyes:',
            color=0x5CDBF0,
            timestamp='now'  # sets the timestamp to current time
        )
        embed.set_author(name='DKB InstagramBot', icon_url=profilepic)
        embed.add_field(name='Caption', value=caption)
        embed.set_footer(text='Like and comment, because why not? Beep boop.', icon_url=profilepic)

        embed.set_thumbnail(profilepic)
        embed.set_image(thumbnail)
        hook.send(username = 'DKB InstaBot', embed=embed)
    else:
        #this is a console message, you can turn it off
        print('Nothing new')
        print(newurl + ' new')
        print(oldurl + ' old')
        print()
        print()
        print('sleeping for 5mins')
    time.sleep(300)