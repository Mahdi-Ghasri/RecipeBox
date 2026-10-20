from decimal import Decimal, InvalidOperation

from database.connection import SessionLocal

from services.recipe_ingredients import (
    add_recipe_ingredient,
    get_recipe_ingredient,
    list_recipe_ingredients,
    update_recipe_ingredient,
    delete_recipe_ingredient,
)

def show_recipe_ingredients_menu():
    while True:
        print("\n===== MANAGE RECIPE INGREDIENTS =====")
        print("1. Add Recipe Ingredient")
        print("2. List Recipe Ingredients")
        print("3. Update Recipe Ingredient")
        print("4. Delete Recipe Ingredient")
        print("0. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            try:
                recipe_id = int(input("Enter recipe ID: "))
                ingredient_id = int(input("Enter ingredient ID: "))
                quantity = Decimal(input("Enter quantity: "))
                unit = input("Enter unit (gram, ml, piece, etc.): ").strip()

                if quantity <= 0 or not unit:
                    print("Quantity must be positive and unit cannot be empty.")
                    continue

                with SessionLocal.begin() as session:
                    item = add_recipe_ingredient(
                    session,
                    recipe_id,
                    ingredient_id,
                    quantity,
                    unit,
)

                    saved_recipe_id = item.recipe_id
                    saved_ingredient_id = item.ingredient_id

                print(
                    "Recipe ingredient added successfully!",
                    "Recipe ID:", saved_recipe_id,
                    "Ingredient ID:", saved_ingredient_id,
)

            except (ValueError, InvalidOperation):
                print("Please enter valid numbers and quantity.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "2":
            try:
                recipe_id = int(input("Enter recipe ID: "))

                with SessionLocal() as session:
                    items = list_recipe_ingredients(session, recipe_id)

                    if not items:
                        print("No ingredients found for this recipe.")
                    else:
                        print("\nIngredients for recipe", recipe_id)

                        for item in items:
                            print(
                "Ingredient ID:", item.ingredient_id,
                "| Quantity:", item.quantity,
                "| Unit:", item.unit,
)

            except ValueError:
                print("Please enter a valid recipe ID.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "3":
            try:
                recipe_id = int(input("Enter recipe ID: "))
                ingredient_id = int(input("Enter ingredient ID: "))
                quantity = Decimal(input("Enter new quantity: "))
                unit = input("Enter new unit: ").strip()

                if quantity <= 0 or not unit:
                    print("Quantity must be positive and unit cannot be empty.")
                    continue

                with SessionLocal.begin() as session:
                    item = update_recipe_ingredient(
                        session,
                        recipe_id,
                        ingredient_id,
                        quantity,
                        unit,
)

                    updated = item is not None

                if updated:
                    print("Recipe ingredient updated successfully!")
                else:
                    print("Recipe ingredient not found.")

            except (ValueError, InvalidOperation):
                print("Please enter valid numbers and quantity.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "4":
            try:
                recipe_id = int(input("Enter recipe ID: "))
                ingredient_id = int(input("Enter ingredient ID: "))

                with SessionLocal.begin() as session:
                    deleted = delete_recipe_ingredient(
                        session,
                        recipe_id,
                        ingredient_id,
)

                if deleted:
                    print("Recipe ingredient deleted successfully!")
                else:
                    print("Recipe ingredient not found.")

            except ValueError:
                print("Please enter valid IDs.")
            except Exception as error:
                print("ERROR:", error)

        else:
            print("Invalid choice. Please try again.")