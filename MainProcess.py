from Cards import Cards
from Cards import CreditCard

def rebatesTransaction(year, month, type):
    t_file = open('static/file/TotalRebates', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')

        if list[0] == year and list[1] == month and list[2] == type:
           total += float(list[3])
    return total


def processAccounts():
    usersList = []
    user_file = open('static/file/creditCards', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        s = CreditCard(list[0], list[1])

        usersList.append(s)
    return usersList

def processAccountss():
    usersLists = []
    userfile = open('static/file/ocbcCard', 'r')
    for i in userfile:
        list = i.split(',')
        a = CreditCard(list[0], list[1])

        usersLists.append(a)
    return usersLists
