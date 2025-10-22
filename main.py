```python
/*
Author: Durgesh Mahajan
Date: 2023-10-15 14:30:00
Project: Daily Spark
*/

import random
import os

QUOTES_FILE = 'quotes.txt'

def load_quotes():
    """Load quotes from the file, create the file if it doesn't exist."""
    if not os.path.exists(QUOTES_FILE):
        with open(QUOTES_FILE, 'w') as file:
            pass  # Create an empty file
        return []
    with open(QUOTES_FILE, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def save_quote(quote):
    """Append a new quote to the quotes file."""
    with open(QUOTES_FILE, 'a') as file:
        file.write(quote + '\n')

def get_random_quote(quotes):
    """Return a random quote from the list."""
    if not quotes:
        return "No quotes available. Please add one!"
    return random.choice(quotes)

def list_all_quotes(quotes):
    """Print all quotes one by one."""
    if not quotes:
        print("No quotes available. Please add one!")
        return
    for index, quote in enumerate(quotes, start=1):
        print(f"{index}. {quote}")

def display_menu():
    """Display the main menu and get user input."""
    print("\nDaily Spark Menu:")
    print("1. Get a Quote")
    print("2. Add a Quote")
    print("3. List All Quotes")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ").strip()
    return choice

def main():
    # Load existing quotes
    quotes = load_quotes()
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            quote = get_random_quote(quotes)
            print(f"\nYour Daily Spark:\n{quote}\n")
        
        elif choice == '2':
            new_quote = input("Enter the new quote: ").strip()
            if new_quote:
                save_quote(new_quote)
                quotes.append(new_quote)
                print("Quote added successfully!")
            else:
                print("Quote cannot be empty.")
        
        elif choice == '3':
            list_all_quotes(quotes)
        
        elif choice == '4':
            print("Exiting Daily Spark. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### Explanation of the Program:

- **File Handling:** The program checks if `quotes.txt` exists and creates it if not. It loads quotes from this file at startup.
- **Random Quote Display:** The `get_random_quote` function selects and returns a random quote from the list.
- **Adding New Quotes:** The `save_quote` function appends a new quote to the `quotes.txt` file.
- **Listing All Quotes:** The `list_all_quotes` function displays all stored quotes one by one.
- **User Menu:** The `display_menu` function presents a simple text-based menu for user interaction.
- **Main Loop:** The `main` function handles the main program loop, taking user input and calling appropriate functions.
- **Error Handling:** Basic checks are in place, such as ensuring the user does not enter an empty quote or an invalid menu choice.

This program is designed to be user-friendly, simple, and efficient, making it easy to add and display inspiring quotes or affirmations.