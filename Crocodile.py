import discord;
from discord.ext.commands import Bot;
import time
from discord.ext import commands;
from collections import deque
import random

# Instantiate bot
Client = discord.Client()
client = commands.Bot(command_prefix="!kkb");
four = deque();
fourHalf = deque();
five = deque();
fiveHalf = deque();
six = deque();
sixHalf = deque();
seven = deque();
sevenHalf = deque();
eight = deque();
eightHalf = deque();
nine = deque();
nineHalf = deque();
ten = deque();
tenHalf = deque();
eleven = deque();
elevenHalf = deque();
twelve = deque();
twelveHalf = deque();
thirteen = deque();
thirteenHalf = deque();
fourteen = deque();
fourteenHalf = deque();
fifteen = deque();
fifteenHalf = deque();
sixteen = deque();
sixteenHalf = deque();

sizes = {
    "4": {},
    "4.5": {},
    "5": {},
    "5.5": {},
    "6": {},
    "6.5": {},
    "7": {},
    "7.5": {},
    "8": {},
    "8.5": {},
    "9": {},
    "9.5": {},
    "10": {},
    "10.5": {},
    "11": {},
    "11.5": {},
    "12": {},
    "12.5": {},
    "13": {},

}


# The few methods below take information from the embedded message that the adisplash sends
async def get_size(message):
    for embeds in message.embeds:
        ""
    return (embeds["fields"][1]["value"][:4].rstrip());


async def get_image(message):
    for embeds in message.embeds:
        ""
    return (embeds["thumbnail"]["url"]);


async def get_url(message):
    for embeds in message.embeds:
        ""
    return embeds["fields"][3]["value"][12:][:-1]


async def get_username(message):
    for embeds in message.embeds:
        ""
    return embeds["fields"][2]["value"]


async def get_id(message):
    for embeds in message.embeds:
        ""
        # print(embeds["fields"][2]["value"])
    return embeds["fields"][0]["value"]


async def get_logs_from(channel):
    async for m in client.logs_from(channel, limit=1):
        print(m.embeds[0]["fields"][0]["value"]);
    # This is printed when the bot starts running


@client.event
async def on_ready():
    print("Waking up is the hardest part but then its essential")


#  await get_logs_from(client.get_server("451505157549588513").get_channel("539194010309230602"));
"!getcart "


