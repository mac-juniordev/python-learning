from datetime import datetime


print("=================== MacDiary ===================")

print("================ Welcome to MacDiary ================")





while True:
    print("1. New Entry")
    print("2. Read All Entries")
    print("3. Exit")

    choice = input("Choose an Option: ")

    if choice == "1":
        word = input("Enter Your text: ")

        now = datetime.now()

        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open("log.txt", "a") as file:
            
            file.write(f"{timestamp}  |  {word}\n")
        

    elif choice == "2":
        try:
            with open("log.txt", "r") as file:
                for line in file:
                    print(line)
        except FileNotFoundError:
            print("No entries found yet.")

    elif choice == "3":
        print("Goodbye, see you soon")
        break

    else:
        print("Invalid choice, try again")
