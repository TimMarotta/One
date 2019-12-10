"""
AUTHOR: TIMOTHY MAROTTA
DATE:   DECEMBER 9, 2019
COURSE: MASS 10400: STORY
"""
import story
from collections import OrderedDict
import textwrap
import pyttsx


def main():
    text = story.text
    full_replace = story.full_replace
    for x in range(len(full_replace)):
        full_replace[x] = full_replace[x].strip()
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
    final_text = ""
    for count in range(len(text)):
        final_text += text[count]
        if count <= 123:
            final_text += full_replace[count]
        count += 1
    wrapper = textwrap.TextWrapper(width=140)
    word_list = wrapper.fill(text=final_text)
    to_print = open("one_run.txt", "w+")
    to_print.write(word_list)
    print(word_list)

    language = "en"
    myobj = gTTS(text=final_text,lang=language, slow=False)
    myobj.save("one_audio.mp3")
    os.system("mpg321 one_audio.mp3")



if __name__ == '__main__':
    main()
