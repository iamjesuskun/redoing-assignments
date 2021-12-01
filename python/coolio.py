import sys
from datetime import datetime
Room1 = [["The Shining.", "1980.", "2h 26m.", "10:00.", "Room 1"],
["Your Name.", "2016.", "1h 52m.", "13:00.", "Room 1"],
["Fate/Stay Night: Heaven's Feel - III. Spring Song.", "2020.", "2h 0m.", "15:00.", "Room 1"],
["The Night Is Short, Walk on Girl.", "2017.", "1h 32m.", "17:30.", "Room 1"],
["The Truman Show.", "1998.", "1h 47m.", "19:30.", "Room 1"],
["Genocidal Organ.", "2017.", "1hr 55m.", "21:45.", "Room 1"]]

Room2 = [["Jacob's Ladder.", "1990.", "1h 56m.", "10:00.", "Room 2"],
["Parasite.", "2019.", "2h 12m.", "12:15.", "Room 2"],
["The Dark Knight.", "2008.", "2h 32min.", "14:45.", "Room 2"],
["Blade Runner 2049.", "2017.", "2h 44m.", "17:45.", "Room 2"],
["The Mist.", "2007.", "2h 6m.", "21:00.", "Room 2"],
["Demon Slayer: Mugen Train.", "2020.", "1h59min.", "23:20.", "Room 2"]]

Room3 = [["The Matrix.", "1999.", "2h 16m.", "10:00.", "Room 3"],
["Inception.", "2010.", "2h 42m.", "11:30.", "Room 3"],
["Shutter Island.", "2010.", "2h 19m.", "14:30.", "Room 3"],
["Soul.", "2020.", "1hr 40m.", "17:00.", "Room 3"],
["Mrs. Brown.", "1997.", "1h 41min.", "19:00.", "Room 3"],
["Peppa Pig: Festival of Fun.", "2019.", "1h 8min.", "21:00.", "Room 3"],
["Titanic.", "1997.", "3h 30min.", "22:15.", "Room 3"]]
ROOMS = [Room1, Room2, Room3]
greeting = ["-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n",
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
"~ Welcome to Pizzaz cinema ~\n",
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
"-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"]

def time_conversion(time):
    try:
        time_object = datetime.strptime(time, '%H:%M')
        return time_object
    except ValueError:
        print("Sorry. This program does not recognise the time format entered.\n\nBye.")

def get_movie(title):
    for room in ROOMS:
        for movie in room:
            if title.lower() in movie[0].lower():
                return movie
    check = input("Sorry, we could not find that movie. Enter Y to try again or N to quit. ")
    check = check.lower()
    if check == "y":
        movie = input("What is the name of the movie you want to watch? ")    
        get_movie(movie)
    elif check == "n":
        exit()

def get_popcorn(people, group):
    if group == False:
        while True:
            size = input("You want popcorn. What size Small, Medium or Large? (S/M/L)")
            if size.lower() != "s" or size.lower() != "m" or size.lower() != "l":
                continue
            else:
                return size.lower()
    else:
        while True:
            size = input("Person %d want popcorn. What size Small, Medium or Large? (S/M/L)".format(people))
            if size.lower() != "s" or size.lower() != "m" or size.lower() != "l":
                continue
            else:
                return size.lower()

def get_transaction(movie_time, popcorn, group):
    pass

def show(ls):
    if len(ls) < 3:
        print("Sorry. This program does not recognise the time format entered.\n\nBye.")    
    else:
        time = ls[2]
        if len(list(time)) > 5 or len(list(time)) < 5:
            print("Sorry. This program does not recognise the time format entered.\n\nBye.")
        time = time_conversion(time)
        for room in ROOMS:
            for j in range(len(room)):
                convert = room[j][3].replace(".","")
                if time_conversion(convert) >= time:
                    line = ""
                    for things in room[j]:
                        line += things + " "
                    print(line)
        print("\nBye.")
                    

def book():
    movie = input("What is the name of the movie you want to watch? ")
    movie = get_movie(movie)
    while True:
        popcorn = input("Would you like to order popcorn? Y/N ")
        if popcorn.lower() == "y":
            popcorn = [get_popcorn(1)]
        elif popcorn.lower() == "n":
            break
        else:
            continue
    print("The seat number for person 1 is #17\n")
    return [movie[3],popcorn, False]

def group():
    pass

def main(ls):
    for line in greeting:
        print(line)
    if len(ls) < 2:
        print("Sorry. This program does not recognise the switch options.\n\nBye.")
    elif ls[1] == "--show":
        show(ls)

    elif ls[1] == "--book":
        book()
    elif ls[1] == "--group":
        group() 

if __name__ == "__main__":
    main(sys.argv)