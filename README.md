# RecipeBox

RecipeBox is a Python-based recipe management application that uses a database to organize users, recipes, ingredients, and favorites.

## Features

• User management
• User profile management
• Category management
• Ingredient management
• Recipe management
• Managing ingredients associated with recipes
• Adding, listing, and removing favorite recipes

## Technologies Used

• Python
• SQLAlchemy
• PostgreSQL
• Git and GitHub

## Project Structure

text
RecipeBox/
├── database/
├── models/
├── services/
├── ui/
├── main.py
├── requirements.txt
└── README.md


### Directory Overview

• database/: Database connection and configuration.
• models/: Database models.
• services/: Database operations and application logic.
• ui/: Command-line menus and user interaction.
• main.py: Main entry point of the application.

## Installation

### 1. Clone the repository

bash
git clone https://github.com/Mahdi-Ghasri/RecipeBox.git
cd RecipeBox


### 2. Create a virtual environment

bash
python -m venv .venv


Activate it on Windows:

powershell
.venv\Scripts\Activate.ps1


### 3. Install dependencies

bash
python -m pip install -r requirements.txt


### 4. Configure the database

Make sure PostgreSQL is installed and running.

Configure the database connection according to the existing project configuration in database/connection.py.

Ensure that the required database and tables have been created before running the application.

Do not commit database passwords or other sensitive credentials to GitHub.

### 5. Run the application

bash
python main.py


## Usage

After starting the application, follow the numbered menu options to manage users, profiles, categories, ingredients, recipes, recipe ingredients, and favorites.

## Project Status

The project includes a menu-driven interface, SQLAlchemy-based database operations, and CRUD functionality across its main modules.

Further testing and improvements may be added as development continues.