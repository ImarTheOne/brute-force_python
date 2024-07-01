import itertools
import string
import time

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

# Main script
target_variable = input("Enter the password to find: ")

start_time = time.time()

matching_combination, combinations_tried = find_matching_combination(target_variable)

end_time = time.time()

time_taken = end_time - start_time
combinations_per_minute = combinations_tried / (time_taken / 60)

print(f"Matching combination found: {matching_combination}")
print(f"Time taken: {time_taken} seconds")
print(f"Combinations tried per minute: {combinations_per_minute:.2f}")
