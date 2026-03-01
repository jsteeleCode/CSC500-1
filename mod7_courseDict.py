#create a dict where we have 5 keys that name the college courses
courseDict = {
    #give each key a room number as a value, as well as an instructor name and the meeting time for the course
    "CS101": {"room": "3004", "instructor": "Haynes", "time": "8:00 a.m."},
    "CS102": {"room": "4501", "instructor": "Alvarado", "time": "9:00 a.m."},
    "CS103": {"room": "6755", "instructor": "Rich", "time": "10:00 a.m."},
    "NET110": {"room": "1244", "instructor": "Burke", "time": "11:00 a.m."},
    "COM241": {"room": "1411", "instructor": "Lee", "time": "1:00 p.m."}
}

    #run a method that asks the user and prints the info
def main():
    courseNumber = input("Enter a course number: ")
    if courseNumber in courseDict:
        print(f"Course: {courseNumber}")
        print(f"Room: {courseDict[courseNumber]['room']}")
        print(f"Instructor: {courseDict[courseNumber]['instructor']}")
        print(f"Time: {courseDict[courseNumber]['time']}")

#call main function
main()

#end of program