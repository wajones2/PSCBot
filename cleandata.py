

class CleanData:
    def __init__(self):
        import json
        self.json = json
        pass

    def singleEmail(self):
        """Takes emails from 'repeatedEmails.txt' and writing to 'members.txt' 
            without repeated emails that are all lowercase, assuming the list
            is one email per line."""

        file = open('./docs/repeatedEmails.txt', 'r')
        file = file.read().split()

        newlist = []
        for email in file:
            if email in newlist:
                pass
            else:
                newlist.append(email)

        newfile = open('./docs/members.txt', 'w')
        for email in newlist:
            newfile.write(email.lower() + '\n')
        newfile.close()


    def emailPosition(self):

        """Takes emails and organization positions from 'positions.txt' 
            and writes to a dictionary formatted as {EMAIL: POSITION}
            then writes to a json file."""
        
        file  = open('./docs/positions.txt', 'r')

        pos = file.read().split('\n')

        pos_dict = {}

        for member in pos:
            member = member.split('\t')
            pos_dict[member[0].lower()] = member[1]

        # Write dictionary to json file
        with open('./docs/member_position.json', 'w') as fp:
            self.json.dump(pos_dict, fp)

    def loadEmailPosition(self):
        
        """Gets the email-position dictionary from 'member_position.json'
            and writes to a dictionary to be used by the bot."""
        
        # Convert json file to Python dictionary (used in main.py)
        file = open('./docs/member_position.json', 'r')
        self.posDict = self.json.load(file)
        file.close()