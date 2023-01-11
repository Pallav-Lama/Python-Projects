blockedUsers = ["pallav", "Lhakpa"]
def checkBlockedUser(username):
        if(username in blockedUsers):
            return True
        else:
            return False
print(checkBlockedUser("palla"))