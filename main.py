import discord
import asyncio
import os
#client object for the bot
client = discord.Client()

#Read the password from the file
def readPassFromFile():
	print("Looking for password file...")
	for root, dirs, files in os.walk("noncommits"):
		if 'LocalPass.txt' in files:
			pathtoPassword = os.path.join('noncommits', 'LocalPass.txt')
			f = open(pathtoPassword, 'r')
			return f.readline()
		else:
			print("Password file not found in 'noncommits/LocalPass.txt'")
			print("make sure you have a 'LocalPass.txt' file in your")
			print("noncommits directory which contains a single string, the password to the bot account")
			
			
#whenever an event happens to the client we need @client.event
#more reading up required
@client.event
@asyncio.coroutine 
def on_ready():
	print("logging on")
	client.accept_invite("https://discord.gg/0151VGd14XdgWWZpA")
	print("log in successful!");

@client.event
@asyncio.coroutine
#Whenever something happens in a voice channel
#including but not limited too member join, member leave,
#member mute/deafen/unmute/undeafen
#params: oldmember: the state of the member before the event flag
#		 member: the state of the member after the event flag
def on_voice_state_update(oldmember, member):
	if str(oldmember.voice_channel) == str(member.voice_channel):
		#Like when a user mutes/unmutes
		pass
	elif str(member.voice_channel) != "None":
		#The None channel is the lack of a channel, i.e: when a user is not in a voice channel
		msg = "{0.name} has joined {1}"
		yield from client.send_message(member.server, msg.format(member, member.voice_channel))
	elif str(member.voice_channel) == "None":
		#if the user joins the "None" channel, he's essentially leaving
		msg = "{0.name} has left {1}"
		yield from client.send_message(member.server, msg.format(member, oldmember.voice_channel))

#credentials, not secured, I don't really care at this point
#run command logs in the bot, since the bot is a user she'll join
#all the channels she's a part of.
#params: username, password
client.run('simplenamibot@gmail.com', readPassFromFile())