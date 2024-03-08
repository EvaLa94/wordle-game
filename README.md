# Wordle solver

## Description
This project aims to implement a function that solves the Wordle game. The project consists of a script to run in the browser via Tampermonkey, which connects to a backend written in Django. The Django backend performs the search in the database to find valid solutions for the Wordle game.

## Features
- Wordle game solver.
- Integration with Tampermonkey for execution in the specific browser.
- Django backend for managing database search.

## Installation
1. Clone the repository to your computer:
```bash
git clone https://github.com/EvaLa94/wordle-game.git
```

2. Run the virtual environment:
```bash
cd wordle-game
python -m venv venv
venv\scripts\activate
```

3. Configure and start the Django backend:
```bash
pip install -r requirements.txt
cd wordle
python manage.py migrate
python manage.py runserver
```

4. Add the Tampermonkey extension to your browser.

5. Connect to the wordle website: 
[Link](https://wordlegame.org/it)

**This solver is currently available only for the Italian language!**

6. Add the script from browser-script/script.js to the Tampermonkey extension.

7. All set! In order to play, run the script to find the possible solutions.