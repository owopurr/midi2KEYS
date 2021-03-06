import pygame.midi as midi
# import pyautogui
import keyboard
from keybinds import KEYBOARD
midi.init()


def printMIDIDeviceList():
    for ID in range(midi.get_count()):
        minfo = midi.get_device_info(ID)
        print(minfo[1].decode('utf-8'),
              "- input -" if minfo[2] else "- output -", ID)


printMIDIDeviceList()
INPUT = midi.Input(1)

NOTES = [36, 37, 46, 47]        # Note numbers in MIDI notes
KEYS = [KEYBOARD.A, KEYBOARD.S, KEYBOARD.W, KEYBOARD.D]
noteToKey = dict(zip(NOTES, KEYS))

PRESS =   [153, 144, 159]
RELEASE = [137, 128, 143]

while True:
    if INPUT.poll():
        data = INPUT.read(1)
        print(data)
        note, stat = data[0][0][1], data[0][0][0]
        if note in noteToKey:
            key = noteToKey[note]
            if stat in RELEASE:
                # pyautogui.keyUp(key)
                # win32api.keybd_event(VK_CODE[key], 0,win32con.KEYEVENTF_KEYUP,0)
                keyboard.ReleaseKey(key)
            elif stat in PRESS:
                # pyautogui.keyDown(key)
                # win32api.keybd_event(VK_CODE[key], 0,0,0)
                keyboard.PressKey(key)
