import datetime
from playsound import playsound

alarm_hour = int(input('Enter Hour: '))
alarm_min = int(input('Enter Minutes: '))
alarm_ap = (input('am / pm : '))

if alarm_ap == 'pm':
    alarm_hour += 12

while True:
    if alarm_hour == datetime.datetime.now().hour and alarm_min == datetime.datetime.now().minute:
        print('playing...')
        playsound('sound.mp3')
        break
