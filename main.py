# Cracker Jack (Jack the Cracker might be problematic...) -- ITP125 Final Project, Sahil Pandit

import time
import hashlib

pass_the_hash = open("hashes.txt", "r")
hash_to_crack = pass_the_hash.readlines()
times_to_crack = []

for hash in hash_to_crack:
    start = time.time()

    while guess_hash != hash:
        #make a recursive brute force lmao

    end = time.time()

    time_taken = end-start

    print(time_taken + " seconds taken")

def crack_password(hash, current_guess, new_char):
    new_guess = current_guess + new_char
    new_guess = (hashlib.md5(new_guess.encode())).hexdigest()

    if hash == new_guess:
        return True
    else
        return False