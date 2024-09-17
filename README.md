
# PSCBot

PSCBot is a Discord bot that verifies if a user is a member in the organization Pathways to STEM Careers at the University of Houston-Clear Lake as well as whether or not they have a paid position.

# Installation

This program requires the 'discord.py' package, which is installed via pip by running the 'firstrun' executive. Below is the installation process:

 ```
 git clone https://github.com/wajones2/PSCBot.git
 cd PSCBot
 ./firstrun
 ```

 # Operation

 After installation, you must enter your Discord bot token in 'main.py' then execute ```./start```. Below explains each major part of the code:

 **newclean**

After pasting list of emails in the 'repeatedEmails.txt' file, execute ```./newclean```, which runs 'newclean.py', which runs the part of the CleanData class in 'cleandata.py' that updates the text file containing the list of emails as well as the json file with emails and positions. Will clean this up a bit on the next commit. Below is what occurs during each execution of 'newclean':

**cleandata.py**

In case the list of emails contains repeated emails, the class 'CleanData' contains the function 'singleEmail' writes one copy of each email to the file 'members.txt'.

The function 'emailPosition' creates an dictionary with emails and positions and writes it to the file 'member_position.json'.

These two functions are currently not used in the operation of the bot and must be performed prior to running the bot. 


**verify.py**

This file contains the 'Verify' class with the two functions that correspond to each bot command:

'memberVerify' checks if an email is in 'members.txt', which is put into a list during the initialization of the Verify class. If so, the user is granted the 'Member' role.

'positionVerify' checks if an email is in the dictionary, created also during initalization. If so, the user is granted the role that corresponds to the email in the email in the dictionary and their position in the PSC organization.

**main.py**

This is the file executed to run the bot and contains the bot commands. You must enter your bot token in this file for the program to work.






