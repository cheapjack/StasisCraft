#!/usr/bin/python

# Moteino Receiver for RF-Crafting and button-craft

from mcpi import minecraft
from mcpi import  minecraftstuff
import server
import serial
from time import sleep

mc = minecraft.Minecraft.create(server.address)

mcdrawing = minecraftstuff.MinecraftDrawing(mc)


# use the default mac serial port, '/dev/tty.SLAB_USBtoUART' this will change platform to platform
ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 9600)
#RED BUTTON 1
button1_received_on = "1,1\r\n"
#YELLOW BUTTON 2
button2_received_on = "2,1\r\n"
#GREEN BUTTON 3 
button3_received_on = "3,1\r\n"
#BLUE BUTTON 4 
button4_received_on = "4,1\r\n"
#Breadboard Button BUTTON 5 
button5_received_on = "5,1\r\n"
# The Button sends the serial message (node, action)
# action: "1", "Button Pressed"
#	"2", "Error"
#	"3", "OK"

# translate mc coords for mcpi ones
# add this to x
mcx = 177
# - this from y
mcy = 64
# - this from z
mcz = 135

def removeSand(x, y, z, blocktype):
	mc.setBlocks((x + mcx), (y - mcy) , (z - mcz), (x + mcx) + 4, (y - mcy) , (z-mcz) + 4, blocktype)

def makeSand1(x, y, z, blocktype):
	mc.setBlocks((x + mcx), (y - mcy) , (z - mcz), (x + mcx) + 4, (y - mcy) , (z-mcz) + 4, blocktype)

def makeSand2(x, y, z, blocktype):
	mc.setBlocks((x + mcx), (y - mcy) , (z - mcz), (x + mcx) + 4, (y - mcy) , (z-mcz) + 4, blocktype)

def makeCircle(x, y, z, blocktype):
	mcdrawing.drawCircle(x, y, z, blocktype)

def beacon(x, y, z):
        playerPos = mc.player.getPos()
        mc.postToChat("Made A beacon near " + str(x) + " " + str(y) + " " + str(z))
        sleep(1)
        mc.setBlocks((x + mcx)+1, (y - mcy)-1, (z - mcz)+1, (x + mcx)+3, (y - mcy), (z - mcz)+3, 57)
        mc.setBlock((x + mcx)+2, (y - mcy)+1, (z-mcz)+2, 138)
        sleep(1)



# takes a minecraft coord and translates it for mcpi
def makeSphere(x, y, z, radius, blocktype):
	#playerPos = mc.player.getPos()
	#playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))	
	#mcdrawing.drawSphere(playerPos.x - (radius*2), playerPos.y - (radius*2), playerPos.z - (radius*2), radius, blocktype)
	mcdrawing.drawSphere(x + mcx, y - mcy, z - mcz, radius, blocktype)

mc.postToChat("Hello CloudMaker this is Serial " + str(ser.readline()))

while True:
	serialcommand = str(ser.readline())
	if serialcommand == button1_received_on:
		print "We've Got Mail from Button 1!"
		mc.postToChat("We've Got Mail from Button 1! It says: " + serialcommand)
		mc.postToChat("Hypothalamus Blood cell water Alert...")
		mc.postToChat("Triggering hormonal response...")
		mc.postToChat("Hypothalamus send messages to your team!")
		makeSphere(503, 126, -1175, 10, 73)
		sleep(0.5)
		makeSphere(503, 126, -1175, 10, 0)
		#openDoor1(596, 3, -451)
		#beacon(185, 86, -273)
		#makeBlock(20)
	elif serialcommand == button2_received_on:
		print "We've Got Mail from Button 2!"
#		makeSand2(332, 99, -1160, 12)
		mc.postToChat("We've Got Mail from Button 2!")
		mc.postToChat("Increasing Water Content  2!")
		#openDoor2(612, 3, -452)
		makeSand1(498, 101, -1160, 12)
	elif serialcommand == button3_received_on:
		print "We've Got Mail from Button 3!"
		mc.postToChat("We've Got Mail from Button 3!")
		mc.postToChat("Increasing Glucose Content!")
		makeSand1(498, 101, -1160, 12)
		#openDoor3(613, 3, -436)
	elif serialcommand == button4_received_on:
		print "We've Got Mail from Button 4!"
		mc.postToChat("We've Got Feedback from Button 4!")
		mc.postToChat("Reducing sand content/water monitor")
		#openDoor4(597, 3, -435)
		removeSand(332, 89, -1160, 0)
		removeSand(285, 89, -1160, 0)
	elif serialcommand == button5_received_on:
		print "We've Got Mail from Reset Button 5!"
		mc.postToChat("We've Got Mail from Button 5!")
		mc.postToChat("GAME OVER!")
		makeSphere(503, 126, -1175, 10, 46)
		#makeDoor1(596, 3, -451)
		#makeDoor2(612, 3, -452)
		#makeDoor4(597, 3, -435)
		#makeDoor3(613, 3, -436)
	else:
		print "Nothing"
#		mc.postToChat("Nothing")
	sleep(0.5)
