def encrypt(plain_text, secret_key):
    #plain text: it is the text we want to encrypt
    #secret key: it is the permutation of the alphabet
    #we need to know the alphabet used
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    print(alphabet)
    
    #eliminate whitespaces and duplicates 
    permutation = []
    for i in secret_key.replace(" ", "").lower():
        if i not in permutation:
            permutation.append(i)
    print(permutation)
    #check length of alphabet and the permutation
    if len(alphabet) == len(permutation):
        cipher_text = ""
        for i in plain_text.replace(" ", "").lower():
            cipher_text = cipher_text + permutation[alphabet.index(i)]
        return cipher_text.upper()
            
def decrypt(cipher_text, secret_key):
    #plain text: it is the text we want to encrypt
    #secret key: it is the permutation of the alphabet
    #we need to know the alphabet used
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    #print(alphabet)
    
    #eliminate whitespaces and duplicates 
    permutation = []
    for i in secret_key.replace(" ", "").lower():
        if i not in permutation:
            permutation.append(i)
    #print(permutation)
    #check length of alphabet and the permutation
    if len(alphabet) == len(permutation):
        plain_text = ""
        for i in cipher_text.replace(" ", "").lower():
            plain_text = plain_text + alphabet[permutation.index(i)]
        return plain_text
            

def main():
    text = "Attack postponed to tomorrow and do not use our secret paper until further info"
    key = "The quick brown fox jumps over the lazy dog"
    print(encrypt(text, key))
    print(decrypt(encrypt(text, key), key))

main()