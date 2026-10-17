from database.connection import SessionLocal

from services.recipes import (
    create_recipe,
    get_recipe,
    list_recipes,
    update_recipe,
    delete_recipe
)

def show_recipes_menu():
    while True:
        print("\n===== MANAGE RECIPES =====")
        print("1. Add Recipe")
        print("2. List Recipes")
        print("3. View Recipe")
        print("4. Update Recipe")
        print("0. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            try:
                user_id = int(input("Enter user ID: "))
                category_id = int(input("Enter category ID: "))
                title = input("Enter recipe title: ").strip()
                instructions = input("Enter instructions: ").strip()
                prep_time = int(input("Enter preparation time (minutes): "))

                if not title or not instructions:
                    print("Title and instructions cannot be empty.")
                    continue

                if prep_time < 0:
                    print("Preparation time cannot be negative.")
                    continue

                with SessionLocal.begin() as session:
                    recipe = create_recipe(
                        session,
                        user_id,
                        category_id,
                        title,
                        instructions,
                        prep_time,
)
                    recipe_id = recipe.id

                print("Recipe created! ID:", recipe_id)

            except ValueError:
                print("Please enter valid numbers.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "2":
            try:
                with SessionLocal() as session:
                    recipes = list_recipes(session)

                    if not recipes:
                        print("No recipes found.")

                    for recipe in recipes:
                        print(recipe.id, "-", recipe.title)

            except Exception as error:
                print("ERROR:", error)

        elif choice == "3":
            try:
                recipe_id = int(input("Enter recipe ID: "))

                with SessionLocal() as session:
                    recipe = get_recipe(session, recipe_id)

                    if recipe is None:
                        print("Recipe not found.")
                    else:
                        print("ID:", recipe.id)
                        print("Title:", recipe.title)
                        print("User ID:", recipe.user_id)
                        print("Category ID:", recipe.category_id)
                        print("Instructions:", recipe.instructions)
                        print("Preparation Time:", recipe.prep_time_minutes)

            except ValueError:
                print("Please enter a valid recipe ID.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "4":
            try:
                recipe_id = int(input("Enter recipe ID: "))
                title = input("Enter new title: ").strip()
                instructions = input("Enter new instructions: ").strip()
                prep_time = int(input("Enter new preparation time: "))

                if not title or not instructions or prep_time < 0:
                    print("Invalid recipe information.")
                    continue

                with SessionLocal.begin() as session:
                    updated_recipe = update_recipe(
                    session,
                    recipe_id,
                    title,
                    instructions,
                    prep_time,
)
                    updated = updated_recipe is not None

                if updated:
                    print("Recipe updated successfully!")
                else:
                    print("Recipe not found.")

            except ValueError:
                print("Please enter valid numbers.")
            except Exception as error:
                print("ERROR:", error)
        elif choice == "5":
            try:
                recipe_id = int(input("Enter recipe ID: "))

                with SessionLocal.begin() as session:
                    deleted = delete_recipe(session, recipe_id)

                if deleted:
                    print("Recipe deleted successfully!")
                else:
                    print("Recipe not found.")

            except ValueError:
                print("Please enter a valid recipe ID.")
            except Exception as error:
                print("ERROR:", error)
        else:
            print("Invalid choice.")