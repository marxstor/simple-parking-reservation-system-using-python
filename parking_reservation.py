# parking reservation system

# global variables that stores the reservation values entered by the user
f = open("reservertion.txt", "r")
records = str(f.read())

#check if reservation.txt is blank/null after removing whitespaces
if records.strip():
    # eval is used to executes a string into a python expression
    # converts string records into python dictionary
    reservations = eval(records)
else:
    # if reservation.txt is blank
    reservations = {}
f.close()

def mainFunc():
    print("""------------------------------------------------------------------------------
                            PARKING RESERVATION SYSTEM
                                   SYSTEM MENU:

                            A - View All Reservations
                            B - Make Reservation
                            C - Update Reservation
                            D - Cancel Reservation
                            E - Generate Report
                            F - Exit

------------------------------------------------------------------------------""")

    action = input("Please enter your selected option: ")

    if action == "A" or action == "a":
        viewAllReservation()
    elif action == "B" or action == "b":
        makeReservation()
    elif action == "C" or action == "c":
        updateReservation()
    elif action == "D" or action == "d":
        cancelReservation()
    elif action == "E" or action == "e":
        generateReports()
    elif action == "F" or action == "f":
        confirm = str(input("Are you sure you want to exit? (Y/N) : "))
        if confirm == "Y" or confirm == "y":
            print("Bye!")
        elif confirm == "N" or confirm == "n":
            mainFunc()
        else:
            print("Invalid input")
            mainFunc()
    else:
        print("Invalid Value. Please select only from the menu.\n")
        mainFunc()

def viewAllReservation():
    print("------------------------------------------------------------------------------")
    print("                             Reservation List".upper())
    print("#    Date    Time    Name    Vehicle Type    Plate Number")
    for res_no, x in reservations.items():
        print(f"{res_no}    {x['Date']}        {x['Time']}      {x['Name']}        {x['Vehicle Type']}            {x['Plate']}")

    print("B - Back")
    print("------------------------------------------------------------------------------")
    back = str(input("Enter action: "))
    # condition to go back at the main dashboard which is the mainFunc()
    if back == "B" or back == "b":
        mainFunc()
    else:
        print("Invalid input")
        viewAllReservation()

def makeReservation():
    res_no = int(input("Reservation No. : "))
    name = str(input("Enter your name: "))
    date = str(input("Enter date (yyyy-mm-dd): "))
    time = str(input("Enter time: "))
    v_type = str(input("Enter your vehicle type: "))
    plate = str(input("Enter your vehicle plate number: "))

    # adding reservation in reservations dictionary
    reservations[res_no] = {"Name" : name, "Date" : date, "Time" : time, "Vehicle Type" : v_type, "Plate" : plate}
    # return feedback
    print("Reservation has been successfully created.".upper())

    # save the updated reservation
    f = open("reservertion.txt", "w")
    f.write(str(reservations))
    f.close()

    mainFunc()

def updateReservation():
    try:
        reservation_no = int(input("Enter reservation number: "))
        # check if reservation number entered by the user is in the reservations dictionary
        if reservation_no in reservations:
            reservation = reservations[reservation_no]
            print("------------------------------------------------------------------------------")
            print("                               Update Reservation".upper())
            print(f"\n# Date Time Name Vehicle Type Plate Number")
            print(f'{reservation_no} {reservation["Name"]} {reservation["Date"]} {reservation["Time"]} {reservation["Vehicle Type"]} {reservation["Plate"]}')

            print("""Select the date to update: 
[N]ame
[D]ate
[T]ime
[V]ehicle Type
[P]late Number
[B] - back""")
            print("------------------------------------------------------------------------------")
            update = str(input("Enter your selected action: "))
            update.upper()

            # return text variable when one of the condition is performed
            text = "Reservation successfully updated!".upper()
            if update == "N":
                # updating the old value key name
                reservation["Name"] = str(input("Enter new name: "))
                f = open("reservertion.txt", "w")
                f.write(str(reservations))
                f.close()
                print(text)
                mainFunc()
            elif update == "D":
                reservation["Date"] = str(input("Enter new date: "))
                f = open("reservertion.txt", "w")
                f.write(str(reservations))
                f.close()
                print(text)
                mainFunc()
            elif update == "T":
                reservation["Time"] = str(input("Enter new time: "))
                f = open("reservertion.txt", "w")
                f.write(str(reservations))
                f.close()
                print(text)
                mainFunc()
            elif update == "V":
                reservation["Vehicle Type"] = str(input("Enter new vehicle type: "))
                f = open("reservertion.txt", "w")
                f.write(str(reservations))
                f.close()
                print(text)
                mainFunc()
            elif update == "P":
                reservation["Plate"] = str(input("Enter new plate number: "))
                f = open("reservertion.txt", "w")
                f.write(str(reservations))
                f.close()
                print(text)
                mainFunc()
            elif update == "B":
                # for going back to the main dashboard
                mainFunc()
            else:
                # if user entered invalid input print invalid input and call again the update function
                print("Invalid input")
                updateReservation()

        else:
            print("Invalid reservation number.")
    except ValueError:
        # print this error when user entered a sting instead of integer
        print("Invalid reservation number.")
        mainFunc()


def cancelReservation():
    try:
        reservation_no = int(input("Enter reservation number: "))
        # check if the reservation number entered by the user is in the dictionary reservations
        if reservation_no in reservations:
            reservation = reservations[reservation_no]
            print("------------------------------------------------------------------------------")
            print("                               Cancel Reservation".upper())
            print(f"\n# Date Time Name Vehicle Type Plate Number")
            print(f'{reservation_no} {reservation["Name"]} {reservation["Date"]} {reservation["Time"]} {reservation["Vehicle Type"]} {reservation["Plate"]}')

            print("------------------------------------------------------------------------------")
            confirmDel = input("Are you sure you want to cancel this reservation? (Y/N): ").upper()

            if confirmDel == "Y":
                del reservations[reservation_no]
                print("Reservation successfully cancelled.".upper())

                # Save the updated reservations back to the file
                f = open("reservertion.txt", "w")
                f.write(str(reservations))
                f.close()
                mainFunc()
            else:
                print("Cancellation aborted.".upper())
                mainFunc()
        else:
            print("Reservation not found".upper())
            mainFunc()
    except ValueError:
        # print this error when user entered a sting instead of integer
        print("Invalid reservation number.")
        mainFunc()


def generateReports():
    date = str(input("Enter date: "))
    print("------------------------------------------------------------------------------")
    print(f"                      Reservation Report: {date}".upper())
    print(f"\n# Date Time Name Vehicle Type Plate Number")

    # variables for the number for reservations and vehicle types
    type1 = 0
    type2 = 0
    totalReserv = 0
    for res_no, reservation in reservations.items():
        # return all the matching reservation base on the date entered by the user
        if reservation["Date"] == date:
            print(f'{res_no} {reservation["Name"]} {reservation["Date"]} {reservation["Time"]} {reservation["Vehicle Type"]} {reservation["Plate"]}')
            totalReserv +=1

        if reservation["Vehicle Type"] == "1":
            type1 +=1
        elif reservation["Vehicle Type"] == "2":
            type2 +=1
    print(f"\nTotal number of Type 1 reservations: {type1}")
    print(f"Total number of Type 2 reservations: {type2}")
    print(f"Total number reservations: {totalReserv}")

    print("B - Back")
    print("------------------------------------------------------------------------------")
    action = str(input("Enter action: ".upper()))
    if action == "B":
        mainFunc()
    else:
        mainFunc()

mainFunc()
