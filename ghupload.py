import time
from datetime import date
tlist = []


print("Note! This code needs to be continuously run! ")


while True:
    date = date.today()
    print("") ## move these later
    print("")
    print("Menu:")
    print("")
    print("Current assignments:")
    if tlist == []:
        print("  All assignments are complete!")
        print("")
        print("Type 'new' to create a new task.")
        op = input("")
    else:
        for ip in range(0, len(tlist)):
            print(str(ip + 1) + " - " + tlist[ip])
        print("")
        print("Type in a task's number to select it, or type 'new' to add a new task.")
        op = input("")
    print("")
    
    if op == 'new':
        tlist.append(input("Task name?"))
        
    else:
        if (int(op) - 1) in range(0, len(tlist)):
            print("Task " + op + " of " + str(len(tlist)) + ":")
            print(tlist[int(op) - 1])
            print("What would you like to do?")
            print("Type 'done' to complete task, or 'time' to time it.") ## add timer!!
            op2 = input("")
            if op2 == 'done':
                del tlist[int(op) - 1]
            elif op2 == 'time':
                timer = input("How many minutes would you like to time?  ")
                timer = int(timer)
                i1 = input("Press Enter to begin timing.")
                for p in range(0, timer):
                    print(str(p) + " minutes elapsed, " + str(timer - p) + " minutes remaining!")
                    time.sleep(60)
                print("Timer done!")
                q = input("Would you like to comeplete this task? (type 'yes' or 'no'.)  ")
                if q == 'yes':
                    del tlist[int(op) - 1]
