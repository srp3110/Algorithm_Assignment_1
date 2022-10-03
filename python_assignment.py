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

def add_ticket(ticket):
    queue.append(ticket)

def table_queue(table_number):
    if len(queue) == 0:
        print("ERROR, ENTER '0' TO ISSUE NEW TICKET NUMBER!!!")
    else:
        new_table = "Table" + table_number
        table_assign[new_table] = queue.pop(0)

queue = []
table_assign = {
        "Table 1": "Not assigned",
        "Table 2": "Not assigned",
        "Table 3": "Not assigned",
        "Table 4": "Not assigned"
}

while True:
    whateva()
    option = input('Enter your option: ')
    print("")
    
    if option == "0":
        ticket += 1
        add_ticket(ticket)

    elif option == "1" or option == "2" or option == "3" or option == "4":
        table_queue(option)
    
    elif option == "5":
        print("Quitting program...")
        break

    else:
        print("Invalid option, try again...")