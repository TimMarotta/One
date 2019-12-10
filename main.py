"""
AUTHOR: TIMOTHY MAROTTA
DATE:   DECEMBER 9, 2019
COURSE: MASS 10400: STORY
"""
import story
from collections import OrderedDict
from datetime import datetime as dt


def main():
    text = story.text
    full_replace = story.full_replace
    unique_replace = list(OrderedDict.fromkeys(full_replace))
    print("Welcome Story Class!! Below I will ask a series of questions to help make Tim's story. Shout out answers "
          "as you see fit!")
    for term in unique_replace:
        temp = input(term + ": ")
        if temp == "break":
            break
        for item in full_replace:
            if item is term:
                full_replace[full_replace.index(item)] = temp
    # TODO write items in alternating order to file text, then full_replace
    file1 = open("one_run_" + str(dt.now().time()) + ".txt", "w+")
    count = 0
    for phrase in text:
        if "." in phrase:
            if phrase.startswith('.'):
                text[count] = '\n' + text[count]
            elif phrase.endswith('.'):
                text[count] = text[count]
        file1.write(text[count])
        if count <= 123:
            file1.write(full_replace[count])
        count += 1
    # TODO print entire story
    # TODO speak text file (estimated 4 minutes?)
    file1.close()


if __name__ == '__main__':
    main()
