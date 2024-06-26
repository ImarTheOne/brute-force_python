import itertools
import string
import time

def find_matching_combination_hashed(target_hash):
    ascii_characters = string.ascii_lowercase  # This includes all ASCII printable characters
    combinations_tried = 0
    
    # Start with length 1 and increase the length until we find the match
    length = 1
    while True:
        # Generate all combinations of the current length
        for combination in itertools.product(ascii_characters, repeat=length):
            combination_str = ''.join(combination)
            #print(combination_str)
            combinations_tried += 1
            if hash(combination_str) == target_hash:
                return combination_str, combinations_tried
        # If no match found, increase the length for the next iteration
        length += 1

# Example usage
target_variable = 'lsblk'  # Replace this with the actual variable you want to match
hashed_target = hash(target_variable)

start_time = time.time()
matching_combination, combinations_tried = find_matching_combination_hashed(hashed_target)
end_time = time.time()

time_taken = end_time - start_time
combinations_per_minute = combinations_tried / (time_taken / 60)

print(f"Matching combination found: {matching_combination}")
print(f"Time taken: {time_taken} seconds")
# print(f"Combinations tried per minute: {combinations_per_minute:.2f}")
