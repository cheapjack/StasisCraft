#!/usr/bin/python

#Install the modules we need
#from pyfirmata import Arduino, util, INPUT
from mcpi import minecraft
from mcpi import minecraftstuff
from time import sleep
import server
import serial


# Use the command /getpos or F3 in Minecraft client to find out where you are then use those
# x, y, z coordinates to build things
# translate mc coords for mcpi ones
# add this to x
mcx = 177
# - this from y
mcy = 64
# - this from z
mcz = 135
# Connect to the server we use the imported server.py to make it work with CloudMaker
mc = minecraft.Minecraft.create(server.address)
#Post a message to the minecraft chat window 
mc.postToChat("Ready to read Dermis Temperature 1!")


dermisfull = False
dermisfull2 = False
dermisfull3 = False

# Text Bubble 1
# use `/js blocktype("My\nMessage", blocktypenumbercode) to build text and note \n represents a new line
def MemoryCloud1(startx,starty,startz, chartwidth, chartheight, chartdepth, blocktype, blockid):
	# Main Bubble
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx) + chartwidth, (starty-mcy) + chartheight, (startz - mcz) + chartdepth, blocktype, blockid)
	# inset bottom
	mc.setBlocks((startx + mcx) + 1, (starty-mcy) - 1, (startz-mcz), (startx + mcx) + (chartwidth-1), (starty-mcy) -1, (startz - mcz) + chartdepth, blocktype, blockid)
	#inset top
	mc.setBlocks((startx + mcx) + 1, (starty-mcy) + (chartheight + 1), (startz-mcz), (startx + mcx) + (chartwidth-1), (starty-mcy) + (chartheight + 1), (startz - mcz) + chartdepth, blocktype, blockid)

# define a barchart function 

def DermisTemperatureBlock(startx, starty, startz, dermiswidth, dermisheight, blocktype, blockid):
	# Make a stage
	mc.setBlocks((startx + mcx) - 2, (starty-mcy), (startz-mcz) - 2, (startx + mcx) + (dermiswidth + 2), (starty-mcy), (startz - mcz) + (dermiswidth + 2), blocktype, blockid)
	# Make glass walls
	mc.setBlocks((startx + mcx) - 1, (starty-mcy), (startz-mcz) - 1, (startx + mcx) + dermiswidth + 1, (starty-mcy) + dermisheight, (startz - mcz) + 1 + dermiswidth, 20)
	# Hollow inside of walls
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx) + dermiswidth, (starty-mcy) + dermisheight, (startz - mcz) + dermiswidth, 0)
	#Take off the 'lid'
	mc.setBlocks((startx + mcx), (starty-mcy)+dermisheight, (startz-mcz), (startx + mcx) + dermiswidth, (starty-mcy) + dermisheight, (startz - mcz) + (dermiswidth), 0)
	# Make an underfloor light
	mc.setBlocks((startx + mcx) - 1, (starty-mcy) - 1, (startz-mcz) - 1, (startx + mcx) + dermiswidth + 1, (starty-mcy) - 1, (startz - mcz) + dermiswidth + 1, 89)
	mc.setBlocks((startx + mcx), (starty-mcy) - 1, (startz-mcz), (startx + mcx) + dermiswidth, (starty-mcy) - 1, (startz - mcz) + (dermiswidth), blocktype, blockid)


def HairDown(startx, starty, startz, hairheight, blocktype, blockid):
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx) + hairheight, (starty-mcy), (startz - mcz), blocktype, blockid)
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx), (starty-mcy) + hairheight, (startz - mcz), 0)


def HairUp(startx, starty, startz, hairheight, blocktype, blockid):
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx) + hairheight, (starty-mcy), (startz - mcz), 0)
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx), (starty-mcy) + hairheight, (startz - mcz), blocktype, blockid)


def VasoDilate(startx, starty, startz, dilation, blocktype, blockid):
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx) + 20, (starty-mcy), (startz - mcz) - dilation , blocktype, blockid)

def VasoConstrict(startx, starty, startz, dilation, blocktype, blockid):
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx) + 20, (starty-mcy), (startz - mcz) - 4 , 35, 2)
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz)-1, (startx + mcx) + 20, (starty-mcy), (startz - mcz) - dilation , blocktype, blockid)

# Gonna make you sweat
def Sweat(startx, starty, startz, sweatheight, blocktype):
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx), (starty-mcy) + sweatheight, (startz - mcz), blocktype)
def NoSweat(startx, starty, startz, sweatheight, blocktype):
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx), (starty-mcy) + sweatheight, (startz - mcz), 0)


