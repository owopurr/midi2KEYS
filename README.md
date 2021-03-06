# midi to keyboard conv.
get python (i have 3.8.5)  
do `pip install -r requirements.txt`  
in `main.py`, find lines 17 and 18
- change line 17 to match your MIDI input notes (i.e. C4 is 60 usually; see [this](https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies))
- change line 18 to match the KEY outputs. see [this](http://www.flint.jp/misc/?q=dik&lang=en)
- __make sure they line up!__  
`NOTES = [1,    2,    3   ]`  
`KEYS  = [0x1E, 0x30, 0x2E] # A, B, C`  
will do:  
`1 -> A`  
`2 -> B`  
`3 -> C`

run `main.py` and the game you want to play  
done 👍