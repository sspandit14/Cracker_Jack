# Cracker Jack (Jack the Cracker might be problematic...) -- ITP125 Final Project, Sahil Pandit

import time
import hashlib

def crack_password(hash, current_guess, password_found, depth):
    if password_found[2] == True:
        print(password_found[1])
        return
    if password_found[0] == depth:
        return
    for i in range (32, 128):
        new_guess = current_guess + chr(i)
        hashed_guess = (hashlib.md5(new_guess.encode())).hexdigest()
        if hash == hashed_guess:
            password_found[1] = new_guess
            password_found[2] = True
            print(new_guess)
            return
        else:
            crack_password(hash, new_guess, password_found, depth+1)
        

pass_the_hash = open("hashes.txt", "r")
hash_to_crack = pass_the_hash.readlines()
print(hash_to_crack)
times_to_crack = []

for hash in hash_to_crack:
    start = time.time()

    hash = hash[:-1]
    print(hash)

    current_guess = ""
    password_found = [1, None, False]

    print("cracking password...")
    while password_found[2] == False:
        crack_password(hash, current_guess, password_found, 0)
        ++password_found[0]

    end = time.time()

    time_taken = end-start

    print(f'{time_taken} seconds taken')

    times_to_crack.append(time_taken)

print("all passwords cracked!")