from database.connection import SessionLocal

from services.ingredients import (
    create_ingredient,
    list_ingredients,
    update_ingredient,
    delete_ingredient,
)

def show_ingredients_menu():
    while True:
        print("\n===== MANAGE INGREDIENTS =====")
        print("1. Add Ingredient")
        print("2. List Ingredients")
        print("3. Update Ingredient")
        print("4. Delete Ingredient")
        print("0. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            name = input("Enter ingredient name: ").strip()

            if not name:
                print("Ingredient name cannot be empty.")
                continue

            try:
                with SessionLocal.begin() as session:
                    ingredient = create_ingredient(
                        session, name
)
                    ingredient_id = ingredient.id

                print("Ingredient created! ID:", ingredient_id)

            except Exception as error:
                print("ERROR:", error)

        elif choice == "2":
            try:
                with SessionLocal() as session:
                    ingredients = list_ingredients(session)

                    if not ingredients:
                        print("No ingredients found.")

                    for ingredient in ingredients:
                        print(ingredient.id, "-", ingredient.name)

            except Exception as error:
                print("ERROR:", error)

        elif choice == "3":
            try:
                ingredient_id = int(
                    input("Enter ingredient ID: ")
)

                new_name = input(
                    "Enter new ingredient name: "
                ).strip()

                if not new_name:
                    print("Name cannot be empty.")
                    continue

                with SessionLocal.begin() as session:
                    updated = update_ingredient(
session, ingredient_id, new_name
)
                    success = updated is not None

                if success:
                    print("Ingredient updated successfully!")
                else:
                    print("Ingredient not found.")

            except ValueError:
                print("Please enter a valid ID.")

            except Exception as error:
                print("ERROR:", error)

        elif choice == "4":
            try:
                ingredient_id = int(
                    input("Enter ingredient ID: ")
)

                with SessionLocal.begin() as session:
                    deleted = delete_ingredient(
                        session, ingredient_id
)

                if deleted:
                    print("Ingredient deleted successfully!")
                else:
                    print("Ingredient not found.")

            except ValueError:
                print("Please enter a valid ID.")

            except Exception as error:
                print("ERROR:", error)

        else:
            print("Invalid choice.")