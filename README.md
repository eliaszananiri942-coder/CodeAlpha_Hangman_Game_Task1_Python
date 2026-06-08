cat > README.md << 'EOF'
# 🎮 Hangman Game - CodeAlpha Task 1

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-completed-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 👨‍💻 Developed By
**Eias Zananiri**

## 📋 Project Overview
A classic text-based Hangman game developed as **Task 1** for the **CodeAlpha Python Programming Internship**. This game challenges players to guess a word one letter at a time, with a limited number of incorrect attempts.

## ✨ Features
- 🎲 **5 Predefined Words** - Randomly selected from a curated list
- 🔢 **6 Incorrect Guesses Limit** - Classic Hangman difficulty
- 🎨 **Visual Hangman Display** - ASCII art showing hangman progress
- ✅ **Input Validation** - Prevents duplicate guesses and invalid inputs
- 🔄 **Replay Option** - Play multiple rounds without restarting
- 📊 **Score Tracking** - Shows number of attempts taken to win

## 🚀 How to Play
1. Run the game: `python hangman_game.py`
2. Guess one letter at a time (A-Z)
3. You have **6 incorrect guesses** before the hangman is complete
4. Fill in all blanks to win!
5. Choose to play again or exit after each round

## 🎯 Word List
| Word | Length |
|------|--------|
| PYTHON | 6 letters |
| JAVASCRIPT | 10 letters |
| DEVELOPER | 9 letters |
| PROGRAMMING | 11 letters |
| HANGMAN | 7 letters |

## 💻 Installation & Running

### Prerequisites
- Python 3.x installed
- No external libraries required

### Steps
```bash
# Clone the repository
git clone https://github.com/eliaszananiri942-coder/CodeAlpha_Hangman_Game_Task1_Python.git

# Navigate to directory
cd CodeAlpha_Hangman_Game_Task1_Python

# Run the game
python hangman_game.py
