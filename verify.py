

class Verify:
    def __init__(self):
        file = './docs/members.txt'
        self.emails = open(file, 'r').read().split()

    def memberVerify(self, email):

    
        if email.lower() in self.emails:
             message = "User is a member of PSC"
             print(f"\n\n{message}")
             return True, message
        else:
            message = "User is not a member of PSC"
            print(f"\n\n{message}")
            return False, message


