def main():
    try:
        keyword = getValidInput("Enter keyword for Encryption: ").upper()

        use_keyed = input("Use keyed alphabet for Vigenere Table? (y/N): ").strip()
        if use_keyed.upper() == 'Y':
            while True:
                vKeyword = getValidInput("Enter keyword for Vigenere Table: ").upper().replace(" ", "")
                if not hasDuplicateLetter(vKeyword):
                    break
                print("Keyword cannot contain duplicate letters. Please try again.")
            vTable = createVigenereTable(vKeyword)
        else:
            vTable = createNormalVigenereTable()

        vdict = createDict(vTable[0])

        while True:
            choice = input("Encrypt or Decrypt? (E/D) or EXIT: ").upper()
            if choice == 'E':
                plaintext = getValidInput("Enter plaintext: ").upper()
                ciphertext = encrypt(plaintext, keyword, vTable, vdict)
                print("Ciphertext:", ciphertext.lower())
            elif choice == 'D':
                ciphertext = getValidInput("Enter ciphertext: ").upper()
                plaintext = decrypt(ciphertext, keyword, vTable, vdict)
                print("Plaintext:", plaintext.lower())
            elif choice == "EXIT":
                print("Goodbye!")
                break
    except KeyboardInterrupt:
        print("\nExiting...")

def encrypt(plaintext, keyword, table, d):
    ciphertext = ""
    plaintext = plaintext.replace(" ", "")
    for char in plaintext:
        ciphertext += table[d[char]][d[keyword[0]]]
        keyword = shiftKeyword(keyword, 1)
    return ciphertext

def decrypt(ciphertext, keyword, table, d):
    plaintext = ""
    ciphertext = ciphertext.replace(" ", "")
    for char in ciphertext:
        alphabet = createAlphabet(keyword[0], d)
        plaintext += table[0][alphabet.index(char)]
        keyword = shiftKeyword(keyword, 1)
    return plaintext

def shiftKeyword(keyword, shift):
    return keyword[shift:] + keyword[:shift]

def createAlphabet(key, d):
    swapped = swapDict(d)
    start = d[key]
    alphabet = ""
    for i in range(26):
        alphabet += swapped[(start + i) % 26]
    return alphabet

def createVigenereTable(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in keyword:
        alphabet = alphabet.replace(letter, "")
    alphabet = keyword + alphabet
    return [alphabet[i:] + alphabet[:i] for i in range(26)]

def createNormalVigenereTable():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return [alphabet[i:] + alphabet[:i] for i in range(26)]

def createDict(row):
    return {char: i for i, char in enumerate(row)}

def swapDict(d):
    return {v: k for k, v in d.items()}

def hasDuplicateLetter(text):
    return len(set(text)) != len(text)

def validateInput(text):
    return all(char.isalpha() or char == ' ' for char in text)

def getValidInput(prompt):
    while True:
        user_input = input(prompt)
        if validateInput(user_input):
            return user_input
        print("Invalid input. Only letters and spaces allowed.")

if __name__ == "__main__":
    main()
