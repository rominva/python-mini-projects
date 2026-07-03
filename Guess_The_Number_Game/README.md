# 🎲 Guess The Number Game

A fun and interactive command-line interface (CLI) game where you challenge yourself to guess a hidden number within a custom range.

![Version](https://img.shields.io/badge/version-4.0-blue)
![Python](https://img.shields.io/badge/python-3.x-green)

## 📺 Demo
![Game Preview](https://github.com/rominva/Guess_The_Number_Game/blob/main/assets/Guess_The_Number_Game.gif)

## 📝 Description
This is a classic "Guess the Number" game developed in Python. The user sets their own difficulty by choosing the range (minimum and maximum numbers). The game then picks a random number, and the player has **5 attempts** to find it.

## ✨ Features
- **Custom Range:** You decide the lower and upper bounds.
- **Input Validation:** Handles non-numeric inputs and range errors gracefully.
- **Smart Feedback:** Tells you if your guess is too high, too low, or out of your specified range.
- **Colorful UI:** Uses `colorama` for a vibrant and user-friendly experience (falls back to plain text if not installed).
- **Retry Logic:** Prevents the game from crashing if you type something wrong.

## 🚀 How to Run
1. **Clone the repository:**
   ```bash  
   git clone https://github.com/rominva/Guess_The_Number_Game.git

2. **Install dependencies:**
This game uses colorama for colors.
   ```bash 
   pip install colorama

3. **Run the game:**
   ```bash 
   python Guess_The_Number_Game.py

## 🎮 How to Play
1. Enter a Smaller number and a Bigger number to set the range.

2. The computer will pick a secret number between them.

3. You have 5 attempts.

4. Type your guess and press Enter.

5. Follow the hints (Higher/Lower) until you win or run out of lives!

## 👩‍💻 Author
• **Romina Valehi**

• Date: 2026

• Version: 4.0

## 📝 Design Notes 
This project was refactored to improve code structure and readability.

• The main focus was on:

• separating game logic from user interaction

• validating user input explicitly

• organizing the program around a clear main() flow

No new features were added — the goal was cleaner, more maintainable code.

This refactor reflects my ongoing focus on Python fundamentals and clean program structure.

