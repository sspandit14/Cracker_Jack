# Cracker Jack (Jack the Cracker might be problematic...) -- ITP125 Final Project, Sahil Pandit

import time
import hashlib

def crack_password(hash, password_found, guesses_so_far):
    if password_found[1] == True:
        return

    next_set_of_guesses = []
    #chars_to_guess = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789~!@#$%&*"
    chars_to_guess = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%&*"
    for guess in guesses_so_far:
        for i in chars_to_guess:
            new_guess = guess + i
            #print(new_guess)
            hashed_guess = (hashlib.md5(new_guess.encode())).hexdigest()
            if hash == hashed_guess:
                password_found[0] = new_guess
                password_found[1] = True
                next_set_of_guesses.append(new_guess)
                return
            else:
                next_set_of_guesses.append(new_guess)

    crack_password(hash, password_found, next_set_of_guesses)

def crack_password_two(hash_to_crack, guesses_so_far, num_cracked, pass_found, start):
    if num_cracked == len(hash_to_crack):
        return

    next_set_of_guesses = []
    chars_to_guess = "0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ~!@#$%&*"
    for guess in guesses_so_far:
        for i in chars_to_guess:
            new_guess = guess + i
            #print(new_guess)
            hashed_guess = (hashlib.md5(new_guess.encode())).hexdigest()
            if hashed_guess in hash_to_crack:
                num_cracked += 1
                pass_found.append([new_guess, time.time()-start])
                print(pass_found)
            
            next_set_of_guesses.append(new_guess)

    crack_password_two(hash_to_crack, next_set_of_guesses, num_cracked, pass_found, start)


pass_the_hash = open("hashes.txt", "r")
hash_to_crack = pass_the_hash.readlines()
pass_and_times = []

for i in range(0, len(hash_to_crack)):
    hash_to_crack[i] = hash_to_crack[i][:-1]

guesses_so_far = [""]

i = 1

for hash in hash_to_crack:
    start = time.time()

    password_found = [None, False]

    print(f'cracking password #{i}...')

    guesses_so_far = [""]

    crack_password(hash, password_found, guesses_so_far)

    print(f'Password is: {password_found[0]}')

    end = time.time()

    time_taken = end-start

    print(f'{time_taken} seconds taken\n')

    pass_times = [password_found[0], time_taken]
    pass_and_times.append(pass_times)

    i += 1

print("all passwords cracked!")
print("times taken per password:")

for t in pass_and_times:
    print(f'Password: \'{t[0]}\' took {t[1]} seconds to crack')