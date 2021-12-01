from datetime import datetime
def time_conversion(time):
    try:
        time_object = datetime.strptime(time, '%H:%M')
        return time_object
    except ValueError:
        print("Sorry. This program does not recognise the time format entered.\n\nBye.")
time = input("time? ")
print(time_conversion(time))