import discord
import os

tables = 0
client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


@client.event
async def on_message(message):
    global tables
    if ':reactron' in message.content.lower():
        emojiList = {}
        for emoji in client.emojis:
            emojiList[emoji.name] = emoji
        try:
            nums = [int(s) for s in message.content.split() if s.isdigit()]
            content = message.content.split("-")
            content = content[1:]
            n = nums[0]
            n += 1
            message2 = message
            async for message in message2.channel.history(limit=n):
                pass
            for item in content:
                if item.strip() in emojiList:
                    await message.add_reaction(emojiList[item.strip()])
            if "poll" in message2.content.lower():
                await message.add_reaction(":yes:542028150293397515")
                await message.add_reaction(":no:542028177703305216")
        except Exception as e:
            print(str(e))
    if ':dirtypost' in message.content.lower():
        try:
            nums = [int(s) for s in message.content.split() if s.isdigit()]
            n = nums[0]
            n += 1
            message2 = message
            async for message in message2.channel.history(limit=n):
                pass
            await message.add_reaction(":nutting_pikachu:542036920285396993")
            await message.add_reaction(
                "a:pulsating_dickplant:567327025837113371")
            await message.add_reaction(":ectoplasm:542016362730618900")
            await message.add_reaction(":dickplant:541995248344104971")
            await message.add_reaction(":japanese_porno:547049871471935528")
            await message.add_reaction(":ahegao:568917738169434119")
        except Exception as e:
            print(str(e))
    if ':help' in message.content.lower():
        await message.author.send(
            "To use reactron all you have to do is count the number of messages between the message you want to react on and the most recent message. Then you will use the command :reacton with the number of messages between the message you want to react on and the current message and a hyphen separated list of reactions. So if you want to react with the yes reaction on the 5th message up you would use :reactron 5 -yes. \n\n:reactron *reaction_name* #.\n\nReactron can work across channels as well if it is in them. Additionally reactron can use :dirtypost # to react with a predefined set of dirtier reactions.\n\n"
        )
        emoList = []
        for emoji in client.emojis:
            emoList.append(str(emoji) + " " + emoji.name + "\n")
        while 0 < len(emoList):
            if len(emoList) >= 10:
                await message.author.send(emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop())
            if len(emoList) == 9:
                await message.author.send(
                    emoList.pop() + emoList.pop() + emoList.pop() +
                    emoList.pop() + emoList.pop() + emoList.pop() +
                    emoList.pop() + emoList.pop() + emoList.pop())
            if len(emoList) == 8:
                await message.author.send(emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop())
            if len(emoList) == 7:
                await message.author.send(emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop() +
                                          emoList.pop())
            if len(emoList) == 6:
                await message.author.send(emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop())
            if len(emoList) == 5:
                await message.author.send(emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop() +
                                          emoList.pop())
            if len(emoList) == 4:
                await message.author.send(emoList.pop() + emoList.pop() +
                                          emoList.pop() + emoList.pop())
            if len(emoList) == 3:
                await message.author.send(emoList.pop() + emoList.pop() +
                                          emoList.pop())
            if len(emoList) == 2:
                await message.author.send(emoList.pop() + emoList.pop())
            if len(emoList) == 1:
                await message.author.send(emoList.pop())

token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)
