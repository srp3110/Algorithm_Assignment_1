ticket = int(2000)

print('''
Enter 0 to 5 for following options:
0 -> Issue new ticket number
1 -> Assign first ticket in queue to Table 1
2 -> Assign first ticket in queue to Table 2
3 -> Assign first ticket in queue to Table 3
4 -> Assign first ticket in queue to Table 4
5 -> Quit program
''')

def whateva():
    print(f'''Ticket in queue: {queue}''')
    print(f'''Table assignment: {table_assign}''')

queue = []
table_assign = {
        "Table 1": "Not assigned",
        "Table 2": "Not assigned",
        "Table 3": "Not assigned",
        "Table 4": "Not assigned"
}
whateva()
option = input('Enter your option: ')
print(option)