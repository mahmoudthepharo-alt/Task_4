# Function to write (append) a message to log.txt
def write_log(message):
    try:
        with open("log.txt", "a") as file:
            file.write(message + "\n")
        print("Message saved.")
    except Exception as e:
        print("Error writing to log file:", e)


# Function to read and print all logs
def read_logs():
    try:
        with open("log.txt", "r") as file:
            print("\n--- Logs ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No log file found.")


# Menu for user interaction
def log_menu():
    while True:
        print("\n--- Log Menu ---")
        print("1. Write a log")
        print("2. Read logs")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter your message: ")
            write_log(message)

        elif choice == "2":
            read_logs()

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Try again.")


# Run the program
log_menu()