import discord
import asyncio
import config as cfg
from time import sleep
import random

# TODO: github
# TODO: check if sean is in voice chat and spam him
# TODO: move sean randomly on a timer into another voice channel :)))))
# TODO: RENAME BOT TO "annihilate sean"
# TODO: sleep

client = discord.Client()


# When bot turns on
@client.event
async def on_ready():
    print("The bot is ready!")
    statusList = cfg.settings['statusList']
    everyoneList = cfg.settings['everyoneList']
    # Function to 1, shuffle the statusList array, and second, change the status every X number of seconds
    async def statusShuffle():
        # Shuffle array
        random.shuffle(cfg.settings['statusList'])
        # for loop for changing the status
        for index in range(len(statusList)):
            await client.change_presence(game=discord.Game(name=statusList[index]))
            await asyncio.sleep(300) # how often to change the status, should be something around 300 seconds (5 mintues)
            if index == range(len(statusList)):# vvvvvvvvvvvvvvvvvvvvv
                statusShuffle() #recall the function at the end of the loop
    await statusShuffle()
# Status changing

@client.event
# On Message
async def on_message(message):
    if message.author == client.user:
        return
    #hello command
    if message.content == "hello":
        await client.send_message(message.channel, "Fuck off loser")

    #merica shooting schools fuck yeah
    if message.content == "USA":
        await client.send_message(message.channel, "!p pumped up kicks")

    #Sean hello command
    if message.author.id == "161263363685482496" and message.content == "hello":
        await client.send_message(message.channel, "shut up sean, your gay and dumb")
    #elif message.content == "hello":
    #    await client.send_message(message.channel, "Goodbye")
    # snapchat command
    if message.content == "snapchat":
        await client.send_message(message.channel, "hi im kayeanna add me on snap kayekayelovlizi")
    # send the fucking nuke on the dumbass who mentioned everyon
    if message.content ==  "@everyone":
        random.shuffle(everyoneList)
        for index in range(everyoneList):
            await client.send_message(message.channel, "<@"+str(message.author.id)+"> " + everyoneList[index])
            sleep(1.5)
    # is sean gay command
    if message.content == "is sean gay?":
        await client.send_message(message.channel, "``` Exhibit A: \n Sean talked to a Swedish pedophile on multiple occasions and became his friend willingly. \n \n Exhibit B: \n Sean took \"bribes\" and \"offers\" from said Swedish pedophile:\n    - Multiple Games \n    - Several electronic Steam gift cards of various values \n    - Bought Counter Strike: Global Offensive skins \n    - Many undisclosed unknown gifts \n \n Exhibit C: \n \n Sean took pictures of his penis and sent the to the Swedish man in exchange for the \"offers\" as disclosed in Exhibit B. \n \n [In conclusion] \n This is undeniable proof, that sean is indeed a fucking faggot. If he is still not a faggot after this, he is still more of a faggot than Damon. ```")


# token stored in config.py
client.run(cfg.settings['token'])
