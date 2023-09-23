import os
from pynput.keyboard import Listener
from time import sleep
import sys


taulukko = {
   "a" : ".-",   
   "b" : "-...", 
   "c" : "-.-.", 
   "d" : "-..",  
   "e" : ".",    
   "f" : "..-.", 
   "g" : "--.",  
   "h" : "....", 
   "i" : "..",   
   "j" : ".---", 
   "k" : "-.-",  
   "l" : ".-..", 
   "m" : "--",   
   "n" : "-.",   
   "o" : "---",  
   "p" : ".--.", 
   "q" : "--.-", 
   "r" : ".-.",  
   "s" : "...",  
   "t" : "-",    
   "u" : "..-",  
   "v" : "...-", 
   "w" : ".--",  
   "x" : "-..-", 
   "y" : "-.--", 
   "z" : "--..", 
   "0" : "-----",
   "1" : ".----",
   "2" : "..---",
   "3" : "...--",
   "4" : "....-",
   "5" : ".....",
   "6" : "-....",
   "7" : "--...",
   "8" : "---..",
   "9" : "----." 
}

# 1. The length of a dot is 1 time unit.
# 2. A dash is 3 time units.
# 3. The space between symbols (dots and dashes) of the same letter is 1 time unit.
# 4. The space between letters is 3 time units.
# 5. The space between words is 7 time units.
timeunit = 0.15 # 150 millisecs

# from enum import Enum
# class MorseAction(Enum):
#     LETTER = 1
#     WORDSPACE = 2
def tarkista( syote):
    kaikki_ok = True
    for kirjain in syote:
        if kirjain not in taulukko and kirjain is not ' ':
            kaikki_ok = False
            break # ensimmainen outo merkki, lopeta etsinta
    if not kaikki_ok:
        print("viesti sisaltaa ei morse-merkkeja")

def printAsIs(morsemerkki, endofline):
    if morsemerkki is None:
        print("   ", end="", flush=True) # sanaväli
    else:
        print(morsemerkki, end=" ", flush=True)
    if endofline:
        print(flush=True) # rivinvaihto
    sleep(timeunit)

def print_timed(morsemerkki, endofline):
    if morsemerkki is None:
        # sanaväli
        print("   ", end="", flush=True); sleep(7*timeunit)
    else:
        # yhden kirjaimen tulostus
        for dash_or_dot in morsemerkki:
            if dash_or_dot is '-':
                factor = 3
            else:
                factor = 1
            print(dash_or_dot, end="", flush=True); sleep(factor*timeunit)
        # kirjaimen vali
        print(end=" ", flush=True); sleep(1*timeunit)
    if endofline:
        # rivinvaihto, viesti loppu
        print(flush=True); sleep(1 * timeunit)


def juokse_lapi(syote):
    counter = 0
    for element in input1:
        kirjain = element.lower()
        counter = counter + 1
        if kirjain is ' ':
            morsemerkki = None
        elif kirjain not in taulukko:
            # skip
            continue
        else:
            morsemerkki = taulukko[kirjain]
        endofline = counter == len(input1)
        #printAsIs(morsemerkki, endofline)
        print_timed(morsemerkki, endofline)


if __name__ == "__main__":
    # input
    print("syota lause (ja paina enter):\n")
    input1 = input()

    # tarkista teksti on koodattavissa
    tarkista(input1)

    # juokse läpi
    juokse_lapi(input1)

