# Brute Force in Python

This Python script attempts to find a matching combination for a given password by generating all possible combinations of ASCII printable characters. It supports both hashed (all algorithms of `hashlib`) and unhashed passwords.

## Features

- Supports various hashing algorithms such as `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `sha3_224`, `sha3_256`, `sha3_384`, `sha3_512`, `shake_128`, `shake_256`, `blake2b`, `blake2s`, and `md5`.
- Can identify the original password for both known and unknown hashing algorithms.
- Calculates the time taken to find the matching password and the number of combinations tried per minute.

## How It Works

1. **Prompt for Password**:
   - The script asks the user if the password is hashed.
   - If the password is hashed, it prompts the user to enter the hashed password.
   - If the password is not hashed, it prompts the user to enter the unhashed password.

2. **Generate Combinations**:
   - The script generates all possible combinations of ASCII printable characters.
   - It starts with combinations of length 1 and increases the length until a matching combination is found.
   - If the password is hashed, it uses the same algorithm to figure out the password by hashing each generated combination before comparing.

3. **Match and Time Calculation**:
   - The script compares each generated combination with the target password or its hash.
   - Once a match is found, the script calculates and prints the time taken and the number of combinations tried per minute.

## Prerequisites

- Python 3.x

## Usage

1. Clone this repository or download the script.
2. Run the script using Python:

    ```bash
    python bruteforce.py
    ```

3. Follow the prompts:
    - Enter whether the password is hashed (y/n).
    - Enter the hashed or unhashed password as appropriate.

4. The script will output the matching combination, the time taken to find it, and the number of combinations tried per minute.

## Performance

Benchmark with a laptop with 16GB of RAM:

It runs at about 520,000,000 combinations per minute.

## Example

```bash
$ python bruteforce.py
Is your password hashed? (y/n): n
Enter the password: Hey!
Matching combination found: Hey!
Time taken: 5.1 seconds
Combinations tried per minute: 523753914.94
```