# brute force python

This Python script attempts to find a matching combination for a given password by generating all possible combinations of ASCII printable characters.

## How It Works

1. **Prompt for Password**:
   - The script asks the user to input the password they want to find.

2. **Generate Combinations**:
   - The script generates all possible combinations of ASCII printable characters.
   - It starts with combinations of length 1 and increases the length until a matching combination is found.

3. **Match and Time Calculation**:
   - The script compares each generated combination with the target password.
   - Once a match is found, the script calculates and prints the time taken and the number of combinations tried per minute.

## Prerequisites

- Python 3.x

## Usage

1. Clone this repository or download the script.
2. Run the script using Python:

    ```bash
    python bruteforce.py
    ```

3. Follow the prompt:

    - Enter the password when prompted.

4. The script will output the matching combination, the time taken to find it, and the number of combinations tried per minute.

## Example

```bash
$ python password_combination_finder.py
Enter the password to find: Hey!
Matching combination found: Hey!
Time taken: 5.06455659866333 seconds
Combinations tried per minute: 523088986.84
```
