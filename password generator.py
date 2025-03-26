import random
import string

# Function to generate a random password
def generate_random_password(length):
    # Minimum password length for security
    min_length = 8
    
    # Check if the password length is less than the minimum required
    if length < min_length:
        print(f"For security, the password must be at least {min_length} characters long.")
        return None
    
    # Include all character types by default (uppercase, lowercase, digits, symbols)
    characters = (
        string.ascii_uppercase +  # Uppercase letters
        string.ascii_lowercase +  # Lowercase letters
        string.digits +           # Digits
        string.punctuation        # Special symbols
    )
    
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to generate a memorable password
def generate_memorable_password(custom_numbers):
    # List of phrases to use in the password
    phrases = [
        "I love coding",
        "The sun is shining",
        "Coffee is life",
        "Keep calm and code",
        "Dream big work hard",
        "Never give up",
        "Stay curious always",
        "Learn something new",
        "Be kind to others",
        "The sky is the limit"
    ]
    
    # Select a random phrase from the list
    phrase = random.choice(phrases)
    
    # Split the phrase into individual words
    words = phrase.split()
    
    # Add custom numbers if provided by the user
    if custom_numbers:
        for i in range(len(words)):
            if i < len(custom_numbers):
                words[i] += custom_numbers[i]
    
    # Add random symbols to each word
    symbols = [random.choice(["!", "@", "#", "$", "%", "&", "*"]) for _ in range(len(words))]
    words = [word + symbols[i] for i, word in enumerate(words)]
    
    # Combine the words into a single password
    password = "".join(words)
    return password

# Main program loop
while True:
    print("\n1. Generate a random password")
    print("2. Generate a memorable password")
    print("3. Exit")
    choice = input("Choose an option (1, 2, or 3): ")

    if choice == '1':
        # Explain the importance of minimum password length
        print("For security, the password must be at least 8 characters long.")
        length = int(input("Enter the password length (minimum 8): "))
        
        # Generate the random password
        password = generate_random_password(length)
        if password:
            print("Your random password:", password)

    elif choice == '2':
        custom_numbers = input("Enter the numbers you want to add (e.g., 123): ")
        
        # Check if the input contains only digits
        if not custom_numbers.isdigit():
            print("Error: Please enter only numbers.")
        else:
            password = generate_memorable_password(custom_numbers)
            print("Your memorable password:", password)

    elif choice == '3':
        print("Exiting the program. Thank you for using the password generator!")
        print("Feel free to come back anytime you need a new password. Goodbye!")
        break  # Exit the loop and end the program

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")