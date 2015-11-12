#!/usr/bin/python

# Moteino Receiver for RF-Crafting and button-craft

from mcpi import minecraft
from mcpi import  minecraftstuff
import server
import serial
from time import sleep

mc = minecraft.Minecraft.create(server.address)

mcdrawing = minecraftstuff.MinecraftDrawing(mc)
# a flag to see if Hypothalamus is activated
HypoStatus = False
# use the default mac serial port, '/dev/tty.SLAB_USBtoUART' this will change platform to platform
ser = serial.Serial('/dev/tty.SLAB_USBtoUART6', 9600)
#button1_received_on = "1,1\r\n"
#button2_received_on = "1,2\r\n"
#button3_received_on = "1,3\r\n"
#button4_received_on = "1,4\r\n"
button1_received_on = "1,1\r\n"
button2_received_on = "2,1\r\n"
button3_received_on = "3,1\r\n"
button4_received_on = "4,1\r\n"
# The Button sends the serial message (action , node)
# action: "1", "Button Pressed"
#	"2", "Error"
#	"3", "OK"

# translate mc coords for mcpi ones
# add this to x
mcx = 177
#mcx = 0
# - this from y
mcy = 64
#mcy = 0
# - this from z
mcz = 135
#mcz = 0

def makeDoor1(x, y, z):
	mc.setBlocks(x + mcx, y - mcy, z - mcz, x + 1, y + 3, z - 1, 0)
def makeDoor2(x, y, z):
	mc.setBlocks(x + mcx, y - mcy, z - mcz, x + 1, y + 3, z + 1, 0)
def makeDoor3(x, y, z):
	mc.setBlocks(x + mcx, y - mcy, z - mcz, x - 1, y + 3, z + 1, 0)
def makeDoor4(x, y, z):
	mc.setBlocks(x + mcx, y - mcy, z - mcz, x - 1, y + 3, z - 1, 0)

def makeCircle(x, y, z, blocktype):
	mcdrawing.drawCircle(x, y, z, blocktype)
def makeSphere(x, y, z, radius, blocktype):
        mcdrawing.drawSphere((x + mcx), (y - mcy), (z - mcz), radius, blocktype)

def beacon(x, y, z):
        playerPos = mc.player.getPos()
        mc.postToChat("Made A beacon near " + str(x) + " " + str(y) + " " + str(z))
        sleep(1)
        mc.setBlocks((x + mcx)+1, (y - mcy)-1, (z - mcz)+1, (x + mcx)+3, (y - mcy), (z - mcz)+3, 57)
        mc.setBlock((x + mcx)+2, (y - mcy)+1, (z-mcz)+2, 138)
        sleep(1)

def makeBlock(blocktype):
	playerPos = mc.player.getPos()
	playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))
	mc.setBlock(playerPos.x + 2, playerPos.y + 2, playerPos.z + 2, blocktype)

def makeTreasure(x, y, z, blocktype):
	mc.setBlock(x + mcx, y - mcy, z - mcz, blocktype)

# takes a minecraft coord and translates it for mcpi
def makeSphere(x, y, z, radius, blocktype):
	#playerPos = mc.player.getPos()
	#playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))	
	#mcdrawing.drawSphere(playerPos.x - (radius*2), playerPos.y - (radius*2), playerPos.z - (radius*2), radius, blocktype)
	mcdrawing.drawSphere(x + mcx, y - mcy, z - mcz, radius, blocktype)

mc.postToChat("Hello CloudMaker this is Serial " + str(ser.readline()))

while True:
	serialcommand = str(ser.readline())
	#global HypoStatus
	if serialcommand == button1_received_on:
		print "We've Got Mail from Button 1!"
		mc.postToChat("Hypothalamus! You've got mail from Button 1! It says: " + serialcommand)
		mc.postToChat("Hypothalamus awakes!...")
		makeSphere(-447, 100, -1368, 5, 73)
		#makeSphere(-447, 100, -1368, 4, 0)
		#HypoStatus = False
		#makeDoor1(596, 3, -451)
		#beacon(185, 86, -273)
		#makeBlock(20)
		#makeTreasure(-197, 152, 81, 89)
		#makeTreasure(2765, -50, 4078, 20)
		#makeCircle(-199, 109, 108, 6, 89)
	elif serialcommand == button2_received_on:
		print "We've Got Mail from Button 2!"
		mc.postToChat("We've Got Mail from Button 2!")
		#mc.postToChat("Shutting Down Hypothalamus...")
		mc.postToChat("Building...")
		#makeSphere(-447, 100, -1368, 5, 0)
		#makeDoor2(612, 3, -452)
	elif serialcommand == button3_received_on:
		print "We've Got Mail from Button 3!"
		mc.postToChat("We've Got Mail from Button 3!")
		mc.postToChat("Building...")
		makeDoor3(613, 3, -436)
	elif serialcommand == button4_received_on:
		print "We've Got Mail from Button 4!"
		mc.postToChat("We've Got Mail from Button 4!")
		#mc.postToChat("Building...")
		mc.postToChat("Shutting Down Hypothalamus...")
		makeSphere(-447, 100, -1368, 5, 0)
		#makeDoor4(597, 3, -435)
	else:
		print "Nothing"
#		mc.postToChat("Nothing")
	sleep(0.5)
