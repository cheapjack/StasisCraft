#!/usr/bin/python

#from mciot import ServerConnection
from mcpi import minecraft
from mcpi import block
from mcpi import minecraftstuff
#cfrom pyfirmata import Arduino, util, INPUT
from time import sleep
import server
import thread

mc = minecraft.Minecraft.create(server.address)
mcdrawing = minecraftstuff.MinecraftDrawing(mc)


# Use the command /getpos to find out where you are then use those
# x, y, z coordinates to build things
# translate mc coords for mcpi ones
# add this to x
mcx = 177
# - this from y
mcy = 64
# - this from z
mcz = 135

EndocrineOver = False

def Temp1(x, y, z, max_temp, pause_length):
        while not EndocrineOver:
        #try:
                for i in range(max_temp):
                        mc.setBlocks((x + mcx), (y - mcy), (z - mcz), (x + mcx)+ 2, (y - mcy)+ i, (z - mcz) + 2, 35, i)
                        print i
                        sleep(pause_length)
                print "Its too damn Hot!"
                #mc.postToChat("It's getting a bit too hot for enzymes in here!")
                for i in range(max_temp, 0, -1):
                        mc.setBlocks((x + mcx), (y - mcy), (z - mcz), (x + mcx)+ 2, (y - mcy)+ i, (z - mcz) + 2, 35, i)
                        mc.setBlocks((x + mcx), (y - mcy) + i, (z - mcz), (x + mcx)+ 2, (y - mcy) + max_temp, (z - mcz) + 2, 0)
                        print i
                        sleep(pause_length)
                print "Ok back to normal"
                #mc.postToChat("It's enzyme heaven in here")
        #except KeyboardInterrupt:
		print("Stopped")
        #finally:
                


try:
        while not EndocrineOver:
                print "Running!"
		#thread.start_new_thread(Temp1, (-455, 89, -1359, 15, 1))
		#thread.start_new_thread(Temp1, (-445, 89, -1359, 15, 2))
		thread.start_new_thread(Temp1, (-455, 89, -1379, 15, 3))
		thread.start_new_thread(Temp1 (-445, 89, -1379, 15, 4))
except:
        print "Over"
finally:
        EndocrineOver = True
	print "Stopped now"
        
