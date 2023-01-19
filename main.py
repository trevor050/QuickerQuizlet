from typing import Text
import googletrans
#install using pip install googletrans==4.0.0-rc1

wordlist = []
fixedoutputs = []

NoParentheses = True
#Disable this if you want a word with Parentheses to show. Enabled (Defualt): Desear (+ infinitive), To wish.  Disabled: Desear (+infinitive), To wish (+infinitive)

def SmartTranslate(text):
    if NoParentheses:
        if "(" in text:
            text = text.split("(")[0]
    translator = googletrans.Translator()
    translated = translator.translate(text, dest='en')
    return translated.text


print("Paste your quizlet string, add --stop on a newline to save it.")
contents = []
while True:
    try:
        line = input()
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
        fixedoutputs.append(wordlist[word]+ ', ' + SmartTranslate(wordlist[word]))
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
