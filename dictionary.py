import json
from difflib import get_close_matches                  #use difflib to check words similarity
                                                       #use get_close_matches is a method of difflib to check all posibilities of similar words 
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:                             #if user entered "UPPER" or "upper" this will check for "Upper" as well.
        return data[w.title()]
    elif w.upper() in data:                             #in case user enters words like USA or INDIA
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:    #checks the length of the 2 words in dict and the user, to check if the word is similar
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:                            #this helps to convert the list to sentence from dict
    for item in output:
        print(item)
else:
    print(output)
   
