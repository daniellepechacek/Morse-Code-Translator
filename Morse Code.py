#This code is to convert a string into Morse code.

# Step 1: Create a prompt that asks the user to input a string. (Or phrase/word/saying, etc)

# Step 2: Create a dictionary for Morse Code.

# Step 3: Create a loop.

# Step 4: Print the Morse code version


morsecode_dictionary={
#Letters
"a":".-",
"b":"-...",
"c":"-.-.",
"d":"-..",
"e":".",
"f":"..-.",
"g":"--.",
"h":"....",
"i":"..",
"j":".---",
"k":"-.-",
"l":".-..",
"m":"--",
"n":"-.",
"o":"---",
"p":".--.",
"q":"--.-",
"r":".-.",
"s":"...",
"t":"-",
"u":"..-",
"v":"...-",
"w":".--",
"x":"-..-",
"y":"-.--",
"z":"--..",
#Numbers and symbols
"0":"-----",
"1": ".----",
"2": "..---",
"3": "...--",
"4": "....-",
"5": ".....",
"6": "-....",
"7": "--...",
"8": "---..",
"9": "----.",
".": ".-.-.-",
",": "--..--",
"?": "..--..",
"'": ".----.",
"!": "-.-.--",
":": "---...",
";": "-.-.-.",
"(": "-.--.",
")": "-.--.-",
"&": ".-...",
"=": "-...-",
"+": ".-.-.",
"-": "-....-",
"_": "..--.-",
'"': ".-..-.",
"$": "...-..-",
"@": ".--.-.",

# The slashes aren't used in morse code, but after research, I found this.
"/": "-..-.",

}

letter = input("Type a letter: ")
print(morsecode_dictionary[letter.lower()])

sentence = input("Type a sentence to convert to Morse code: ")
#Create the empty string below to hold the morse code.
morse_translation = ""
#Loop
for char in sentence:
    if char ==" ":
    #The slash will separate the words.
        morse_translation += " / "
    elif char.lower() in morsecode_dictionary:
        morse_translation+=morsecode_dictionary[char.lower()]+""
    else:
        morse_translation+="[??]"
print("Morse code:",morse_translation)