import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up! Focus session complete.")

if __name__ == "__main__":
    focus_time = int(input("Enter the duration of focus session in minutes: "))
    focus_timer(focus_time)
