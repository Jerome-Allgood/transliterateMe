from tkinter import *

# Main transcription analouges
trans_rules = {"а": "a", "б": "b", "в": "v", "г": "h", "ґ": "g", "д": "d", "е": "e", "є": "ie", "ж": "zh", "з": "z",
               "и": "y", "і": "i", "ї": "i", "й": "i", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p",
               "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh",
               "щ": "shch", "ю": "iu", "я": "ia", "ь": "", "'": "",
               "А": "A", "Б": "B", "В": "V", "Г": "H", "Ґ": "G", "Д": "D", "Е": "E", "Є": "Ie", "Ж": "Zh", "З": "Z",
               "И": "Y", "І": "I", "Ї": "I", "Й": "I", "К": "K",
               "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U", "Ф": "F",
               "Х": "Kh", "Ц": "Ts", "Ч": "Ch", "Ш": "Sh", "Щ": "Shch", "Ю": "Iu", "Я": "Ia",
               " ": " ", ".": ".", ",": ",", "!": "!", "?": "?", "-": "-", "_": "_", '"': '"', "—": "—",
               "ё": "zgh", "Ё": "Zgh",
               "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0"}

# For first letters
# ю = yu
# я = ya
# є = ye
# й = y
# ї = yi

# List of special first letters
first_letters = {"й": "y", "Й": "Y", "ї": "yi", "Ї": "Yi", "є": "ye", "Є": "Ye", "ю": "yu", "Ю": "Yu",
                 "я": "ya", "Я": "Ya"}

target = "Їїїї, много жіжі. Піпа піпа ме, фасоль. Згори донизу, згораю"
test_string = "згзгзгзг"


# Special cases
# зг = zgh
# Зг = Zgh


def check_for_special_case(string):
    string = string.replace("Зг", "Ё")
    string = string.replace("зг", "ё")
    return string


def transliterate(string):
    words_arr = str(string).split(" ")
    new_words_arr = []
    for word in words_arr:
        word = check_for_special_case(word)
        new_word = ""
        for x in range(len(word)):
            if x == 0 and word[x] in first_letters:
                new_word += first_letters[word[0]]
            else:
                new_word += trans_rules[word[x]]
        new_words_arr.append(new_word)
    return " ".join(new_words_arr)


def set_result():
    result_entry.delete(0, END)
    result_entry.insert(0, transliterate(message.get()))


root = Tk()
root.title("TransliterateMe v0.2")
root.geometry("500x200")

message = StringVar()
result = StringVar()
enter_label = Label(text="Enter text in Ukrainian language: ")
result_label = Label(text="Result: ")
message_entry = Entry(textvariable=message, width=75)
message_entry.place(relx=.5, rely=.3, anchor="c")
enter_label.place(anchor="c", relx=.5, rely=.15)
result_label = Label(text="Result: ")
result_label.place(anchor="c", relx=.5, rely=.45)
result_entry = Entry(textvariable=result, width=75)
result_entry.place(relx=.5, rely=.6, anchor="c")

transcribe_button = Button(text="Transliterate", command=set_result)
transcribe_button.place(relx=.5, rely=.8, anchor="c")


root.mainloop()

# For first letters
# ю = yu
# я = ya
# є = ye
# й = y
# ї = yi