# This code runs when a message is sent to a channel that the bot is in
@client.event
async def on_message(message):
    if (message.channel.is_private):
        if (message.content[0:8] == "!getcart"):
            size = message.content[9:]
            if (size == ""):
                size = random.randint(9, 33)
                print(size / 2);
                size = (size / 2).__str__();

            print(size);
            if (size == "4" or size == "4.0"):
                if (len(four) < 1):
                    await client.send_message(message.author, "No carts available in size 4! Please try again later.")
                else:
                    await client.send_message(message.author, embed=four.popleft())
            if (size == "4.5"):
                if (len(fourHalf) < 1):
                    await client.send_message(message.author, "No carts available in size 4.5! Please try again later.")
                else:
                    await  client.send_message(message.author, embed=fourHalf.popleft())
            if (size == "5" or size == "5.0"):
                if (len(five) < 1):
                    print("TRE")
                    await client.send_message(message.author, "No carts available in size 5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=five.popleft())
            if (size == "5.5"):
                if (len(fiveHalf) < 1):
                    await client.send_message(message.author, "No carts available in size 5.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=fiveHalf.popleft())
            if (size == "6" or size == "6.0"):
                if (len(six) < 1):
                    await client.send_message(message.author, "No carts available in size 6! Please try again later.")
                else:
                    await client.send_message(message.author, embed=six.popleft())
            if (size == "6.5"):
                if (len(sixHalf) < 1):
                    await client.send_message(message.author, "No carts available in size 6.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=sixHalf.popleft())
            if (size == "7" or size == "7.0"):
                if (len(seven) < 1):
                    await client.send_message(message.author, "No carts available in size 7! Please try again later.")
                else:
                    await client.send_message(message.author, embed=seven.popleft())
            if (size == "7.5"):
                if (len(sevenHalf) < 1):
                    await client.send_message(message.author, "No carts available in size 7.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=sevenHalf.popleft())
            if (size == "8" or size == "8.0"):
                if (len(eight) < 1):
                    await  client.send_message(message.author, "No carts available in size 8! Please try again later.")
                else:
                    await client.send_message(message.author, embed=eight.popleft())
            if (size == "8.5"):
                if (len(eightHalf) < 1):
                    await client.send_message(message.author, "No carts available in size 8.5! Please try again later.")
                else:
                    await  client.send_message(message.author, embed=eightHalf.popleft())
            if (size == "9" or size == "9.0"):
                if (len(nine) < 1):
                    await  client.send_message(message.author, "No carts available in size 9! Please try again later.")
                else:
                    await client.send_message(message.author, embed=nine.popleft())
            if (size == "9.5"):
                if (len(nineHalf) < 1):
                    await client.send_message(message.author, "No carts available in size 9.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=nineHalf.popleft())
            if (size == "10" or size == "10.0"):
                if (len(ten) < 1):
                    await client.send_message(message.author, "No carts available in size 10! Please try again later.")
                else:
                    await client.send_message(message.author, embed=ten.popleft())
            if (size == "10.5"):
                if (len(tenHalf) < 1):
                    await client.send_message(message.author,
                                              "No carts available in size 10.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=tenHalf.popleft())
            if (size == "11" or size == "11.0"):
                if (len(eleven) < 1):
                    await  client.send_message(message.author, "No carts available in size 11! Please try again later.")
                else:
                    await client.send_message(message.author, embed=eleven.popleft())
            if (size == "11.5"):
                if (len(elevenHalf) < 1):
                    await client.send_message(message.author,
                                              "No carts available in size 11.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=elevenHalf.popleft())
            if (size == "12" or size == "12.0"):
                if (len(twelve) < 1):
                    await  client.send_message(message.author, "No carts available in size 12! Please try again later.")
                else:
                    await client.send_message(message.author, embed=twelve.popleft())
            if (size == "12.5"):
                if (len(twelveHalf) < 1):
                    await client.send_message(message.author,
                                              "No carts available in size 12.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=twelveHalf.popleft())
            if (size == "13" or size == "13.0"):
                if (len(twelveHalf) < 1):
                    await client.send_message(message.author, "No carts available in size 13! Please try again later.")
                else:
                    await client.send_message(message.author, embed=thirteen.popleft())
            if (size == "13.5"):
                if (len(twelveHalf) < 1):
                    await client.send_message(message.author,
                                              "No carts available in size 13.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=thirteenHalf.popleft())
            if (size == "14" or size == "14.0"):
                if (len(twelveHalf) < 1):
                    await client.send_message(message.author, "No carts available in size 14! Please try again later.")
                else:
                    await client.send_message(message.author, embed=fourteen.popleft())
            if (size == "14.5"):
                if (len(twelveHalf) < 1):
                    await client.send_message(message.author,
                                              "No carts available in size 14.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=fourteenHalf.popleft())
            if (size == "15" or size == "15.0"):
                if (len(twelveHalf) < 1):
                    await client.send_message(message.author, "No carts available in size 15! Please try again later.")
                else:
                    await client.send_message(message.author, embed=fifteen.popleft())
            if (size == "15.5"):
                if (len(twelveHalf) < 1):
                    await client.send_message(message.author,
                                              "No carts available in size 15.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=fifteenHalf.popleft())
            if (size == "16" or size == "16.0"):
                if (len(twelveHalf) < 1):
                    await client.send_message(message.author, "No carts available in size 16! Please try again later.")
                else:
                    await client.send_message(message.author, embed=sixteen.popleft())
            if (size == "16.5"):
                if (len(twelveHalf) < 1):
                    await client.send_message(message.author,
                                              "No carts available in size 16.5! Please try again later.")
                else:
                    await client.send_message(message.author, embed=sixteenHalf.popleft())
    # Checking if the message is coming from #carts, otherwise the bot would copy paste information from any channel. This is why we don't speak in carts.
    if message.channel.id == "578764085865480194":
        # I have to use await here because this involves web requests, otherwise it will crash.
        try:

            url = await get_url(message);
            size = await get_size(message);
            image = await get_image(message);
            username = await get_username(message)
            id = await get_id(message);
            # This is an embed message, its what most bots use to display information in an organized way.-
            embed = discord.Embed(title="Adidas Cart (CLICK HERE) Size: " + size + "", url=url, color=0x9c6bf5)
            embed.set_thumbnail(url=image);
            embed.add_field(name="Account Details", value=username, inline=True)
            print("SIZE " + size);
            print(url)
            # print(image);
            print(username);
            size = size.replace("U", "");
            size = size.replace("S", "");
            size = size.replace("US", "");
            size = size.replace("K", "");
            size = size.replace("C", "");


            size = size.strip();
            print("SIZE: " + size);
            await client.send_message(client.get_server("531267925534048306").get_member_named("PenguinMaster926#0926"),embed=embed)

            # Size filtering here. Checks if something is a certain size and sends to the corresponding text channel
            if (size == "4"):
                four.append(embed)
            # four.append(embed)
            if (size == "4.5"):
                fourHalf.append(embed)
                # fourHalf.append(embed)
            if (size == "5"):
                # await client.send_message(client.get_server("451505157549588513").get_member_named("Schlop#1111"),embed=embed)
                five.append(embed)
            if (size == "5.5"):
                # await client.send_message(client.get_server("451505157549588513").get_member_named("Schlop#1111"),embed=embed)
                fiveHalf.append(embed)
            if (size == "6"):
                # await client.send_message(client.get_server("451505157549588513").get_member_named("Ratatoilet#0001"),embed=embed)
                six.append(embed)
            if (size == "6.5"):
                # await client.send_message(client.get_server("552219609332449287").get_member_named("Alpha#9999"),embed=embed)
                sixHalf.append(embed)
            if (size == "7"):
                # await client.send_message(client.get_server("451505157549588513").get_member_named("Ratatoilet#0001"),embed=embed)
                seven.append(embed)
            if (size == "7.5"):
                # await client.send_message(client.get_server("451505157549588513").get_member_named("Ratatoilet#0001"),embed=embed)
                sevenHalf.append(embed)
            if (size == "8"):
                # await client.send_message(client.get_server("552219609332449287").get_member_named("Rindler#0420"),embed=embed)
                eight.append(embed)
            if (size == "8.5"):
                # await client.send_message(client.get_server("552219609332449287").get_member_named("Alpha#9999"),embed=embed)
                eightHalf.append(embed)
            if (size == "9"):
                # await client.send_message(client.get_server("552219609332449287").get_member_named("Alpha#9999"),embed=embed)
                nine.append(embed)
            if (size == "9.5"):
                # await client.send_message(client.get_server("552219609332449287").get_member_named("Alpha#9999"),embed=embed)
                nineHalf.append(embed)
            if (size == "10"):
                # await client.send_message(client.get_server("552219609332449287").get_member_named("Alpha#9999"),embed=embed)
                ten.append(embed)
            if (size == "10.5"):
                # await client.send_message(client.get_server("451505157549588513").get_member_named("PenguinMaster926#0926"),embed=embed)
                tenHalf.append(embed)
            if (size == "11"):
                # await client.send_message(client.get_server("451505157549588513").get_member_named("PenguinMaster926#0926"),embed=embed)
                eleven.append(embed)
            if (size == "11.5"):
                # await client.send_message(client.get_server("451505157549588513").get_member_named("PenguinMaster926#0926"),embed=embed)
                elevenHalf.append(embed)
            if (size == "12"):
                # await client.send_message(client.get_server("451505157549588513").get_member_named("PenguinMaster926#0926"),embed=embed)
                twelve.append(embed)
            if (size == "12.5"):
                # await client.send_message(client.get_server("552219609332449287").get_member_named("Alpha#9999"),embed=embed)
                twelveHalf.append(embed)
            if (size == "13"):
                thirteen.append(embed)
            if (size == "13.5"):
                thirteenHalf.append(embed);
            if (size == "14"):
                fourteen.append(embed)
            if (size == "14.5"):
                fourteenHalf.append(embed)
            if (size == "15"):
                fifteen.append(embed)
            if (size == "15.5"):
                fifteenHalf.append(embed)
            if (size == "16"):
                sixteen.append(embed)
            if (size == "16.5"):
                sixteenHalf.append(embed)



        except Exception as e:
            print(e);
            print("L");

    # await client.send_message(message.channel,"Check dms :)")
    # await client.send_message(message.channel, "you are right my friend")


# Runs the bot
client.run("");
