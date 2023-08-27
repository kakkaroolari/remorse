import os
from pynput.keyboard import Listener


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

temp_viesti = ""

def lue_viesti():
    # todo: virheet kii..
    temp_viesti = "" # tyhjennetaan
    print("Enter message: ")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    print(message)

def on_press(key):
    print("Key pressed: {0}".format(key))
    if not isinstance(key, str):
        return
    lowkey = key.lower()
    if not lowkey in taulukko.keys():
        return
    
    temp_viesti += lowkey

def on_release(key):
    pass

def main():
    print("Aloitetaan!")
    # 1. syötä lause (while) kunnes ctrl-C
    #   -- lue key press, kunnes EOF
    lue_viesti()
    # 2. käännä syöte morsejonoksi
    # 3. echota ja piipitä



if __name__ == "__main__":
    main()
