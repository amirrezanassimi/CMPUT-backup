
import string 

def main(): 
    mKey = 'Missing Key!'
    inPair = 'Invalid ciphertext-code pair!'
    ciphers = getFileData()
    alphabet = string.ascii_uppercase
    for cipherCodePair in ciphers:
        decipheredWord = ''
        if len(cipherCodePair) > 1:
            for letter in cipherCodePair[0]: 
                index = (alphabet.index(letter)+int(cipherCodePair[1]))%len(alphabet)
                decipheredWord += alphabet[index]
            print(decipheredWord)
        else:
            print(mKey)
            #break
def getFileData(): 
    getFileName = True 
    dataAccessPrompt = 'Enter the input filename: '
    checkFilePathMes = 'Please make sure the file is in the correct location, and try again.'
    accessAttempts = 0 
    ciphers = []
    while getFileName:
        try: 
            fileName = input(dataAccessPrompt).lower().rstrip()
            dataFile = open(fileName,'U')
            fileContent = dataFile.read().split('\n')
            for cipherDatum in fileContent:
                cipherCodePair = cipherDatum.split(' ')
                ciphers.append(cipherCodePair)
            dataFile.close()
            return ciphers
        except FileNotFoundError: 
            accessAttempts += 1
            if accessAttempts >= 3:
                print(checkFilePathMes)
                quit()

main()