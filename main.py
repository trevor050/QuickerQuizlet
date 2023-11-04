#install using "pip install googletrans==4.0.0-rc1"
import googletrans

# USER SETTINGS

# Show words with parentheses (True/False)
# Example assuming input is "desear (+infinitive)" Outputs are: True -> "To wish"; False -> "To wish (+infinitive)"
no_parentheses = True

# Import quizlet strings from a file path (True/False)
import_from_file = False 

# Increase speed greatly, but might hit rate limits (True/False)
extreme_speed_mode = False

# Output language (default is English 'en')
# For more language codes, visit: https://www.science.co.il/language/Codes.php
output_lang = "en"



# ADVANCED SETTINGS

# Enable highly efficent processing. Creates an extra file though (True/False). Recommended: True
efficiency_mode = True

# Enable SmartTranslate for optimal functionality (True/False). Strongly Recommended: True
smart_translate = True 

# Number of threads for ExtremeSpeedMode. Tinker only if you know your stuff.
extreme_speed_mode_threads = 5 




#DO NOT TOUCH
#Below is the code for the actual program. Do not touch unless you know what you're doing.

from typing import Dict
import socket
import json

acceptable_stops = [
    "--stop", "-- stop", "--sto", "-- sto", 
    "--stp", "-- stp", "--sotp", "-- sotp", 
    "--stpo", "-- stpo", "--top", "-- top",
    "--sopt", "-- sopt", "--stopp", "-- stopp",
    "--ops", "-- ops", "--st", "-- st",
    "--sop", "-- sop", "--stops", "-- stops"
]

wordlist = []
fixedoutputs = []
translation_cache: Dict[str, str] = {}



def Translate(text: str) -> str:
    translator = googletrans.Translator()
    translated = translator.translate(text, dest=output_lang).text
    return translated

def SmartTranslate(text: str, context: str = '', format_output=False) -> str:
    global translation_cache
    original_text = text
    if no_parentheses:
        if "(" in text:
            text = text.split("(")[0].strip()
    if efficiency_mode:
        if original_text in translation_cache:
            if format_output == True or extreme_speed_mode == True:
                formattedfix = f"{original_text}, {translation_cache[original_text]}"
                return formattedfix
            return translation_cache[original_text]

    translator = googletrans.Translator()
    translated = translator.translate(f"{text} {context}", dest='en').text  # Adjust 'en' to your desired language if needed

    # Cache the translation
    print(f"Adding {original_text} to cache")
    translation_cache[original_text] = translated
    print(translation_cache[original_text])

    if format_output == True or extreme_speed_mode == True:
        formattedfix = f"{original_text}, {translated}"
        return formattedfix
    else:
        return translated

# Your ExtremeSpeedModeTranslate function would look like this
def ExtremeSpeedModeTranslate(word_list, num_threads):
    from concurrent.futures import ThreadPoolExecutor
    global translation_cache
    translated_list = []
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        translated_list = list(executor.map(lambda x: SmartTranslate(x, format_output=True), word_list))
    
    return translated_list



def save_translation_cache(filename='translation_cache.json'):
    with open(filename, 'w') as f:
        json.dump(translation_cache, f)
    print(f"Cache saved to {filename}")

def load_translation_cache(filename='translation_cache.json'):
    global translation_cache
    try:
        with open(filename, 'r') as f:
            translation_cache = json.load(f)
        print(f"Cache loaded from {filename}")
    except FileNotFoundError:
        print(f"Efficiency Mode: No cache file found. Creating a new one at {filename}")
        translation_cache = {}
        save_translation_cache(filename)



def IsOnline(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False
    
def read_wordlist_from_file(filename: str) -> list:
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

if not __name__ == "__main__":
    print("Error: Please run this script directly.")
    exit()
if efficiency_mode:
    load_translation_cache()
if import_from_file:
    print("Please enter the file path.")
    filename = input("")
    wordlist = read_wordlist_from_file(filename)
else:
    print("Please enter your quizlet string. Add --stop on a newline to save it.")

    contents = []
    while True:
        try:
            line = input()
            if line.lower().strip() in acceptable_stops:
                break
        except EOFError:
            break
        wordlist.append(line)

if not IsOnline():
    print("\n")
    print("Error: Cannot connect to the internet. Please make sure you're online and try again.")
    exit()

print("Loading...")
print("\n\n\n")



def FinalTranslatedResult(wordlist):
    global fixedoutputs
    wordlist_length = len(wordlist)
    for word in range(wordlist_length):
        if not wordlist[word] == "" or wordlist[word].startswith("--"):
            if SmartTranslate:
                if not extreme_speed_mode:
                    fixedoutputs.append(wordlist[word]+ ', ' + SmartTranslate(wordlist[word]))
                else:
                    fixedoutputs = ExtremeSpeedModeTranslate(wordlist, extreme_speed_mode_threads)
            else:
                fixedoutputs.append(wordlist[word]+ ', ' + Translate(wordlist[word]))
    return fixedoutputs

final_result = FinalTranslatedResult(wordlist)
for item in final_result:
        print(item)

print("\n")

def create_text_file(final_result):
    with open("translated_words.txt", "w") as f:
        for item in final_result:
            f.write(item + "\n")
    return
if efficiency_mode:
    save_translation_cache()
print("Would you like to turn it into a text file? (y/n)")
TextFileAsk = input("")
TextFileAsk = TextFileAsk.lower()
if TextFileAsk == "y":
    create_text_file(final_result)
    print("Created!")
else:
    print("Ok, bye!")
    exit()
