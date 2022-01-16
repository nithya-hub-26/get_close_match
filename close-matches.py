from difflib import get_close_matches
import json
import calendar

jsonfile = json.load(open("data.json"))  # dataset

word = input("enter the word: ")  # enter the word which must be accessed from the dataset
if word == "calendar":
    yr = int(input("Enter the year: "))  # the calendar is displayed according to the entered year
    calendar = calendar.calendar(yr)


    def check(w):
    w = w.lower()  # the entered words are lowered
    if w in jsonfile:
        if w == "calendar":
            print()
            print()
            print(jsonfile[w])  # it contains a tagline of "displayed below" after which the calendar is displayed
            print(calendar)
        else:
            print(jsonfile[w])  # the value of the entered key word is displayed
    elif len(get_close_matches(w, jsonfile.keys())) > 0:  # 0 is priority always the priority must be high so that we get the close match
        close_match = get_close_matches(w, jsonfile.keys())[0]  # first element of the list is the closest match
        print("Did you mean %s" % close_match)
        user = input("yes or no: ")
        user = user.lower()
        if user in ("y", "yes", "s"):  # if the close match is guessed
            if close_match == "calendar":
                calendar1 = calendar.calendar(int(input("Enter the year: ")))
                print()
                print()
                print(jsonfile[close_match])
                print(calendar1)
            else:
                print(jsonfile[close_match])
        elif user in ("n", "no", "nope"):  # if the close match is not guessed
            print("please try again")
        else:
            print("only give yes or no, y or n, s or nope")
    else:
        print("invalid word")


check(word)


