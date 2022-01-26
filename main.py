import discord
import os
import requests
import json

client = discord.Client()

application = ["Application:"]
appResponse = "**if you need help joining the clan ingame, please contact a staff member.**"

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
 print("we have logged in as {0.user}"
 .format(client))

@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return
  

  elif message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  elif message.content.startswith('$rules'):
    f = open("rules.txt","r")
    rules = f.read()

    await message.channel.send(rules)
 
  elif message.content.startswith('$ranks'):
    f = open("ranks.txt","r")
    ranks = f.read()

    await message.channel.send(ranks)
  
  elif message.content.startswith('$drinkie'):
    ranks = "***Hydration and Posture check!***"
    
    await message.channel.send(ranks)

  elif any(word in msg for word in application):
    await message.channel.send(appResponse)


client.run(os.getenv('token'))


from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
  return "Bot up and running"
if __name__ == '__main__':
  app.run(host="0.0.0.0",debug=True,port=8080)
