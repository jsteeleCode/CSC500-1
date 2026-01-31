#ask user for current time in hours
currentHour = int(input("Enter the current hour (0-23): "))

#ask user for alarm time in hours
alarmHour = int(input("Enter the alarm hour (0-23): "))

#calculate hours until alarm
if alarmHour >= currentHour:
    hoursUntilAlarm = alarmHour - currentHour
else:
    hoursUntilAlarm = (24 - currentHour) + alarmHour

#display hours until alarm
print("The alarm will go off in", hoursUntilAlarm, "hours.")

#end of program