
# PSCBot

PSCBot is a Discord bot that verifies if a user is a member in the organization Pathways to STEM Careers at the University of Houston-Clear Lake as well as whether or not they have a paid position.

# Installation

This program requires the 'discord.py' package, which can be installed via pip. Below is the installation process:

 ```
 git clone https://github.com/wajones2/PSCBot.git
 cd PSCBot
 pip install discord.py
 ```

 # Operation


**cleandata.py**


In case the list of emails contains repeated emails, the class 'CleanData' contains the function 'singleEmail' writes one copy of each email to the file 'members.txt'.

The function 'emailPosition' creates an dictionary with emails and positions and writes it to the file 'member_position.json'.

These two functions are currently not used in the operation of the bot and must be performed prior to running the bot. I may eventually write this using sqlite so that it will automatically be executed only once upon running the bot.


**verify.py**

Will update on next commit






