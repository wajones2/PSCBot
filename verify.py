
class Verify:
    def __init__(self):
        file = './docs/members.txt'
        self.emails = open(file, 'r').read().split()

        """Takes the dictionary from 'cleandata.py'"""
        from cleandata import CleanData
        self.cd = CleanData()
        self.cd.loadEmailPosition()
        self.posDict = self.cd.posDict

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


