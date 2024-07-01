# Brute force in python

This Python script attempts to find a matching combination for a given password by generating all possible combinations of ASCII printable characters. It supports both hashed (MD5) and unhashed passwords.

## How It Works

1. **Prompt for Password**:
   - The script asks the user if the password is hashed.
   - If the password is hashed, it prompts the user to enter the hashed password (MD5).
   - If the password is not hashed, it prompts the user to enter the unhashed password.

2. **Generate Combinations**:
   - The script generates all possible combinations of ASCII printable characters.
   - It starts with combinations of length 1 and increases the length until a matching combination is found.

3. **Match and Time Calculation**:
   - The script compares each generated combination with the target password or its MD5 hash.
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

Benchmark with a laptop with 16Gib of ram:

It runs with about $520'000'000$ combinations a minute.


## Example

```bash
$ python bruteforce.py
Is your password hashed? (y/n): y
Enter the unhashed password to find the hash: Hey!
Matching combination found: Hey!
Time taken: 5.058126926422119 seconds
Combinations tried per minute: 523753914.94
```
