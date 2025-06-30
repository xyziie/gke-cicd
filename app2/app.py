# from flask import Flask

# # Create a Flask application
# app = Flask(__name__)

# # Define a route for the root URL
# @app.route('/')
# def hello_world():
#     return 'Hello, Achyut. This is Application 2!'

# # Run the Flask application if this file is executed directly
# if __name__ == '__main__':
#     app.run(debug=True, port=8081,host='0.0.0.0')


###################################
# Second App
# app.py
import sys
from pyfiglet import Figlet

def generate_ascii_art(text):
    """
    Generates ASCII art for the given text.
    """
    try:
        # Initialize Figlet with a default font
        # You can explore other fonts by listing them:
        # f = Figlet()
        # print(f.getFonts())
        f = Figlet(font='slant')
        ascii_art = f.renderText(text)
        return ascii_art
    except Exception as e:
        return f"Error generating ASCII art: {e}"

def main():
    print("Welcome to the Funky ASCII Art Generator!")
    print("---------------------------------------")
    print("Enter the text you want to convert to ASCII art.")
    print("Type 'exit' or 'quit' to stop.")

    while True:
        try:
            user_input = input("Your text: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting the ASCII Art Generator. Goodbye!")
                break
            elif not user_input.strip():
                print("Please enter some text.")
                continue

            art = generate_ascii_art(user_input)
            print("\n" + art + "\n")
        except EOFError: # Handles Ctrl+D/Ctrl+Z
            print("\nExiting. Goodbye!")
            break
        except KeyboardInterrupt: # Handles Ctrl+C
            print("\nExiting. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()

