import tkinter as tk
from tkinter import font
import pydirectinput
import time
import os
import keyboard
import pyautogui
import mss
import numpy as np
import threading

# ==============================================================================
# --- SETTINGS ---
# ==============================================================================

IMAGE_FOLDER = 'Pic'
# Speed of repeated key presses. Safe values are between 0.1 (slow) and 0.02 (very fast).
KEY_PRESS_INTERVAL_SECONDS = 0.005
# Image recognition confidence. Start with 0.8. If it fails, try 0.75. 0.95 is too high.
IMAGE_CONFIDENCE = 0.95

# Image to close the game
CLOSE_GAME_IMAGE = 'close.png'

# --- SEARCH AREA FOR ACTIONS (UPDATE WITH YOUR VALUES!) ---
ACTION_SEARCH_REGION = {
    "left": 906,
    "top": 430,
    "width": 103,
    "height": 103
}

# --- SEARCH AREA FOR THE CLOSE IMAGE (UPDATE!) ---
CLOSE_SEARCH_REGION = {
    "left": 938,
    "top": 757,
    "width": 45,
    "height": 45
}

# ==============================================================================
# --- SCRIPT ---
# ==============================================================================

# --- Global Control Variables ---
is_running = False
should_exit = False
close_search_error_logged = False
cycle_counter = 0 # NEW: Cycle counter
cycle_counter_hung = 0

# --- HELPER FUNCTIONS ---
def press_key_for_duration(key, duration):
    """Repeatedly presses a key for a duration, allowing for interruption."""
    start_time = time.time()
    while time.time() - start_time < duration:
        if not is_running or should_exit: return False
        pydirectinput.press(key)
        time.sleep(KEY_PRESS_INTERVAL_SECONDS)
    return True

def wait_for_duration(duration):
    """Waits for a duration, allowing for interruption."""
    start_time = time.time()
    while time.time() - start_time < duration:
        if not is_running or should_exit: return False
        time.sleep(0.1)
    return True

# --- BOT LOGIC ---
def bot_loop():
    """This function contains the main bot loop."""
    global is_running, should_exit, close_search_error_logged, cycle_counter, cycle_counter_hung
    with mss.mss() as sct:
        while not should_exit:
            if is_running:
                
                print(f"Checking... (Cycle: {cycle_counter})")
                cycle_counter_hung +=1
                print("cycle counte hung", cycle_counter_hung)
                if cycle_counter_hung >100:
                    pyautogui.hotkey('alt', 'f4')
                    time.sleep(1)
                    pyautogui.hotkey('alt', 'f4')
                    time.sleep(1)
                    print("To cancel the shutdown, open CMD and type: shutdown /a")
                    os.system('shutdown /s /t 5')
                    time.sleep(1)
                    exit_script()
                
                # --- NEW ACTION EVERY 3 CYCLES ---
                
                # --- END OF NEW ACTION ---

                # --- HIGH-PRIORITY CHECK (CLOSE REGION) ---
                if not close_search_error_logged:
                    try:
                        close_screenshot = sct.grab(CLOSE_SEARCH_REGION)
                        close_haystack = np.array(close_screenshot)
                        close_path = os.path.join(IMAGE_FOLDER, CLOSE_GAME_IMAGE)
                        if os.path.exists(close_path):
                            if pyautogui.locate(close_path, close_haystack, confidence=IMAGE_CONFIDENCE, grayscale=True):
                                print(f"\nCLOSE image '{CLOSE_GAME_IMAGE}' found! Closing...")
                                pyautogui.hotkey('alt', 'f4')
                                time.sleep(1)
                                pyautogui.hotkey('alt', 'f4')
                                time.sleep(1)
                                print("To cancel the shutdown, open CMD and type: shutdown /a")
                                os.system('shutdown /s /t 5')
                                time.sleep(1)
                                exit_script()
                                continue
                    except Exception as e:
                        print(f"not found hunger image")
                     
                
                
                # --- NORMAL SEARCH (ACTION REGION) ---
                action_screenshot = sct.grab(ACTION_SEARCH_REGION)
                action_haystack = np.array(action_screenshot)
                key_found = None
                
                for image_path, key in target_images.items():
                    try:
                        if pyautogui.locate(image_path, action_haystack, confidence=IMAGE_CONFIDENCE, grayscale=True):
                            key_found = key
                            break
                    except (pyautogui.ImageNotFoundException, ValueError):
                        continue
                
                if key_found:
                    print(f"Target '{key_found}' found! Starting full sequence...")
                    
                    if not press_key_for_duration(key_found, 73): continue
                    time.sleep(6)
                    if cycle_counter_hung >100:
                        pyautogui.hotkey('alt', 'f4')
                        time.sleep(1)
                        pyautogui.hotkey('alt', 'f4')
                        time.sleep(1)
                        print("To cancel the shutdown, open CMD and type: shutdown /a")
                        os.system('shutdown /s /t 5')
                        time.sleep(1)
                        exit_script()
                    cycle_counter += 1
                    
                    if cycle_counter > 0 and cycle_counter % 2 == 0:
                        
                        print("\nExecuting 3-cycle sequence...")
                    
                        print("--> Pressing '2'...")
                        pydirectinput.press('4')
                        time.sleep(1) # Short pause
                    
                        print("--> Clicking mouse...")
                        pydirectinput.click()
                        time.sleep(2)

                        print("--> Pressing '3'...")
                        pydirectinput.press('5')
                        time.sleep(1)

                        print("--> Clicking mouse...")
                        pydirectinput.click()
                        time.sleep(2)
                        print("3-cycle sequence complete.")
                    if cycle_counter > 0 and cycle_counter % 15  == 0:
                        print("--> Pressing '4'...")
                        pydirectinput.press('6')
                        time.sleep(1) # Short pause
                    
                        print("--> Clicking mouse...")
                        pydirectinput.click()
                        time.sleep(2)

                        print("--> Pressing '5'...")
                        pydirectinput.press('7')
                        time.sleep(1)

                        print("--> Clicking mouse...")
                        pydirectinput.click()
                        time.sleep(2)

                        pydirectinput.press('8')
                        time.sleep(1)
                        pydirectinput.click()
                        print("10-cycle sequence complete.")

                    print("--> Pausing for 20 seconds...")
                    if not wait_for_duration(10): continue
                    if not close_search_error_logged:
                        try:
                            close_screenshot = sct.grab(CLOSE_SEARCH_REGION)
                            close_haystack = np.array(close_screenshot)
                            close_path = os.path.join(IMAGE_FOLDER, CLOSE_GAME_IMAGE)
                            if os.path.exists(close_path):
                                if pyautogui.locate(close_path, close_haystack, confidence=IMAGE_CONFIDENCE, grayscale=True):
                                    print(f"\nCLOSE image '{CLOSE_GAME_IMAGE}' found! Closing...")
                                    pyautogui.hotkey('alt', 'f4')
                                    time.sleep(1)
                                    pyautogui.hotkey('alt', 'f4')
                                    time.sleep(1)
                                    print("To cancel the shutdown, open CMD and type: shutdown /a")
                                    os.system('shutdown /s /t 5')
                                    time.sleep(1)
                                    exit_script()
                                    continue
                        except Exception as e:
                            print(f"not found hunger image")
                        
                    print("--> Holding 'W' for 1 second...")
                    pydirectinput.keyDown('w')
                    if not wait_for_duration(1):
                        pydirectinput.keyUp('w'); continue
                    pydirectinput.keyUp('w')
                    
                    print("--> Pressing 'E'...")
                    pydirectinput.press('e')
                    if not wait_for_duration(1): continue

                    print("--> Smoothly moving mouse to X=955, Y=610...")
                  
                    
                    print("--> Clicking at current mouse position...")
                    pydirectinput.click()

                    print("Sequence complete. Resuming search.")
                    time.sleep(2)
                
                else:
                    time.sleep(0.5)

            else:
                time.sleep(0.1)
    print("Bot thread terminated.")

