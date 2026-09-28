# Password Strength Checker

A simple Python password strength checker that validates password security based on character composition and length.

## Features

- Check password strength in real-time
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
3. The program will calculate and display your password strength
4. Choose whether to check another password or exit

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

---

## Version History

### v2.0 (Current)

**Major Changes:**
- **GUI Update**: Replaced command-line interface with a modern Tkinter GUI
  - Clean graphical interface with password input field
  - Button to trigger password strength check
  - Visual display of results with dynamic label updates
- **Improved User Experience**: 
  - Real-time visual feedback with "Calculating password strength..." message
  - 3-second delay for better UX during calculation
  - Ability to check multiple passwords without restarting
  - Proper label cleanup between checks to prevent UI clutter
- **Code Structure**: 
  - Refactored with improved variable management
  - Better separation of UI elements and logic
  - Enhanced password checking algorithm with more robust character detection

### v1.0 (Initial Release)

**Features:**
- Command-line interface for password strength checking
- Support for English and Portuguese languages
- Basic password validation based on:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Password length thresholds
- Four strength levels (Very Weak, Weak, Medium, Strong, Very Strong)
- Restart functionality after each check
