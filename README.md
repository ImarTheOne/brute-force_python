# brute force python

This Python script attempts to find a matching combination for a given password, either hashed or unhashed, by generating all possible combinations of ASCII printable characters.

## How It Works

1. **Prompt for Password Type**:
   - The script asks if the password is hashed or not.
   - If the password is unhashed, the script hashes the provided password.
   - If the password is already hashed, the script accepts the unhashed password.

2. **Generate Combinations**:
   - The script generates all possible combinations of ASCII printable characters.
   - It starts with combinations of length 1 and increases the length until a matching combination is found.

3. **Match and Time Calculation**:
   - The script compares each generated combination with the target (either hashed or unhashed).
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

    - Indicate if your password is hashed (y/n).
    - Enter the password when prompted.

4. The script will output the matching combination, the time taken to find it, and the number of combinations tried per minute.

## Example

```bash
$ python password_combination_finder.py
Is your password hashed? (y/n): n
Enter the password: example
Matching combination found: example
Time taken: 5.123 seconds
Combinations tried per minute: 45000.67
```
