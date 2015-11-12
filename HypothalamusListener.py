#!/usr/bin/python
# Import modules for mcpi etc
from time import sleep
from mcpi import minecraft
from mcpi import minecraftstuff
import server

mc = minecraft.Minecraft.create(server.address)
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
mc.postToChat("Server started watching block events")

# Use F3 to find out where you are then use those
# x, y, z coordinates to build things
# translate mc coords for mcpi ones
# add this to x
mcx = 177
# - this from y
mcy = 64
# - this from z
mcz = 135

def makeSphere(x, y, z, radius, blocktype):
        mcdrawing.drawSphere((x + mcx), (y - mcy), (z - mcz), radius, blocktype)

def getLevel(x, ylimit, z):
	blocktype = mc.getBlock((x+mcx), (ylimit-mcy), (z - mcz))
	if blocktype != 0:
		print "Getting hot!"
	return blocktype

def Test1(x, y, z, max_temp, pause_length):
                print getLevel(x, y, z)
		if getLevel(x, y, z) != 0:
                        makeSphere(-448, 95, -1368, 4, 20)
                        sleep(pause_length)
			makeSphere(-448, 95, -1368, 4, 0)
			#mc.setBlocks((x + mcx), (y - mcy), (z - mcz), (x + mcx) + 2, (y - mcy) + max_temp, (z - mcz) + 2, 35, i)
                	print "Its too damn Hot!"
                	#mc.postToChat("It's getting a bit too hot for enzymes in here!")


try:
	while True:
		Test1(-443, 97, -1359, 20, 1)
except:
	pass
finally:
	makeSphere(-448, 95, -1368, 4, 0)


