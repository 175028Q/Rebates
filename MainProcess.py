from Cards import Cards

def rebatesTransaction(year, month, type):
    t_file = open('file/TotalRebates.txt', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')

        if list[0] == year and list[1] == month and list[2] == type:
            total += float(list[3])
    return total
