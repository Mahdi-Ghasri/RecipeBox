from database.connection import SessionLocal
from services.users import (
    create_user,
    list_users,
    delete_user,
)

def show_users_menu():
    while True:
        print("\n===== MANAGE USERS =====")
        print("1. Add User")
        print("2. List Users")
        print("3. Delete User")
        print("0. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            email = input("Enter email: ").strip()

            if not email:
                print("Email cannot be empty.")
                continue

            try:
                with SessionLocal.begin() as session:
                    user = create_user(session, email)
                    user_id = user.id

                print("User created successfully! ID:", user_id)

            except Exception as error:
                print("ERROR:", error)

        elif choice == "2":
            try:
                with SessionLocal() as session:
                    users = list_users(session)

                    if not users:
                        print("No users found.")

                    for user in users:
                        print(user.id, "-", user.email)

            except Exception as error:
                print("ERROR:", error)

        elif choice == "3":
            try:
                user_id = int(input("Enter user ID: "))

                with SessionLocal.begin() as session:
                    deleted = delete_user(session, user_id)

                if deleted:
                    print("User deleted successfully!")
                else:
                    print("User not found.")

            except ValueError:
                print("Please enter a valid number.")

            except Exception as error:
                print("ERROR:", error)

        else:
            print("Invalid choice.")