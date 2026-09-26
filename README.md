# Password Strength Checker

A simple Python password strength checker that validates password security based on character composition and length.

## Features

- Check password strength in real-time
- Support for multiple languages (English and Portuguese)
- Evaluates based on:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Password length (8+ and 16+ characters)
- Four strength levels:
  - **Very Strong**: Contains uppercase, lowercase, numbers, and 16+ characters
  - **Strong**: Contains uppercase, lowercase, numbers, and 8+ characters
  - **Medium**: Contains at least 2 of 3 (uppercase/lowercase/numbers) and 8+ characters
  - **Weak**: Contains at least 2 of 3 (uppercase/lowercase/numbers) but less than 8 characters
  - **Very Weak**: Contains only 1 or none of the above requirements

## How to Use

1. Run the program:
   ```bash
   python password_strength_checker.py
   ```

2. Enter your password when prompted
3. Select your language (English or Portuguese)
4. The program will calculate and display your password strength
5. Choose whether to check another password or exit

## Example

```
Please insert your password >>> MyPassword123
Calculating password strengh...
Your password is: strong
```

## ⚠️ Important Warning

**This tool is for educational purposes only.** 

- **Do NOT use this as a password strength validator for important accounts** (email, banking, social media, etc.)
- This checker provides basic validation only and does not account for advanced security measures
- For important accounts, use the security tools provided by the official platforms (Gmail, banks, etc.)
- Always use strong, unique passwords with special characters for sensitive accounts
- Consider using a password manager for better security

## Requirements

- Python 3.x

## Notes

- The program will restart after each password check
- Invalid inputs will cause the program to restart
- This is a beginner-friendly learning project