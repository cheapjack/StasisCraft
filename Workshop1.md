# StasisCraft Workshop 1
## Visualising Homeostasis: Body Temperature
 
![stasiscraftdynmapsmall](https://cloud.githubusercontent.com/assets/128456/11134653/6ae6e364-8996-11e5-910b-b4cab7d953d9.png)

Uses Minecraft PC client version `1.7.9` running `Bukkit-1.7.2`


###Activity

To get to the StasisCraft zone you need to `/warp stasiscraft`

####Performing Thermoregulation

 * We are going to split into groups


 * CloudMaker01 - CloudMaker05 Temperature rising Hypothalamus group 
  * `tp skintemp1`

It's your job to be the stimulus in the system, in this case we are representing temperature through glass silos with giant flowchart labels. When the silo is full (top centre block) of sand it will be marked as **too hot** ie the Dermis and other parts of the nervous system will send signals to the **Hypothalamus** to react. 

 * CloudMaker06 - CloudMaker09 
  * `warp hair`

This team are effectively the **Hypothalamus** team and act out in the game the  autonomous nervous system's response to rises in temperature. This is the start of the negative feedback 'system'

The silo **SkinTemp1** triggers the dermis hair response; hair standing up conserves heat from the Dermis, if too hot the hair's in the dermis muscle is relaxed so they lay flat on the skin 


The silo **SkinTemp2** triggers the dermis vascular system response; blood vessels near the surface of the skin contract to keep blood away from the skin surface, to conserve heat,  if too hot the blood vessels in the upper dermis relax so the blood flows near the epidermis to lose heat. That's why pale coloured skin goes pink and red during exercise. 

 * Use `ScriptCraft` to make sweat response

###Hypothalamus Radio

RF-Craft is a CloudMaker resource that sends messages through concrete using the  868MHz amateur radio band as an alternative to managed WiFi

We are using the RF-Craft Buttons to trigger certain events:
 * RED - **Hypothalamus Alert** Builds a hypothalamus shaped redstone ore sphere as an alert
 * GREEN - **SkinTemp1 Silo Increase** Fills the SkinTemp1 silo with sand to visualise increase in temperature
 * YELLOW - **SkinTemp2 Silo Increase** Fills the SkinTemp2 silo with sand to visualise increase in temperature
 * BLUE - **Decrease Temperature** Removes sand from both silos to visualise decrease in temperature
 


