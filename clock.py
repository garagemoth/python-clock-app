import os
import time
import winsound

os.system('cls' if os.name == 'nt' else 'clear')

def timerStart(timer_length):
    increment = timer_length // 4
    for x in range(abs(timer_length), 0, -1):
        if abs(timer_length) <= 3:
            print(f"{x} seconds remaining!")
        elif x % increment == 0:
            print(f"{x} seconds remaining!")
        time.sleep(1)
    print("Your timer is done!\n")
    try:
        winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
    except RuntimeError:
        pass

print("-----------------------------------")
print("       Your Personal Clock!")
print("-----------------------------------")
print(f"Today is: {time.ctime(time.time())}")
print("Type 'help' for a command list of actions!\n")

while True: 
    action = input("What would you like to do?\n> ")
    print()

    if action.strip().lower() == "help":
        print("Commands:")
        print("1. Time \t-\tShows current time")
        print("2. Timer\t-\tInitiates a timer that will alert you in (n) seconds")
        print("3. Stopwatch\t-\tInitiates a stopwatch that tracks your time")
        print("4. Exit \t-\tExits program")
        print()

    elif action.strip().lower() == "time":
        print(f"Current date and time: {time.ctime(time.time())}\n")

    elif action.strip().lower() == "timer":
        while True:
            try:
                timer_length = int(input("How long do you want your timer to be? (in seconds):\n> "))
                break
            except ValueError:
                print("Invalid input (no decimals, or letters)\n")

        print(f"\nI'll alert you when {abs(timer_length)} second/s has passed by!")
        timerStart(timer_length)

    elif action.strip().lower() == "stopwatch":
        time_started = time.time()
        stop_program = ""
        while stop_program != "stop":
            stop_program = input("Stopwatch initiated! Type \"stop\" to stop it!\n> ")
            print()
        if stop_program == "stop":
            time_stopped = time.time()
            total_time = time_stopped - time_started
            seconds = total_time % 60
            minutes = int(total_time / 60) % 60
            hours = int(total_time / 60 / 60)
            print(f"Your time was: {hours:02}:{minutes:02}:{seconds:05.2f}\n")

    elif action.strip().lower() == "exit":
        print("See ya!")
        break

    else:
        print("Invalid input, try again!\n")