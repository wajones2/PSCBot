import json

class Verify:
    def __init__(self):
        """'members.txt' is a list of emails with one on each line"""
        file = '../docs/members.txt'
        self.emails = open(file, 'r').read().split()

        """'member_position.json' is a dictionary with the format {'EMAIL': 'POSITION'}"""
        posFile = open('../docs/member_position.json', 'r')
        self.posDict = json.load(posFile)
        posFile.close()

    def memberVerify(self, email):

        if email.lower() in self.emails:
             message = "User is a member of PSC"
             print(f"\n\n{message}")
             return True, message
        else:
            message = "User is not a member of PSC"
            print(f"\n\n{message}")
            return False, message

    def positionVerify(self, email):
        if email.lower() in self.posDict:
            member = [email.lower(), self.posDict[email.lower()]]
            return member
        else:
            return False
