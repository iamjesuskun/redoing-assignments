# from datetime import datetime
# def time_conversion(time):
#     try:
#         time_object = datetime.strptime(time, '%H:%M')
#         return time_object
#     except ValueError:
#         print("Sorry. This program does not recognise the time format entered.\n\nBye.")
# time = input("time? ")
# print(time_conversion(time))
Room1 = {"name":"Room 1", "movies":[["The Shining.", "1980.", "2h 26m.", "10:00.", "Room 1"],
["Your Name.", "2016.", "1h 52m.", "13:00.", "Room 1"],
["Fate/Stay Night: Heaven's Feel - III. Spring Song.", "2020.", "2h 0m.", "15:00.", "Room 1"],
["The Night Is Short, Walk on Girl.", "2017.", "1h 32m.", "17:30.", "Room 1"],
["The Truman Show.", "1998.", "1h 47m.", "19:30.", "Room 1"],
["Genocidal Organ.", "2017.", "1hr 55m.", "21:45.", "Room 1"]],
"size":35}

Room2 = {"name":"Room 2", "movies":[["Jacob's Ladder.", "1990.", "1h 56m.", "10:00.", "Room 2"],
["Parasite.", "2019.", "2h 12m.", "12:15.", "Room 2"],
["The Dark Knight.", "2008.", "2h 32min.", "14:45.", "Room 2"],
["Blade Runner 2049.", "2017.", "2h 44m.", "17:45.", "Room 2"],
["The Mist.", "2007.", "2h 6m.", "21:00.", "Room 2"],
["Demon Slayer: Mugen Train.", "2020.", "1h59min.", "23:20.", "Room 2"]],
"size":136}

Room3 = {"name":"Room 3","movies": [["The Matrix.", "1999.", "2h 16m.", "10:00.", "Room 3"],
["Inception.", "2010.", "2h 42m.", "11:30.", "Room 3"],
["Shutter Island.", "2010.", "2h 19m.", "14:30.", "Room 3"],
["Soul.", "2020.", "1hr 40m.", "17:00.", "Room 3"],
["Mrs. Brown.", "1997.", "1h 41min.", "19:00.", "Room 3"],
["Peppa Pig: Festival of Fun.", "2019.", "1h 8min.", "21:00.", "Room 3"],
["Titanic.", "1997.", "3h 30min.", "22:15.", "Room 3"]],
"size": 42}
print(Room3["size"])