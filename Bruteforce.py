import time
import pyautogui
import keyboard

def bruteforce():
    for brute in range(1001, 10000):
        yield str(brute)
        time.sleep(0.7)

def Keyboard(brute_value):
    pyautogui.write(brute_value)
    pyautogui.press('enter')

# Create a generator for the brute force values
brute_gen = bruteforce()

while True:
    try:
        # Get the next brute force value
        brute_value = next(brute_gen)
        print(brute_value)  # This is optional, for debugging
        Keyboard(brute_value)
        
        # Optional: Add a break condition or a way to stop the loop
        if keyboard.is_pressed('q'):  # Stop the loop if 'q' is pressed
            print("Stopped by user.")
            break
    except StopIteration:
        # If the generator is exhausted, stop the loop
        print("Brute force range exhausted.")
        break
