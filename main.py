import goslate
import discord
from discord.ext import commands
from googletrans import Translator, constants
import json
import os 
from textblob import TextBlob

def get(element:str):
  path = os.path.abspath("./conf.json")
  with open(path, "r") as read_file:
    content = json.load(read_file)
  return content[element]

intents = discord.Intents().all()
client = commands.Bot(command_prefix=get("prefix"),intents = intents)


"""def translate(text:str,lang = "en"):
    gs = goslate.Goslate()
    translatedText = gs.translate(text,lang)
    return (translatedText)"""# this can also be used but just remember this might get ratelimited


def translate(message,lang="en"):
    translator = Translator()
    translation = translator.translate(message)
    return (translation.text)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print(f"{client.user}: Online")


@client.command()
async def ping(ctx):
  await ctx.send("pong!")
  
@client.event
async def on_message(message,lang = "en"):
  #channel = message.channel
  print("working!")
  print(message.author)
  m = TextBlob(message.content)
  if m.detect_language() == "en":
    return
  if message.author == client.user:
      return
  t=translate(message.content,lang)
  #t=translate(bytes(message.content, encoding="UTF-8"), lang)
  #use the above line instead of line 37 if your going to use the goslate method
  await message.reply(t)

client.run(get("token"))