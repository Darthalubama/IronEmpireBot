import discord
import os
import requests
import json

client = discord.Client()

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




client.run(os.getenv('token'))

