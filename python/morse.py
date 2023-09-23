import os
from pynput.keyboard import Listener
from time import sleep


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
timefactor = 0.05 # 50 millisecs

if __name__ == "__main__":
    # input
    print("syota lause (ja paina enter):\n")
    input1 = input()

    # juokse läpi
    for kirjain in input1:
        if kirjain not in taulukko:
            print()
            continue
        morsemerkki = taulukko[kirjain]
        print(morsemerkki, " ")
        sleep(timefactor)

