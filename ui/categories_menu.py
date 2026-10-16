from database.connection import SessionLocal

from services.categories import (
    create_category,
    list_categories,
    update_category,
    delete_category,
)

def show_categories_menu():
    while True:
        print("\n===== MANAGE CATEGORIES =====")
        print("1. Add Category")
        print("2. List Categories")
        print("3. Update Category")
        print("4. Delete Category")
        print("0. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            name = input("Enter category name: ").strip()

            if not name:
                print("Category name cannot be empty.")
                continue

            try:
                with SessionLocal.begin() as session:
                    category = create_category(session, name)
                    category_id = category.id

                print("Category created! ID:", category_id)

            except Exception as error:
                print("ERROR:", error)

        elif choice == "2":
            try:
                with SessionLocal() as session:
                    categories = list_categories(session)

                    if not categories:
                        print("No categories found.")

                    for category in categories:
                        print(category.id, "-", category.name)

            except Exception as error:
                print("ERROR:", error)

        elif choice == "3":
            try:
                category_id = int(
                    input("Enter category ID: ")
)

                new_name = input(
                    "Enter new category name: "
                ).strip()

                if not new_name:
                    print("Name cannot be empty.")
                    continue

                with SessionLocal.begin() as session:
                    updated = update_category(
                        session, category_id, new_name
)
                    success = updated is not None

                if success:
                    print("Category updated successfully!")
                else:
                    print("Category not found.")

            except ValueError:
                print("Please enter a valid ID.")

            except Exception as error:
                print("ERROR:", error)

        elif choice == "4":
            try:
                category_id = int(
                    input("Enter category ID: ")
)

                with SessionLocal.begin() as session:
                    deleted = delete_category(
                        session, category_id
)

                if deleted:
                    print("Category deleted successfully!")
                else:
                    print("Category not found.")

            except ValueError:
                print("Please enter a valid ID.")

            except Exception as error:
                print("ERROR:", error)

        else:
            print("Invalid choice.")