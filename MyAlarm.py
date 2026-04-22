import datetime
import time
import winsound

def convert_spoken_time(spoken):
    spoken = spoken.strip().replace(" ", "")
    
    spoken = spoken.lower().replace(":", "")
    
    am_pm = ""
    if "am" in spoken:
        am_pm = "AM"
        spoken = spoken.replace("am", "")
    elif "pm" in spoken:
        am_pm = "PM"
        spoken = spoken.replace("pm", "")
    
    spoken = spoken.zfill(4)
    
    hours = spoken[:2]
    minutes = spoken[2:]
    
    if not am_pm:
        if int(hours) < 7:
            am_pm = "PM"
        else:
            am_pm = "AM"
    
    return f"{int(hours)}:{minutes} {am_pm}"


def alarm(Timing):
    try:
        Timing = convert_spoken_time(Timing)
        print(f"Converted time: {Timing}")
        
        alttime = datetime.datetime.strptime(Timing, "%I:%M %p")

        Horeal = alttime.hour
        Mireal = alttime.minute

        print(f"Done, alarm is set for {Timing}")

        while True:
            now = datetime.datetime.now()

            if Horeal == now.hour and Mireal == now.minute:
                print("Alarm is running!")

                for _ in range(5):
                    winsound.Beep(1000, 500)

                break

            time.sleep(30)

    except Exception as e:
        print(f"Error: {e}")
        print("Invalid time format. Please try again")