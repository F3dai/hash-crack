import hashlib
import sys
import os
import hashid # HashID py file

logo = """
██╗░░██╗░█████╗░░██████╗██╗░░██╗░░░░░░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
██║░░██║██╔══██╗██╔════╝██║░░██║░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
███████║███████║╚█████╗░███████║█████╗██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░
██╔══██║██╔══██║░╚═══██╗██╔══██║╚════╝██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░
██║░░██║██║░░██║██████╔╝██║░░██║░░░░░░╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
"""

hashtypes = ["MD5", "SHA-256", "SHA-1", "SHA-512"]

# Have they provided 2 arguments?
def get_input():
    if len(sys.argv) == 3:
        wordlist = sys.argv[1]
        passwordhash = sys.argv[2]
        print("Wordlist selected:", sys.argv[1], "\nPassword Hash:", sys.argv[2])
        validate(sys.argv[1], sys.argv[2])
        hash_ID(passwordhash, wordlist)
    else:
        print("Incorrect number of arguments.")
        print("Usage: python hashcracker.py [/wordlist/path] [password hash]")
        sys.exit()

# Is wordlist is valid
def validate(wordlist, password):
    hash_type = ""
    if os.path.isfile(wordlist) == False:
        print("\n[!] '"+wordlist+ "' Not Found, please use a valid path to a wordlist.\nUsage: python hashcracker.py [/wordlist/path] [password hash]")
        sys.exit()


# Identify hash type
def hash_ID(passwordhash, wordlist):
    try: # Start Validation
        results = hashid.get_hash(passwordhash)
        print("\nPossible Hashs:")
        print("- ", results[0])
        print("- ", results[1])
        print("\nLeast possible Hashs:")
        for x in range(len(results)-2):
            print("-", results[x+2])
            if x == 7:
                break
    except:
        print("[!] Hash type not found, please enter a valid hash type")
        sys.exit()

    print("\nAvailable hash decryption functions: ")
    for x in range(len(hashtypes)): print(str(x + 1) + ". " + hashtypes[x]) # Display all selection choices 

    while True:
        try: # Integer Validation
            cont = int(input("\nWhich hash type would you like to check against? "))
            if cont < 1 or cont > len(hashtypes): # Range validation
                print("[!] Out of range")
            else:
                break
        except:
            print("[!] Invalid int")
                
    decrypt_algorithm(hashtypes[cont-1], passwordhash, wordlist) # Send user choices to algorithm selection
    
def decrypt_algorithm(algorithm, item, wordlist): # Redirect to brute function
    print("Testing = ", algorithm)
    if algorithm == "MD5":
        decrypt_MD5(item, wordlist)
    if algorithm == "SHA-256":
        decrypt_SHA256(item, wordlist)
    if algorithm == "SHA-1":
        decrypt_SHA1(item, wordlist)
    if algorithm == "SHA-512":
        decrypt_SHA512(item, wordlist)

def decrypt_MD5(item, wordlist):
    wordlist = open(wordlist, "r")
    try:
        for line in wordlist:
            line = line.strip()
            print("- Trying: ", line, end='\r')

            if hashlib.md5(line.encode('utf-8')).hexdigest() == item:
                print("[+] Success - cracked", item, " as ", line)
                sys.exit()
    except KeyboardInterrupt: # Stops python errors
        print("\nBye bye")
        
    print("\r\n\n[x] Failed to crack file")

def decrypt_SHA1(item, wordlist):
    wordlist = open(wordlist, "r")
    try:
        for line in wordlist:
            line = line.strip()
            print("- Trying: ", line, end='\r')

            if hashlib.sha1(line.encode('utf-8')).hexdigest() == item:
                print("[+] Success - cracked", item, " as ", line)
                sys.exit()
                
    except KeyboardInterrupt: # Stops python errors
        print("\nBye bye")

    print("\r\n\n[x] Failed to crack file")

def decrypt_SHA256(item, wordlist):
    wordlist = open(wordlist, "r")
    try: 
        for line in wordlist:
            line = line.strip()
            print("- Trying: ", line, end='\r')

            if hashlib.sha256(line.encode('utf-8')).hexdigest() == item:
                print("[+] Success - cracked", item, " as ", line)
                sys.exit()
    except KeyboardInterrupt: # Stops python errors
        print("\nBye bye")
    
    print("\r\n\n[x] Failed to crack file")

def decrypt_SHA512(item, wordlist):
    wordlist = open(wordlist, "r")
    try:
        for line in wordlist:
            line = line.strip()
            print("- Trying: ", line, end='\r')

            if hashlib.sha512(line.encode('utf-8')).hexdigest() == item:
                print("[+] Success - cracked", item, "as", line)
                sys.exit()
    except KeyboardInterrupt:
        print("\nBye bye")

    print("\r\n\n[x] Failed to crack file")

print(logo)

get_input()