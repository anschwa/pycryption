'''
Modified encryption script to be used with PyCryption GUI
Made by Adam Schwarz, April 2013
'''


import random
from fractions import gcd

PRIMES = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
467, 479, 487, 491, 499]


########################################################################################################################
def check_keys(keys):
    keyList = keys.split(',')    
    try:
        n = map(int, keyList)   # checks if keys are integers
        return True
        
    except ValueError:
        error = "Key must be numbers separated with a comma"
        return error
########################################################################################################################
def gen_keys(primes):
    if check_keys(primes) == True:
        
        primesT = tuple(int(i) for i in primes.split(','))
        p, q = primesT
        n = p*q
        
        if (p and q) in PRIMES:
            totn = (p-1)*(q-1)
            
            while True:
                '''pick a random int between 1 and totn,
                if the gcd between num and totn == 1,
                then num must be coprime to totn'''
                
                num = random.randint(1, totn)
                if gcd(num, totn) == 1:
                    e = num
                    d = pow(e, totn-1, totn)
                    if e != d:
                        break
            
            return [(n, e), (n, d)]     # returns public and private key in a list
                
        else:
            error = "Primes must be betwwen 10 and 500"
            return error
    
    else:
        error = "Primes cannot contain letters and must be separated with a comma"
        return error
########################################################################################################################
def encrypt_message(pubKey, message):
        try:
            pubKeyT = tuple(int(i) for i in pubKey.split(','))     # splits a string into a integer tuple
            n, e = pubKeyT
            
            plainList = list(message)
            paddedList = [ord(i) for i in plainList]    # converts characters to ascii integers

            encrypt = [(i**e)%n for i in paddedList] 

            enMessage = "-".join(str(i) for i in encrypt)
            return enMessage
        except ValueError:
            return "An error occurred during the encryption process"
########################################################################################################################            
def decrypt_message(priKey, enMessage):
        try:
            priKeyT = tuple(int(i) for i in priKey.split(','))     # splits a string into a integer tuple
            n, d = priKeyT

            enListStr = enMessage.split('-')
            enList = map(int, enListStr)

            decrypt = [(i**d)%n for i in enList]

            deMessage = ''.join(chr(i) for i in decrypt)    # joins list and reverses padding of message
            return deMessage
        except ValueError:
            return "An error occurred during the decryption process"
########################################################################################################################
# generating keys
#
#genKeys = gen_keys(primes)
#
#print "public key:", genKeys[0]
#
#print "private key:", genKeys[1]
#
########################################################################################################################
# Testing the cryption
#
#if check_keys(defaultPubKey) == True:    
#    enMessage = encrypt_message(defaultPubKey, message)
#    print enMessage
#
#    if check_keys(defaultPriKey) == True:
#        deMessage = decrypt_message(defaultPriKey, enMessage)
#        print deMessage
#    else:
#        print check_keys(defaultPriKey)
#
#else:
#    print check_keys(defaultPubKey)    # prints out error message if keys fail check