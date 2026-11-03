# Matrix Falling Text Generator

A Python-based terminal animation inspired by the digital rain effect from *The Matrix*. It displays multiple streams of falling characters, with customizable colours, rainbow effects, and Japanese Katakana characters.

## Features

- **Multiple falling streams:** Displays several columns of falling characters simultaneously.
- **Customizable colours:** Choose from green, red, blue, white, yellow, cyan, magenta, and black.
- **Rainbow mode:** Displays trails in multiple colours.
- **Katakana mode:** Uses half-width Japanese Katakana characters.
- **Screensaver mode:** Runs continuously and exits when any key is pressed.
- **Adjustable speed:** Set the animation delay when starting the program or change it while running.
- **Terminal resizing:** Adjusts the animation when the terminal window changes size.
- **White character heads:** The leading character in each stream is displayed in white.

## Requirements

- Python 3.10 or later
- A terminal that supports `curses`

**Windows users:** Install `windows-curses` to enable curses support.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/abrahamzion01/matrix_generator.git
```

### 2. Navigate into the project directory

```bash
cd matrix_generator
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate
```

**Windows (Git Bash):**
```bash
source .venv/Scripts/activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 5. Install the Windows curses dependency

On Windows, run:

```bash
pip install windows-curses
```

Linux and macOS users generally have curses available through Python.

## Usage

Start the animation using:

```bash
python ccmatrix.py
```

### Command-line options

| Option | Description |
|---|---|
| `-s` | Run in screensaver mode. Press any key to exit. |
| `-u 0` to `-u 10` | Set the animation delay level (default: 4). |
| `-C green` | Choose the trail colour. |
| `-C red` | Display red trails. |
| `-C blue` | Display blue trails. |
| `-C white` | Display white trails. |
| `-C yellow` | Display yellow trails. |
| `-C cyan` | Display cyan trails. |
| `-C magenta` | Display magenta trails. |
| `-C black` | Display black trails. |
| `-r` | Enable rainbow mode. |
| `-c` | Enable half-width Katakana characters. |

### Examples

Run with red trails:

```bash
python ccmatrix.py -C red
```

Run in rainbow mode:

```bash
python ccmatrix.py -r
```

Run with Katakana characters:

```bash
python ccmatrix.py -c
```

Run in screensaver mode:

```bash
python ccmatrix.py -s
```

Set the animation delay:

```bash
python ccmatrix.py -u 6
```

Combine options:

```bash
python ccmatrix.py -r -c -u 3
```

## Keyboard Controls

While the animation is running:

| Key | Action |
|---|---|
| `q` | Quit the animation. |
| `0`–`9` | Change the animation speed. |
| Any key | Exit when running with `-s`. |

## Project Structure

```text
matrix_generator/
│
├── ccmatrix.py
├── README.md
└── .venv/
```

## Technologies Used

- **Python** – Main programming language.
- **Curses** – Terminal screen handling and animation.
- **Random** – Generates random characters and stream behaviour.
- **Argparse** – Handles command-line arguments.
- **Time** – Controls animation timing.

## Learning Outcomes

Building this project provided practical experience with:

- Python functions and modules.
- Loops and conditional statements.
- Lists and dictionaries.
- Random number generation.
- Command-line argument parsing.
- Terminal manipulation using curses.
- Handling keyboard input.
- Working with virtual environments and Python dependencies.

## Author

Created as a Python programming challenge project.

