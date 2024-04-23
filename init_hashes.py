import hashlib

passwords = open("words.txt", "r")
hashes = open("hashes.txt", "w")

words = passwords.readlines()

for w in words:
    w = w.strip()
    w = w.encode()
    w = hashlib.md5(w)
    hashes.write(w.hexdigest() + "\n")

passwords.close()
hashes.close()