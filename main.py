from typing import Text
import googletrans


#take a string, then every new line split the string, then put that through google translate. the come back with orginalword, translatedword. example: hola \n gordo comes out with hola, hello \n gordo, fat. Translate from eng to spanish
wordlist = []
fixedoutputs = []
def translate(text):
    translator = googletrans.Translator()
    translated = translator.translate(text, dest='en')
    return translated.text


print("Paste your quizlet string, add --stop on a newline to save it.")
contents = []
while True:
    try:
        line = input()
        #check if --stop is included
        if line == "--stop":
            break
            contents.append(line)
    except EOFError:
        break
    wordlist.append(line)

print("Loading...")
print("\n\n\n\n")

def FinalTranslatedResult(wordlist):
    wordlist_length = len(wordlist)
    for word in range(wordlist_length):
        fixedoutputs.append(wordlist[word]+ ', ' + translate(wordlist[word]))
    return fixedoutputs

final_result = FinalTranslatedResult(wordlist)
for item in final_result:
    print(item)

print("\n")

def create_text_file(final_result):
    with open("translated_words.txt", "w") as f:
        for item in final_result:
            f.write(item + "\n")
print("Would you like to turn it into a text file? (y/n)")
TextFileAsk = input("")
TextFileAsk = TextFileAsk.lower()
if TextFileAsk == "y":
    create_text_file(final_result)
    print("Created!")
else:
    print("Ok, bye!")
    exit()