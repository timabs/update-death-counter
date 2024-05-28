import os
import keyboard

counter_file = 'death_counter.txt'

if not os.path.exists(counter_file):
    with open(counter_file, 'w') as file:
        file.write('Death Counter: 0')

def read_counter():
    with open(counter_file, 'r') as file:
        content = file.read().strip()
        count = int(content.split(": ")[1])
    return count

def update_counter(count):
    with open(counter_file, 'w') as file:
        file.write(f'Death Counter: {count}')

def increment():
    count = read_counter()
    count += 1
    update_counter(count)
    print(f'Death count updated: {count}')

def decrement():
    count = read_counter()
    count -= 1
    update_counter(count)
    print(f'Death count updated: {count}')

keyboard.add_hotkey('+', increment)
keyboard.add_hotkey('-', decrement)
print("Press the numpad minus key to increment the death counter. Press ESC to quit.")
print("Press the numpad plus key to increment the death counter. Press ESC to quit.")
keyboard.wait('esc')
