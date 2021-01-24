#As the title represents, the task here to write a python script that creat's an alarm clock. For this task i will be using the date time module in python to create an alarm clock and the sound library in python to play the alarm sound.

### Alarm clock with python

from datetime import datetime

from playsound import playsound
alarm_time=input('Enter the time of the alarm to be set :HH:MM:SS\n')

#Set the hour
alarm_hour=alarm_time[0:2]
#set the minute
alarm_minute=alarm_time[3:5]
#set the seconds
alarm_seconds=alarm_time[6:8]

alarm_period=alarm_time[9:11].upper()

print('Setting up alarm')

while True:
    now=datetime.now()
    current_hour=now.strftime("%I")
    current_minute=now.strftime("%M")
    current_seconds=now.strftime("%S")
    current_period=now.strftime("%p")

    if(alarm_period == current_period):
        if(alarm_hour == current_hour):
            if(alarm_minute == current_minute):
                if(alarm_seconds == current_seconds):
                    print("Wake up! Boss It's getting late")
                    playsound('police.mp3')
                    break