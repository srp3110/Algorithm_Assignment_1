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

while True:
    whateva()
    option = input('Enter your option: ')
    print("")
    
    if option == "0":
        ticket += 1
        queue.append(ticket)

    elif option == "1":
        if len(queue) == 0:
            print("ERROR, ENTER '0' TO ISSUE NEW TICKET NUMBER!!!") 
            #make table assign disappear but keep whateva
        else:
            ticket = queue.pop(0)
            table_assign["Table 1"] = ticket
            print(table_assign)
    
    elif option == "2":
        if len(queue) == 0:
            print("ERROR, ENTER '0' TO ISSUE NEW TICKET NUMBER!!!")
        else:
            ticket = queue.pop(0)
            table_assign["Table 2"] = ticket
            print(table_assign)
    
    elif option == "3":
        if len(queue) == 0:
            print("ERROR, ENTER '0' TO ISSUE NEW TICKET NUMBER!!!")
        else:
            ticket = queue.pop(0)
            table_assign["Table 3"] = ticket
            print(table_assign)
    
    elif option == "4":
        if len(queue) == 0:
            print("ERROR, ENTER '0' TO ISSUE NEW TICKET NUMBER!!!")
        else:
            ticket = queue.pop(0)
            table_assign["Table 4"] = ticket
            print(table_assign)
    
    elif option == "5":
        print("Quitting program...")
        break

    else:
        if len(queue) == 0:
            print("ERROR, ENTER '0' TO ISSUE NEW TICKET NUMBER!!!")
        else:
            print("Invalid option, try again...")