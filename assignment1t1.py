from datetime import date, datetime

books = open('books.txt','r')
members = open('members.txt','r')
summary = open('summary.txt','w')
limitDays = 90
cost  = 0.25
today = datetime.now().date()
membersList = members.read().split('\n')[:-1]
#print(membersList)
membersList = sorted([a.split(',') for a in membersList])
print(membersList)
booksList = books.read().split('\n')[:-1]
booksList = [a.split(';') for a in booksList]
print(booksList)
for i in booksList:
    i[1] = float(i[1])
    y, m, d = [int(a) for a in i[2].split('/')]
    i[2] = date(y,m,d)
membersDic = {}
for i in membersList:
    membersDic[i[0]] = [i[1]]
    membersDic[i[0]].append(00.00)
for i in booksList:
    bookID = i[0]
    price = i[1]
    daysTotal = (today-i[2]).days
    penalty = daysTotal * cost 
    membersDic[i[-1]][1] += price * (daysTotal > limitDays) + penalty
    membersDic[i[-1]].append([bookID, daysTotal])
totalDues = 0.0
for i in membersDic:
    totalDues += membersDic[i][1]
def create_table(key, dictionary):
    phoneNumber = '({}) {} {}'.format(key[0:3],key[3:6],key[6:])
    name = '{:30}'.format(dictionary[key][0])
    owing = '${:7.2f}'.format(dictionary[key][1])
    book_lines = ''
    for i in dictionary[key][2:]:
        book_lines += '[{}]({} days); '.format(i[0],i[1])
    return '|'+phoneNumber+'|'+name+'|'+owing+'|'+book_lines+'\n'
border = '+--------------+------------------------------+--------+\n'
first = '| Phone phoneNumber | Name                         | Due    |\n'
scound = '| Total Dues   |'+' '*28+'${:10.2f}|\n'.format(totalDues)
summary.write(border); summary.write(first); summary.write(border)
for i in membersList:
    summary.write(create_table(i[0], membersDic))
summary.write(border); summary.write(scound); summary.write(border)
summary.close()