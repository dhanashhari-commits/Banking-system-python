from bank_system import BankSystem


def show_menu():
    print("\n==== BANKING SYSTEM ====")
    print("1. Create Customer")
    print("2. Create Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. View Account Details")
    print("6. Exit")


def main():
    system = BankSystem()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            print("Create Customer selected")

        elif choice == "2":
            print("Create Account selected")

        elif choice == "3":
            print("Deposit Money selected")

        elif choice == "4":
            print("Withdraw Money selected")

        elif choice == "5":
            print("View Account selected")

        elif choice == "6":
            print("Exiting program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
  
