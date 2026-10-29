
MORSE_CODE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",
    "D": "-..",   "E": ".",     "F": "..-.",
    "G": "--.",   "H": "....",  "I": "..",
    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",
    "S": "...",   "T": "-",     "U": "..-",
    "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "!": "-.-.--", "'": ".----.", ":": "---...",
    ";": "-.-.-.", "/": "-..-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "&": ".-...",
    "=": "-...-", "+": ".-.-.", "_": "..--.-",
    '"': ".-..-.", "$": "...-..-", "@": ".--.-."
}

REVERSE_CODE = {
    code: letter for letter, code in MORSE_CODE.items()
}


def text_to_morse(text):
    words = text.upper().split()
    translated_words = []

    for word in words:
        letters = [
            MORSE_CODE.get(letter, "?")
            for letter in word
        ]
        translated_words.append(" ".join(letters))

    return " / ".join(translated_words)


def morse_to_text(morse):
    words = morse.strip().split(" / ")
    translated_words = []

    for word in words:
        letters = word.split()
        decoded = "".join(
            REVERSE_CODE.get(code, "?")
            for code in letters
        )
        translated_words.append(decoded)

    return " ".join(translated_words)


while True:
    print("\n=== MORSE CODE TRANSLATOR ===")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        text = input("Enter your text: ")
        print("===============================")
        print("Morse Code:", text_to_morse(text))
        print("===============================")

    elif choice == "2":
        morse = input("Enter Morse code: ")
        print("===============================")
        print("Translated Text:", morse_to_text(morse))
        print("===============================")

    elif choice == "3":
        print("Thank you for using the translator!")
        print("===============================")
        break

    else:
        print("Invalid choice. Please try again.")
