import discord
import YouTube
import APIKey

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$get'):
        YouTube.main()
        await message.channel.send(file=discord.File("img.png"))


async def on_member_join(member):
    channel = member.guild.get_channel(754755358316298260)
    count = member.guild.member_count
    await channel.edit(name='Member count : ' + str(count))


async def on_member_remove(member):
    channel = member.guild.get_channel(754755358316298260)
    count = member.guild.member_count
    await channel.edit(name='Member count : ' + str(count))


client.run(APIKey.discord_apikey())