# Hair Response
def DermisListener1(startx, starty, startz, dermisno):
	global dermisfull
	#Listen for blocks filling up leve
	blockType = mc.getBlock((startx + mcx), (starty - mcy), (startz - mcz), 1)
	if blockType != 0:
		print "It's really hot in SkinTemp ", dermisno, blockType
		sleep(0.5)
		#print "1st", dermisfull
		#mc.postToChat("WARNING! Dermis Sensor" + str(dermisno) + " is full!")
		HairDown(394, 89, -1150, 20, 35, 12)
		if not dermisfull:
			mc.postToChat("WARNING! Dermis Sensor" + str(dermisno) + " is full!")
			mc.postToChat("Triggering dermis Hair response")
			mc.postToChat("Hypothalamus you need to reduce temperature!")
			mc.postToChat("Hypothalamus, direct your response team!")
			sleep(0.5)
			HairDown(394, 89, -1150, 20, 35, 12)
			sleep(0.5)
			dermisfull = True
			#print "2nd", dermisfull
	else:
		if dermisfull:
			HairUp(394, 89, -1150, 20, 35, 12)
			print "Nothing from " + str(dermisno)
			dermisfull = False
			#print dermisFull
			sleep(5)

# Vascular Dilation
def DermisListener2(startx, starty, startz, dermisno):
	global dermisfull2
	#Listen for blocks filling up level
	blockType = mc.getBlock((startx + mcx), (starty - mcy), (startz - mcz))
	if blockType != 0:
		print "It's really hot in SkinTemp " , dermisno, blockType
		sleep(0.5)
		#print "1st", dermisfull2
		#mc.postToChat("WARNING! Dermis Sensor" + str(dermisno) + " is full!")
		VasoDilate(393, 87, -1161, 4, 35, 14)
		#HairUp(394, 89, -1150, 20, 35, 12)
		if not dermisfull2:
			mc.postToChat("WARNING! Dermis Sensor" + str(dermisno) + " is full!")
			mc.postToChat("Hypothalamus you need to reduce temperature!")
			sleep(0.5)
			VasoDilate(393, 87, -1161, 4, 35, 14)
			sleep(0.5)
			dermisfull2 = True
			#print "2nd", dermisfull2
	else:
		if dermisfull2:
			#HairDown(394, 89, -1150, 20, 35, 12)
			VasoConstrict(393, 87, -1161, 2, 35, 14)
			print "Nothing from " + str(dermisno)
			dermisfull2 = False
			#print dermisFull2
			sleep(5)


# Build First blocks
# The MemoryCloud needs more x and less z to centre it
# Overwrite Memory Text
#MemoryCloud1(288, 105, -1164, 20, 12, 2, 35, 8)
DermisTemperatureBlock(285, 89, -1160, 4, 10, 35, 4)
# Second block
#MemoryCloud1(334, 105, -1164, 20, 12, 2, 35, 6)
DermisTemperatureBlock(332, 89, -1160, 4, 10, 35, 4)
# Draw window into epidermis to observe vaso-dilation
VasoDilate(393, 88, -1161, 4, 20, 0)
# Draw a sweat example
#Sweat(399, 84, -1176, 5, 8) 
#Main Loop

while True:
	#Make a DermisListeners() and listen
	#arguments are startx, starty, startz, dermiswidth, dermisheight, dermisno
	# with the same width and thickness as the corresponding DermisTemperatureBlocks
	# SkinTemp 1 Hair Response
	#DermisListener1(285, 89, -1160, 1)
	DermisListener1(287, 99, -1158, 1)
	# Skin Temp2 Vascular system response
	DermisListener2(334, 99, -1158, 2)
	#DermisListener2(332, 99, -1155, 4, 10, 1)
	#DermisListener3(332, 89, -1160, 4, 10, 2)

#while True:
	# Remember your chart is (x_coord, x_coord, x_coord, chartwidth, dermisheight, block block id(usually 0)) 
#	TemperatureChart1(394, 68, -326, 2, 40, 35, 5)
	#TemperatureChart2(394, 68, -318, 2, 40, 35, 4)
	#TemperatureChart3(394, 68, -310, 2, 40, 35, 4)
	#TemperatureChart4(394, 68, -302, 2, 40, 35, 4)
	#TemperatureChart5(394, 68, -294, 2, 40, 35, 4)

print "stopped"
