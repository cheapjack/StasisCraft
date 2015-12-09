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
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#Post a message to the minecraft chat window 
mc.postToChat("Ready to read Dermis Temperature 1!")


dermisfull = False
dermisfull2 = False
#dermisfull3 = False

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

def UrineConcentrationBlock(startx, starty, startz, dermiswidth, dermisheight, blocktype, blockid):
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

def NormalBloodCell(startx, starty, startz, radius, blocktype, blockid):
	mcdrawing.drawSphere((startx + mcx), (starty-mcy), (startz-mcz), radius, blocktype, blockid)
	# remove the excess sphere to flatten it
	mc.setBlocks((startx + mcx) + 2, (starty-mcy) - radius, (startz-mcz) + radius, (startx + mcx) + (radius + 1), (starty-mcy) + radius, (startz - mcz) - radius, 0)
	mc.setBlocks((startx + mcx) - 2, (starty-mcy) - radius, (startz-mcz) + radius, (startx + mcx) - (radius + 1), (starty-mcy) + radius, (startz - mcz) - radius, 0)


def FatBloodCell(startx, starty, startz, radius, blocktype, blockid):
	mcdrawing.drawSphere((startx + mcx), (starty-mcy), (startz-mcz), radius, blocktype, blockid)
	# remove the excess sphere to flatten it
	mc.setBlocks((startx + mcx) + radius/1.5, (starty-mcy) - radius, (startz-mcz) + radius, (startx + mcx) + (radius + 1), (starty-mcy) + radius, (startz - mcz) - radius, 0)
	mc.setBlocks((startx + mcx) - radius/1.5, (starty-mcy) - radius, (startz-mcz) + radius, (startx + mcx) - (radius + 1), (starty-mcy) + radius, (startz - mcz) - radius, 0)


# Blood Sugar Listener and response
def DermisListener1(startx, starty, startz, dermisno):
	global dermisfull
	#Listen for blocks filling up level
	blockType = mc.getBlock((startx + mcx), (starty - mcy), (startz - mcz), 1)
	if blockType != 0:
		print "Too much glucose in Blood ", dermisno, blockType
		sleep(0.5)
		#print "1st", dermisfull
		#mc.postToChat("WARNING! Dermis Sensor" + str(dermisno) + " is full!")
		# Blood cells balloon out
		
		#HairDown(394, 89, -1150, 20, 35, 12)
		if not dermisfull:
			mc.postToChat("WARNING! Blood Sugar Content " + str(dermisno) + " is full!")
			# Liver makes glycogen (orange wool)
			mcdrawing.drawSphere(490 + mcx, 98 - mcy, -1200 - mcz, 6, 35, 1)
			mcdrawing.drawSphere(495 + mcx, 98 - mcy, -1200 - mcz, 6, 35, 1)
			#mcdrawing.drawSphere(495, 200, -1200, 10, 46, 0)
			mc.postToChat("Hypothalamus you need to reduce sugar content!")
			mc.postToChat("Hypothalamus, direct your response team!")
			mc.postToChat("We need to convert glucose to glycogen!")
			sleep(0.5)
			dermisfull = True
			#print "2nd", dermisfull
	else:
		if dermisfull:
			# Liver in standby (purple wool)
			mcdrawing.drawSphere(490 + mcx, 98 - mcy, -1200 - mcz, 6, 35, 10)
			mcdrawing.drawSphere(495 + mcx, 98 - mcy, -1200 - mcz, 6, 35, 10)
			print "Nothing from " + str(dermisno)
			dermisfull = False
			#print dermisFull
			sleep(5)

# Blood cell water increase 
def DermisListener2(startx, starty, startz, dermisno):
	global dermisfull2
	
	#Listen for blocks filling up level
	blockType = mc.getBlock((startx + mcx), (starty - mcy), (startz - mcz))
	if blockType != 0:
		print "It's really wet in the blood! " , dermisno, blockType
		sleep(0.5)
		#print "1st", dermisfull2
		#mc.postToChat("WARNING! Dermis Sensor" + str(dermisno) + " is full!")
		#VasoDilate(393, 87, -1161, 4, 35, 14)
		#HairUp(394, 89, -1150, 20, 35, 12)
		if not dermisfull2:
			mc.postToChat("WARNING! Blood Water Content " + str(dermisno) + " is full!")
			# Kidney Tubules become more permeable to allow for water to leave the body: Time to fill the urine hoppers!
			
			mc.postToChat("Hypothalamus you need to reduce water content!")
			mc.postToChat("Hypothalamus, direct your response team!")
			FatBloodCell(528, 99, -1208, 6, 35, 14)
			mcdrawing.drawCircle(500 + mcx, 99 - mcy , -1180 - mcz, 6, 35,12)
			mcdrawing.drawCircle(500 + mcx, 99 - mcy, -1180 - mcz, 3, 0, 0)
			sleep(0.5)
			dermisfull2 = True
			#print "2nd", dermisfull2
	else:
		if dermisfull2:
			print "Nothing from " + str(dermisno)
			# Blood cells shape swells with water content, no longer work efficiently
			# Kidney Tubules become less permeable to  water to be lost as urine
			mcdrawing.drawCircle(500 + mcx, 99 - mcy, -1180 - mcz, 6, 0, 0)
			mcdrawing.drawCircle(500 + mcx, 99 - mcy, -1180 - mcz, 3, 35, 12)
			FatBloodCell(528, 99, -1208, 6, 35, 0)
			NormalBloodCell(528, 99, -1208, 6, 35, 14)
			dermisfull2 = False
			#print dermisFull2
			sleep(5)


# Build First blocks
# The MemoryCloud needs 3 more x, 2 more y and 4 less z to centre it
# Overwrite Memory Text
#MemoryCloud1(288, 105, -1164, 20, 12, 2, 35, 8)
#MemoryCloud1(500, 117, -1168, 20, 12, 2, 35, 7)
#UrineConcentrationBlock(285, 89, -1160, 4, 10, 35, 4)
UrineConcentrationBlock(479, 91, -1160, 4, 10, 35, 7)
# Second block
#MemoryCloud1(476, 117, -1168, 20, 12, 2, 35, 3)
#MemoryCloud1(334, 105, -1164, 20, 12, 2, 35, 6)
#UrineConcentrationBlock(332, 89, -1160, 4, 10, 35, 4)
UrineConcentrationBlock(498, 91, -1160, 4, 10, 35, 4)
# Draw Extra silos for dumping water 

UrineConcentrationBlock(479, 91, -1190, 4, 10, 35, 4)
UrineConcentrationBlock(479, 91, -1190, 4, 10, 35, 4)
# Main Loop

sleep(2)

while True:
	#Make a DermisListeners() and listen
	# arguments are startx, starty, startz, dermisno
	# x + 2, z + 2, y + height to the corresponding UrineConcentrationBlocks
	# Blood Water Content Response
	DermisListener1(481, 101, -1158, 1)
	DermisListener2(500, 101, -1158, 2)

print "stopped"
