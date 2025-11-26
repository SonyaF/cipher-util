def main():
    try:
        keyword = getValidInput("Enter keyword for Encryption: ")
        keyword = keyword.upper()
        
        use_keyed = input("Use keyed alphabet for Vigenere Table? (y/N): ").strip()
        if use_keyed.upper() == 'Y':
            while True:
                vKeyword = getValidInput("Enter keyword for Vigenere Table: ")
                vKeyword = vKeyword.upper().replace(" ", "")
                if not hasDuplicateLetters(vKeyword):
                    break
                print("Keyword cannot contain duplicate letters. Please try again.")
            vTable = createVigenereTable(vKeyword)
        else:
            vTable = createNormalVigenereTable()

    except KeyboardInterrupt:
        print("\nExiting...")
        raise


def createVigenereTable(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper()
    for letter in keyword:
        alphabet = alphabet.replace(letter, "")
    alphabet = keyword + alphabet
    table = []
    for i in range(26):
        table.append(alphabet[i:] + alphabet[:i])
    return table

def hasDuplicateLetter(text):
    seen = set()
    for char in text:
        if char in seen:
            return True
        seen.add(char)
    return False

def createNormalVigenereTable():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = []
    for i in range(26):
        table.append(alphabet[i:] + alphabet[:i])
    return 
    
def validateInput(text):
    for char in text:
        if not (char.isalpha() or char == ' '):
            return False
    return True



if __name__ == "__main__":
    main()
