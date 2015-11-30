# StasisCraft Workshop 2
## Visualising Homeostasis: Body Temperature
 
![stasiscraftdynmapsmall](https://cloud.githubusercontent.com/assets/128456/11134653/6ae6e364-8996-11e5-910b-b4cab7d953d9.png)

Uses Minecraft PC client version `1.7.9` running `Bukkit-1.7.2` with the server `mc.fact.uk`


###Activity

####Revisiting Thermoregulation zone

 1. Sit in groups at the breakout tables with some paper and whiteboard
 * Introduce Minecraft for those who have not played it.
 * Explain the **Performing Thermoregulation game** again
 * Play through

####Thermo-Regulation Game

to get to the StasisCraft zone you need to `/warp stasiscraft`

####Performing Thermoregulation

 * We are going to split into 2 groups

####Temperature Stimulus Team

 * CloudMaker01 - CloudMaker04 Temperature rising Hypothalamus group 
  * `/warp skintemp1` to get to your area

It's your job to be the stimulus in the system, in this case we are representing temperature through glass *silos* with giant flowchart labels. When the silo is full (top centre block) of sand it will be marked as **too hot** ie the Dermis and other parts of the nervous system will send signals to the **Hypothalamus** to react.

You will use the [RF-Craft](https://github.com/cheapjack/StasisCraft/blob/master/Workshop2.md#hypothalamus-radio) buttons like a **Hypothalamus radio** stimulaing the system to increase temperature, and then responding to the Hypothalamus alerts and commands. You need to **STIMULATE** then **LISTEN** to the feedback response or you will all die...

 * Use the `GREEN` & `YELLOW` RF-Craft Buttons to fill the 2 Temperature silos with sand. The trigger point is the centre top of each silo
 * Once we have triggered the response you need to wait from orders from Hypothalamus
 * Hypothalamus orders with `/say Hypo says reduce SkinTemp1` or `/say Hype says reduce SkinTemp2 with BLUE button`
 * Please respond to the Hypothalamus or your bacterial mega-community will die!

####Hypothalamus Team

 * CloudMaker07 - CloudMaker09 & CloudMaker 
  * `/warp hair`

This team are effectively the **Hypothalamus** team and act out in the game the  autonomous nervous system's response to rises in temperature. This is the start of the negative feedback 'system'

Your main task is to perform the sweat response with water buckets following the Dermis hair and vascular responses. Listen to your Hypothalamus commands and once youve made enough 'sweat' you can remove it by using the `/drain 100` command near the water. You will need to be op to do that so choose one person and request this from the `sysadmin`

The silo **SkinTemp2** triggers the epidermal vascular response; blood vessels near the skin surface constrict and blood flows deeper in the skin to conserve heat. 
If too hot blood vessels near the skin surface dilate and blood flows closer to  the skin surface to lose heat, in the game the red wool is thicker beneath the glass blocks in the `hair` area, and in reality pale skinned people go pink!

 * CloudMaker05 - 06
Keep an eye on all things you are the Hypothalamus! Hit the red button to trigger a Hypothalamus redstone ore sphere to flash in the dermis area and send messages to your team.

Primarily the team simulates the sweat response. Once the dermis is sufficiently flooded use the chat to tell the SkinTemp team to use the `BLUE` button

###Game - Over

Hypothalamus can call game over and we can break away from our computers and disconnect from the game.

###RF-Craft: The Hypothalamus Radio

RF-Craft is a [CloudMaker](https://github.com/cheapjack/CloudMaker/) resource that sends messages through concrete using the  868MHz amateur radio band as an alternative to managed WiFi

We are using the RF-Craft Buttons to trigger certain events:
 * RED - **Hypothalamus Alert** Builds a hypothalamus shaped redstone ore sphere as an alert
 * GREEN - **SkinTemp1 Silo Increase** Fills the SkinTemp1 silo with sand to visualise increase in temperature
 * YELLOW - **SkinTemp2 Silo Increase** Fills the SkinTemp2 silo with sand to visualise increase in temperature
 * BLUE - **Decrease Temperature** Removes sand from both silos to visualise decrease in temperature
 

###Activity 2

####Labelling Thermoregulation
 
  * Labelling and modding the dermis landscape model

###Activity 3

####Building Parkour FlowCharts

 * Use `ScriptCraft` to build flowcharts

Format is `/js box("35:4", x (east/west coordinate, y (up or down coordinate), z (north/south coordinate)` but you always need to build from a start block, the one you are **looking** at to refer from: look at the block and run the command to build from that point

You can also add `/up()` and `down()` functions before you start to 
so `/js up(2).box("35:14", 10, 6, 2)` builds a box 10 across, 6 high and 2 thickness/depth) after moving up 2 blocks from the one you are looking at.


![hypothalamus_small](https://cloud.githubusercontent.com/assets/128456/11132490/17ac85fe-8988-11e5-8daf-c4e3992d1681.gif)

####Hypothalamus Says 

(using `/say` & `/whisper` commands)

####Minecraft 101

It's a building game that uses these basic controls:

 * `MENU` - `esc` then customise controls in `OPTIONS` or use defaults below
 * `UP` - `w`
 * `DOWN` - `s`
 * `LEFT` - `a`
 * `RIGHT` - `s`
 * `JUMP` - `SPACE`
 * `FLY` - double-hit the `SPACE` bar and hold it to fly 
  * use `SHIFT` to descend and another double-hit on `SPACE` to fall
 * `BUILD` - `right-click` on the `MOUSE`
 * `BREAK` - `left-click` on the `MOUSE`
 * `SELECT` - custom key
 * `INVENTORY` - `e`

Typing `/` will open the minecraft chat/terminal window where you can issue commands like

 * `/say Hello` - Say Hello to the server
 * `/whisper <message> <playername>` - Whisper something directly to another player
 * `/warp <warplocation>` - Warp to specific warp locations, we use:
  * `/warp hair` , `/warp skintemp1` , `/warp stasiscraft
 * `/js box(20)` build a glass box on the block you are looking at
 * `/` then `delete` the forward slash to just talk to the server


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