# --- CONTROL FUNCTIONS (BUTTONS AND HOTKEYS) ---
def start_bot():
    global is_running, close_search_error_logged, cycle_counter
    if not is_running:
        close_search_error_logged = False
        cycle_counter = 0 # Reset counter on start
        is_running = True; print("====== BOT ACTIVATED ======"); update_status_label()

def stop_bot():
    global is_running
    if is_running:
        is_running = False; print("====== BOT PAUSED ======"); update_status_label()

def toggle_bot_hotkey():
    if is_running: stop_bot()
    else: start_bot()

def exit_script():
    global should_exit, root
    print("Exiting script...")
    should_exit = True
    try: root.destroy()
    except: pass

# --- IMAGE PREPARATION ---
target_images = {}
print("Loading images from 'Pic' folder...")
try:
    action_images_list = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith('.png') and f != CLOSE_GAME_IMAGE]
    for filename in action_images_list:
        key = os.path.splitext(filename)[0]
        full_path = os.path.join(IMAGE_FOLDER, filename)
        target_images[full_path] = key
        print(f"  - ACTION Image: '{full_path}' mapped to key '{key}'")
    if not target_images:
        print("\nWARNING: No ACTION images found.")
    if os.path.exists(os.path.join(IMAGE_FOLDER, CLOSE_GAME_IMAGE)):
        print(f"  - CLOSE Image: '{CLOSE_GAME_IMAGE}' is configured.")
    else:
        print(f"\nWARNING: The close image '{CLOSE_GAME_IMAGE}' was not found.")
except FileNotFoundError:
    print(f"\nCRITICAL ERROR: The folder '{IMAGE_FOLDER}' was not found!")
    exit()

# --- HOTKEY SETUP ---
keyboard.add_hotkey('f8', toggle_bot_hotkey)
keyboard.add_hotkey('esc', exit_script)

# --- GRAPHICAL USER INTERFACE (GUI) SETUP ---
root = tk.Tk()
root.title("Bot Controller")
root.attributes("-topmost", True)
root.geometry("300x150")
root.resizable(False, False)

bold_font = font.Font(family="Helvetica", size=12, weight="bold")
status_font = font.Font(family="Helvetica", size=14, weight="bold")

main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(expand=True, fill="both")

status_frame = tk.Frame(main_frame)
status_frame.pack(pady=5)
tk.Label(status_frame, text="Status:", font=bold_font).pack(side="left")
status_label = tk.Label(status_frame, text="PAUSED", font=status_font, fg="red")
status_label.pack(side="left")

button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start (F8)", command=start_bot, font=bold_font, bg="#4CAF50", fg="white", width=12)
start_button.pack(side="left", padx=5)

stop_button = tk.Button(button_frame, text="Stop (F8)", command=stop_bot, font=bold_font, bg="#f44336", fg="white", width=12)
stop_button.pack(side="left", padx=5)

info_label = tk.Label(main_frame, text="Press 'Esc' to close", font=("Helvetica", 8))
info_label.pack(side="bottom")

def update_status_label():
    if is_running:
        status_label.config(text="ACTIVE", fg="green")
    else:
        status_label.config(text="PAUSED", fg="red")

# --- INITIALIZATION ---
if __name__ == "__main__":
    bot_thread = threading.Thread(target=bot_loop, daemon=True)
    bot_thread.start()
    root.mainloop()