import sys

def main():
    try:
        # 1. FIX: getValidInput will now work with the fixed loop
        keyword = getValidInput("Enter keyword for Encryption: ")
        keyword = keyword.upper()
        
        use_keyed = input("Use keyed alphabet for Vigenere Table? (y/N): ").strip()
        if use_keyed.upper() == 'Y':
            while True:
                vKeyword = getValidInput("Enter keyword for Vigenere Table: ")
                vKeyword = vKeyword.upper().replace(" ", "")
                # 2. FIX: Corrected function name from hasDuplicateLetters to hasDuplicateLetter
                if not hasDuplicateLetter(vKeyword):
                    break
                print("Keyword cannot contain duplicate letters. Please try again.")
            vTable = createVigenereTable(vKeyword)
        else:
            vTable = createNormalVigenereTable()
        
        vdict = createDict(vTable[0])
        
        try:
            while True:
                choice = input("Encrypt or Decrypt? (E/D): ").upper()
                if choice == 'E':
                    plaintext = getValidInput("Enter plaintext: ").upper()
                    ciphertext = encrypt(plaintext, keyword, vTable, vdict)
                    print("Ciphertext: ", ciphertext.lower())
                elif choice == 'D':
                    ciphertext = getValidInput("Enter ciphertext: ").upper()
                    plaintext = decrypt(ciphertext, keyword, vTable, vdict)
                    print("Plaintext: ", plaintext.lower())
                elif choice == "EXIT":
                    break
        except KeyboardInterrupt:
            print("\nExiting...")
    except KeyboardInterrupt:
        print("\nExiting...")

def encrypt(plaintext, keyword, table, dict):
    ciphertext = ""
    plaintext = plaintext.upper().replace(" ", "")
    keyword = keyword.upper()
    while len(keyword) < len(plaintext):
        keyword += keyword
    for i, char in enumerate(plaintext):
        row = dict[keyword[i]]
        col = dict[char]
        ciphertext += table[row][col]
    return ciphertext

def decrypt(ciphertext, keyword, table, dict):
    plaintext = ""
    ciphertext = ciphertext.upper().replace(" ", "")
    keyword = keyword.upper()
    # 3. FIX: Simplified logic to correctly find the original letter
    while len(keyword) < len(ciphertext):
        keyword += keyword
    for i, char in enumerate(ciphertext):
        row_idx = dict[keyword[i]]
        row = table[row_idx]
        col_idx = row.index(char)
        plaintext += table[0][col_idx]
    return plaintext

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

def createNormalVigenereTable():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = []
    for i in range(26):
        table.append(alphabet[i:] + alphabet[:i])
    return table # 4. FIX: Added missing return

def createDict(List):
    dictionary = {}
    for i, key in enumerate(List):
        dictionary[key] = i # 5. FIX: '=' instead of '=='
    return dictionary

def hasDuplicateLetter(text):
    seen = set()
    for char in text:
        if char in seen: return True
        seen.add(char)
    return False

def validateInput(text):
    return all(char.isalpha() or char == ' ' for char in text)

def getValidInput(prompt):
    while True:
        user_input = input(prompt)
        if validateInput(user_input): # 6. FIX: Added missing colon
            return user_input
        print("Invalid input. Only letters and spaces are allowed.")

if __name__ == "__main__":
    main()
