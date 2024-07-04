import hashlib
import random

hashes = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'shake_128', 'shake_256', 'blake2b', 'blake2s', 'md5']

def hashing():
    hash_alg = str(input("Which algorithm do you want to use? (d for don't know & x for random) ").lower())
    while hash_alg not in hashes and hash_alg != "d" and hash_alg != "x":
        print("This is not an option")
        hash_alg = input("Which algorithm do you want to use? (d for don't know & x for random) ").lower()
        
    target_variable = str(input("What do you want to hash? "))
    if hash_alg in hashes:
        hash_func = getattr(hashlib, hash_alg)
        if hash_alg in ['shake_128', 'shake_256']:
            while True:
                try:
                    val = int(input("Length of your hash? "))
                    if 1 <= val <= 255:
                        break  # Exit loop if val is valid
                    else:
                        print("Invalid input. Please enter a number between 1 and 255.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            target_hash = hash_func(target_variable.encode()).hexdigest(val)
        else:
            target_hash = hash_func(target_variable.encode()).hexdigest()
        return target_hash
    elif hash_alg == "d":
        hash_func = hashlib.md5
        target_hash = hash_func(target_variable.encode()).hexdigest()
        return target_hash    
    elif hash_alg == "x":
        random_alg = random.choice(hashes)
        print(random_alg)
        hash_func = getattr(hashlib, random_alg)
        if random_alg in ['shake_128', 'shake_256']:
            while True:
                try:
                    val = int(input("Length of your hash? "))
                    if 1 <= val <= 255:
                        break  # Exit loop if val is valid
                    else:
                        print("Invalid input. Please enter a number between 1 and 255.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            target_hash = hash_func(target_variable.encode()).hexdigest(val)
        else:
            target_hash = hash_func(target_variable.encode()).hexdigest()
        return target_hash
    else:
        print("Error")

print(hashes)

result = hashing()
print("Hashed value:", result)
