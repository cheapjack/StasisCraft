# StasisCraft Workshop 2
## Visualising Homeostasis: Body Temperature
 
![stasiscraftdynmapsmall](https://cloud.githubusercontent.com/assets/128456/11134653/6ae6e364-8996-11e5-910b-b4cab7d953d9.png)

Uses Minecraft PC client version `1.7.9` running `Bukkit-1.7.2` with `mc.fact.uk`


###Activity

To get to the StasisCraft zone you need to `/warp stasiscraft`

####Labelling Thermoregulation
 
  * Labelling and modding the dermis landscape model

####Building Parkour FlowCharts

 * Use `ScriptCraft` to build flowcharts

Format is `/js box("35:4", x (east/west, y, z (north/south)` but you always need to build a start block to refer from: look at the block and run the command to build from that point

You can also add up() and down() functions before you start to 
so `/js up(2).box("35:14", 10, 6, 2)` builds a box 10 across, 6 high and 2 thickness/depth)


![hypothalamus_small](https://cloud.githubusercontent.com/assets/128456/11132490/17ac85fe-8988-11e5-8daf-c4e3992d1681.gif)

####Hypothalamus Says 

(using `/say` & `/whisper` commands)

####ScriptCraft Reference
Get the full info on github from http://scriptcraftjs.org/

Shapes

 * box( blocks.material, width, height, depth ) - creates a solid box 
 * box0( blocks.material, width, height, depth ) - creates an empty box (with the insides hollowed out - perfect for dwellings.
 * box( blocks.material, width, height, depth ) - creates an empty box (with the insides hollowed out - perfect for dwellings.
 * cylinder( blocks.material, radius, height ) - creates cylinders, perfect for Chimneys.
 * cylinder0( blocks.material, radius, height ) - creates empty cylinders 
 * prism( blocks.material, width, depth ) - creates a Prism - good for roofs.

Just substitute 'block.material' for 'block.wool.red' or 'block.ice' or 'block.brick.red' type /js block. then use tab to see the different materials autocomplete in the command line

Movement

The 'drone' is the invisible cursor that 'builds' things in minecraft; whatever block is highlighted as you look at it is the drone start position. You can combine commands by using a dot between commands. So /js box(block.ice).right(2).box(block.ice, 2,2,2) makes a single block of ice, moves 2 blocks to the right and makes a 2x2x2 block of ice


 * up( numberOfBlocks ) - moves the Drone Up. For example: up() will move the Drone 1 block up. You can tell it how many blocks to move if you want it to move more than one block.
 * down( numberOfBlocks ) - moves the Drone Down.
 * left( numberOfBlocks ) - moves the Drone Left.
 * right( numberOfBlocs ) - moves the Drone Right.
 * fwd( numberOfBlocs ) - moves the Drone Forward (away from the player).
 * back( numberOfBlocs ) - moves the Drone Back (towards the player)
i
 * turn( numberOfTurns ) - Turns the Drone Clock-wise (right). For example: turn() will make the Drone turn right 90 degrees. turn(2) will make the Drone turn twice so that it is facing in the opposite direction.


