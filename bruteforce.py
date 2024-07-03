import itertools
import string
import time
import hashlib

hashs = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'shake_128', 'shake_256', 'blake2b', 'blake2s', 'md5']

def hashed():
    global hashedornot, target_variable, hashed_target, knownhash, lentarget_variable
    hashedornot = input('Is your password hashed? (y/n): ').lower()
    if hashedornot == "y":
        print(hashs)
        knownhash = input("With which algorithm was the password hashed? (n if you don't know) ").lower()
        target_variable = input("Enter the hashed password to find the hash: ")
        lentarget_variable = int(len(target_variable)/2)
        hashed_target = target_variable
    else:
        target_variable = input("Enter the password: ")
    return hashedornot

def find_matching_combination_hashed(target_hash, hash_alg):
    ascii_characters = string.printable  # This includes all ASCII printable characters
    combinations_tried = 0
    hash_func = getattr(hashlib, hash_alg)
    
    length = 1
    while True:
        for combination in itertools.product(ascii_characters, repeat=length):
            combination_str = ''.join(combination)
            combinations_tried += 1
            if hash_alg in ['shake_128', 'shake_256']:
                if hash_func(combination_str.encode()).hexdigest(lentarget_variable) == target_hash:
                    return combination_str, combinations_tried
            else:
                if hash_func(combination_str.encode()).hexdigest() == target_hash:
                    return combination_str, combinations_tried
        length += 1

def find_matching_combination_unknownhash(target_hash, hashs):
    ascii_characters = string.printable # This includes all ASCII printable characters
    combinations_tried = 0
    
    length = 1
    while True:
        for hash_alg in hashs:
            hash_func = getattr(hashlib, hash_alg)
            for combination in itertools.product(ascii_characters, repeat=length):
                combination_str = ''.join(combination)
                combinations_tried += 1
                if hash_alg in ['shake_128', 'shake_256']:
                    if hash_func(combination_str.encode()).hexdigest(lentarget_variable) == target_hash:
                        return combination_str, combinations_tried
                else:
                    if hash_func(combination_str.encode()).hexdigest() == target_hash:
                        return combination_str, combinations_tried
        length += 1
    
def find_matching_combination(target):
    ascii_characters = string.printable  # This includes all ASCII printable characters
    combinations_tried = 0
    
    length = 1
    while True:
        for combination in itertools.product(ascii_characters, repeat=length):
            combination_str = ''.join(combination)
            combinations_tried += 1
            if combination_str == target:
                return combination_str, combinations_tried
        length += 1

hashed()

start_time = time.time()

if hashedornot == "y":
    if knownhash in hashs:
        matching_combination, combinations_tried = find_matching_combination_hashed(hashed_target, knownhash)
    else:
         matching_combination, combinations_tried = find_matching_combination_unknownhash(hashed_target, hashs)
else:
    matching_combination, combinations_tried = find_matching_combination(target_variable)

end_time = time.time()

time_taken = end_time - start_time
combinations_per_minute = combinations_tried / (time_taken / 60)

print(f"Matching combination found: {matching_combination}")
print(f"Time taken: {round(time_taken, 1)} seconds")
print(f"Combinations tried per minute: {combinations_per_minute:.2f}")
