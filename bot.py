import discord
import os
import requests
import json
import random 

def get_meme():
  response = requests.get("https://meme-api.com/gimme")
  json_data = json.loads(response.text)
  return json_data['url']

def get_quotes():
  response = requests.get("https://zenquotes.io/api/quotes/")
  json_data = json.loads(response.text)
  return random.choice(json_data)['q']




class  MyClient(discord.Client):
  async def on_ready(self):
    print("Logged on as {0}!".format(self.user))

  async def on_message(self, message): 
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme() )
    if message.content.startswith("$quote"):
      await message.channel.send(get_quotes())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("discord_bot_token"))


