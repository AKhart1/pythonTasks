import time
def setAlarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            return "Alarm! Wake up!"
        time.sleep(30)

print(setAlarm("11:38"))