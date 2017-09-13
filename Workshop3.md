# StasisCraft Workshop 3
## Visualising Homeostasis: Osmo-Regulation and Blood sugar
 
![stasiscraftdynmapsmall](https://cloud.githubusercontent.com/assets/128456/11134653/6ae6e364-8996-11e5-910b-b4cab7d953d9.png)

Uses Minecraft PC client version `1.7.9` with the server `mc.fact.uk`

Following some game co-design around osmo-regualtion , thermo-regulation and other negative feedback systems in the human body like the hormonal regulation of blood sugar with **insulin** and the **pituitary gland** 

### Activity

#### Osmo-regulation zone

 1. Sit in groups at the breakout tables with some paper and whiteboard
 * Explain the **Performing Osmo-regulation game** based on the co-design notes from last session, again with RF-Craft and mcpi
  * Use `RF-Craft-Water.py` and `Osmo1.py` in the repo
 * Play through

#### Thermo-Regulation Game

to get to the StasisCraft zone you need to `/warp stasiscraft` and to get to the Osmo-regulation area it's `/warp osmo`

####Performing Osmo-regulation

 * As before split into 2 groups

#### Stimulus Team

 * CloudMaker01 - CloudMaker04 Temperature rising Hypothalamus group 
  * `/warp osmo1` to get to your area

It's your job to be the stimulus in the system, in this case we are representing water levels in the blood through the same glass *silos* with giant flowchart labels. When the silo is full (top centre block) of sand it will be marked as **dangerous water levels** ie the autonomous nervous system will send signals to the **Hypothalamus** to react:

The pituitary gland controls blood water concentration, this gland produces the hormone ADH. ADH is carried by the blood to the kidneys and increases the permeability of the kidney tubules allowing water to be reabsorbed from the tubules into the blood.

 * If blood water concentration falls, more water reabsorption is needed so that less water is lost as urine. ADH production is increased.
 * If blood water concentration rises, less water reabsorption is needed so that more water is lost as urine. ADH production is decreased.

You will use the [RF-Craft](https://github.com/cheapjack/StasisCraft/blob/master/Workshop2.md#hypothalamus-radio) buttons like a **Hypothalamus radio** stimulaing the system to increase water levels, and then respond to the Hypothalamus alerts and commands. You need to **STIMULATE** then **LISTEN** to the feedback response or you will all die...

 * Use the `GREEN` & `YELLOW` RF-Craft Buttons to fill the 2 Water content silos with sand. The trigger point is the centre top of each silo
 * Once we have triggered the response you need to wait from orders from Hypothalamus
 * Hypothalamus orders with `/say Hypo says reduce Water content` or `/say Hype says use BLUE button to stimulate ADH`
 * Please respond to the Hypothalamus or your bacterial mega-community will die!

#### Hypothalamus Team

 * CloudMaker07 - CloudMaker09 & CloudMaker 
  * `/warp tubules`

This team are effectively the **Hypothalamus** team and act out in the game the  autonomous nervous system's response to rises in water levels and glucose. This is the start of the negative feedback 'system'

Your main task is to perform the water loss response with water buckets in the silo next to the purple liver model following the circle responses which represent increases in permeability of kidney tubules. 

Listen to your Hypothalamus commands and once youve made enough 'urine' you can remove it by using the `/drain 100` command near the water. You will need to be op to do that so choose one person and request this from the `sysadmin`

The silo **Water Levels** triggers the kidneys to increase permeability, represented as a growing circle influenced by the hormone **ADH** from the **pituitary gland**. The blood cell model also grows fatter than usual as they can swell with water content.

The silo **Glucose Levels** triggers the Pancreas to release the **hormone** **insulin** to stimulate the Liver to convert **glucose** to **glucagen** and to be absorbed by cells in the body. We've visualised this by making a purple Liver 'activate' by turning into orange wool.


 * CloudMaker05 - 06
Keep an eye on all things you are the Hypothalamus! Hit the red button to trigger a Hypothalamus redstone ore sphere to flash in the Osmo area and send messages to your team.

Primarily the team simulates the sweat response. Once the dermis is sufficiently flooded use the chat to tell the Water level team to use the `BLUE` button

### Game - Over

Hypothalamus can call game over and we can break away from our computers and disconnect from the game.

### RF-Craft: The Hypothalamus Radio

RF-Craft is a [CloudMaker](https://github.com/cheapjack/CloudMaker/) resource that sends messages through concrete using the  868MHz amateur radio band as an alternative to managed WiFi

We are using the RF-Craft Buttons to trigger certain events:
 * RED - **Hypothalamus Alert** Builds a hypothalamus shaped redstone ore sphere as an alert in the Osmo warp area
 * GREEN - **Glucose Silo Increase** Fills the Glucose silo with sand to visualise increase in glucose levels
 * YELLOW - **Water Levels Silo Increase** Fills the Water Levels silo with sand to visualise increase in water levels
 * BLUE - **Decrease Water and Glucose** Removes sand from both silos to visualise decrease in water levels and glucose levels.
 

### Activity 2

#### Labelling Thermoregulation
 
  * Labelling and modding the dermis landscape model

### Activity 3

#### Building Parkour FlowCharts

 * Use `ScriptCraft` to build flowcharts

Format is `/js box("35:4", x (east/west coordinate, y (up or down coordinate), z (north/south coordinate)` but you always need to build from a start block, the one you are **looking** at to refer from: look at the block and run the command to build from that point

You can also add `/up()` and `down()` functions before you start to 
so `/js up(2).box("35:14", 10, 6, 2)` builds a box 10 across, 6 high and 2 thickness/depth) after moving up 2 blocks from the one you are looking at.

 * Use `ScriptCraft` to label charts with text

Format is as above to position the text, but using the blocktype() funtion

`/js blocktype("My\nMessage", 89)`

This builds minecraft style text "MY MESSAGE" from the block you are looking at `\n` is `newline` so you can have multiple lines of text. It will always render the last `newline` at the bottom of the block you are looking at.

 * Use `ScriptCraft` to build stairs between the flow charts to make a **parkour** style map which players have to complete.

To build an oak staircase 3 blocks wide and 5 blocks tall:

`/js stairs(blocks.stairs.oak, 3, 5)`

Staircases do not have any blocks beneath them.

![hypothalamus_small](https://cloud.githubusercontent.com/assets/128456/11132490/17ac85fe-8988-11e5-8daf-c4e3992d1681.gif)

#### Hypothalamus Says 

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


#### ScriptCraft Reference
Get the full info on github from http://scriptcraftjs.org/

Shapes

 * box( blocks.material, width, height, depth ) - creates a solid box 
 * box0( blocks.material, width, height, depth ) - creates an empty box (with the insides hollowed out - perfect for dwellings.
 * box( blocks.material, width, height, depth ) - creates an empty box (with the insides hollowed out - perfect for dwellings.
 * cylinder( blocks.material, radius, height ) - creates cylinders, perfect for Chimneys.
 * cylinder0( blocks.material, radius, height ) - creates empty cylinders 
 * prism( blocks.material, width, depth ) - creates a Prism - good for roofs.

Just substitute 'block.material' for 'block.wool.red' or 'block.ice' or 'block.brick.red' type /js block. then use tab to see the different materials autocomplete in the command line

### Movement

The 'drone' is the invisible cursor that 'builds' things in minecraft; whatever block is highlighted as you look at it is the drone start position. You can combine commands by using a dot between commands. So /js box(block.ice).right(2).box(block.ice, 2,2,2) makes a single block of ice, moves 2 blocks to the right and makes a 2x2x2 block of ice


 * up( numberOfBlocks ) - moves the Drone Up. For example: up() will move the Drone 1 block up. You can tell it how many blocks to move if you want it to move more than one block.
 * down( numberOfBlocks ) - moves the Drone Down.
 * left( numberOfBlocks ) - moves the Drone Left.
 * right( numberOfBlocs ) - moves the Drone Right.
 * fwd( numberOfBlocs ) - moves the Drone Forward (away from the player).
 * back( numberOfBlocs ) - moves the Drone Back (towards the player)
i
 * turn( numberOfTurns ) - Turns the Drone Clock-wise (right). For example: turn() will make the Drone turn right 90 degrees. turn(2) will make the Drone turn twice so that it is facing in the opposite direction.


