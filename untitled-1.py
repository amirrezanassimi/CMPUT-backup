from datetime import date, datetime

book_data = open('books.txt','r')
member_data = open('members.txt','r')
output = open('summary.txt','w')
MAX_DAYS = 90
DAILY_CHARGE = 0.25
#TODAY = datetime.now().date()
TODAY = date(2018,1,19)

member_list = member_data.read().split('\n')[:-1]
member_list = sorted([a.split(',') for a in member_list])
book_list = book_data.read().split('\n')[:-1]
book_list = [a.split(';') for a in book_list]

# CONVERT BOOK PRICE TO FLOAT AND DATE TO DATETIME OBJECT
for i in book_list:
    i[1] = float(i[1])
    y, m, d = [int(a) for a in i[2].split('/')]
    i[2] = date(y,m,d)

# CREATE A DICTIONARY W/ EACH MEMBERS PHONE NUMBER AS KEY AND LIST AS ITEM
member_dict = {}
for i in member_list:
    # FIRST ITEM IN DICTIONARY IS MEMBER NAME
    member_dict[i[0]] = [i[1]]
    # SECOND ITEM IN DICTIONARY IS TOTAL OWING
    member_dict[i[0]].append(0.00)

# ITERATE THROUGH BOOK LIST AND UPDATE MEMBER_DICT
for i in book_list:
    book_code = i[0]
    cost = i[1]
    days_total = (TODAY-i[2]).days
    late_charge = days_total * DAILY_CHARGE
    # GET PHONE # FROM BOOK LIST (i[-1]) & UPDATE TOTAL MEMBER OWING IN DICT
    member_dict[i[-1]][1] += cost * (days_total > MAX_DAYS) + late_charge
    # ADD BOOK CODE AND TOTAL DAYS TO MEMBERS KEY LIST
    member_dict[i[-1]].append([book_code, days_total])

# GET TOTAL OWING FROM ALL MEMBERS
total_dues = 0
for i in member_dict:
    total_dues += member_dict[i][1]

# TAKES IN A DICTIONARY & KEY AND CREATES A LINE OF INFO
def create_line(key, dictionary):
    number = '({}) {} {}'.format(key[0:3],key[3:6],key[6:])
    name = '{:30}'.format(dictionary[key][0])
    owing = '${:7.2f}'.format(dictionary[key][1])
    book_lines = ''
    for i in dictionary[key][2:]:
        book_lines += '[{}]({} days); '.format(i[0],i[1])
    return '|'+number+'|'+name+'|'+owing+'|'+book_lines+'\n'

# PRINT TABLE
spacer = '+--------------+------------------------------+--------+\n'
header = '| Phone Number | Name                         | Due    |\n'
footer = '| Total Dues   |'+' '*28+'${:10.2f}|\n'.format(total_dues)
output.write(spacer); output.write(header); output.write(spacer)
for i in member_list:
    output.write(create_line(i[0], member_dict))
output.write(spacer); output.write(footer); output.write(spacer)
output.close()