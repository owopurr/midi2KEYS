VALS = {
"ESC": 0x01,
"NUMBER1": 0x02,
"NUMBER2": 0x03,
"NUMBER3": 0x04,
"NUMBER4": 0x05,
"NUMBER5": 0x06,
"NUMBER6": 0x07,
"NUMBER7": 0x08,
"NUMBER8": 0x09,
"NUMBER9": 0x0A,
"NUMBER0": 0x0B,
"-": 0x0C,
"=": 0x0D,
"BKSP": 0x0E,
"TAB": 0x0F,
"Q": 0x10,
"W": 0x11,
"E": 0x12,
"R": 0x13,
"T": 0x14,
"Y": 0x15,
"U": 0x16,
"I": 0x17,
"O": 0x18,
"P": 0x19,
"[": 0x1A,
"]": 0x1B,
"ENTER": 0x1C,
"LEFTCTRL": 0x1D,
"A": 0x1E,
"S": 0x1F,
"D": 0x20,
"F": 0x21,
"G": 0x22,
"H": 0x23,
"J": 0x24,
"K": 0x25,
"L": 0x26,
";": 0x27,
"'": 0x28,
"`": 0x29,
"LEFTSHIFT": 0x2A,
"BACKSLASH": 0x2B,
"Z": 0x2C,
"X": 0x2D,
"C": 0x2E,
"V": 0x2F,
"B": 0x30,
"N": 0x31,
"M": 0x32,
",": 0x33,
".": 0x34,
"/": 0x35,
"RIGHTSHIFT": 0x36,
"NUM_STAR": 0x37,
"LEFTALT": 0x38,
"SPACE": 0x39,
"CAPSLOCK": 0x3A,
"F1": 0x3B,
"F2": 0x3C,
"F3": 0x3D,
"F4": 0x3E,
"F5": 0x3F,
"F6": 0x40,
"F7": 0x41,
"F8": 0x42,
"F9": 0x43,
"F10": 0x44,
"NUMLOCK": 0x45,
"SCROLLOCK": 0x46,
"NUM_7": 0x47,
"NUM_8": 0x48,
"NUM_9": 0x49,
"NUM_DASH": 0x4A,
"NUM_4": 0x4B,
"NUM_5": 0x4C,
"NUM_6": 0x4D,
"NUM_PLUS": 0x4E,
"NUM_1": 0x4F,
"NUM_2": 0x50,
"NUM_3": 0x51,
"NUM_0": 0x52,
"NUM_PERIOD": 0x53,
"F11": 0x57,
"F12": 0x58,
"F13": 0x64,
"F14": 0x65,
"F15": 0x66,
"YEN": 0x7D,
"EQUAL": 0x8D,
"CARET": 0x90,
"AT": 0x91,
"COLON": 0x92,
"UNDERSCORE": 0x93,
"NUM_Enter": 0x9C,
"RIGHTCTRL": 0x9D,
"NUM_COMMA": 0xB3,
"NUM_FORWARDSLASH": 0xB5,
"RIGHTALT": 0xB8,
}

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
KEYBOARD = Struct(**VALS)