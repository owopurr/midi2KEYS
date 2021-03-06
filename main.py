import pygame.midi as midi
# import pyautogui
import keyboard
midi.init()


def printMIDIDeviceList():
    for ID in range(midi.get_count()):
        minfo = midi.get_device_info(ID)
        print(minfo[1].decode('utf-8'),
              "- input -" if minfo[2] else "- output -", ID)


printMIDIDeviceList()
INPUT = midi.Input(1)

NOTES = [36, 37, 46, 47]        # Note numbers in MIDI notes
KEYS = [0x1e, 0x1f, 0x11, 0x20] # HEX codes from http://www.flint.jp/misc/?q=dik&lang=en
noteToKey = dict(zip(NOTES, KEYS))

while True:
    if INPUT.poll():
        data = INPUT.read(1)
        note, stat = data[0][0][1], 0 if data[0][0][2] == 0 else 1
        if note in noteToKey:
            key = noteToKey[note]
            if stat == 0:
                # pyautogui.keyUp(key)
                # win32api.keybd_event(VK_CODE[key], 0,win32con.KEYEVENTF_KEYUP,0)
                keyboard.ReleaseKey(key)
            else:
                # pyautogui.keyDown(key)
                # win32api.keybd_event(VK_CODE[key], 0,0,0)
                keyboard.PressKey(key)
