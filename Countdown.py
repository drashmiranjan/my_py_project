# This code is Time Countdown Code in python
import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60) #divmod is a function for divide the seconds in 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("countdown: ", timer)
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    try:
        total_seconds = int(input("Enter the time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter an integer value.")

                        # Thank you...
