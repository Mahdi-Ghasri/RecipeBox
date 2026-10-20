from sqlalchemy.exc import IntegrityError

from database.connection import SessionLocal

from services.favorites import (
add_favorite,
get_favorite,
list_user_favorites,
list_recipe_favorites,
delete_favorite,
)

def show_favorites_menu():
    while True:
        print("\n===== MANAGE FAVORITES =====")
        print("1. Add Favorite")
        print("2. List User Favorites")
        print("3. List Recipe Favorites")
        print("4. Delete Favorite")
        print("0. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            try:
                user_id = int(input("Enter user ID: "))
                recipe_id = int(input("Enter recipe ID: "))

                with SessionLocal.begin() as session:
                    existing = get_favorite(
                    session,
                    user_id,
                    recipe_id,
)

                    if existing is not None:
                        print("This recipe is already in favorites.")
                        continue

                    favorite = add_favorite(
                    session,
                    user_id,
                    recipe_id,
)

                    saved_user_id = favorite.user_id
                    saved_recipe_id = favorite.recipe_id

                print("Favorite added successfully!")
                print("User ID:", saved_user_id)
                print("Recipe ID:", saved_recipe_id)

            except ValueError:
                print("Please enter valid IDs.")
            except IntegrityError:
                print("Could not add favorite. Check the user and recipe IDs.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "2":
            try:
                user_id = int(input("Enter user ID: "))

                with SessionLocal() as session:
                    favorites = list_user_favorites(
                        session,
                        user_id,
    )

                    if not favorites:
                        print("No favorites found for this user.")
                    else:
                        print("\nFavorites for user", user_id)

                        for favorite in favorites:
                            print("Recipe ID:", favorite.recipe_id)

            except ValueError:
                print("Please enter a valid user ID.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "3":
            try:
                recipe_id = int(input("Enter recipe ID: "))

                with SessionLocal() as session:
                    favorites = list_recipe_favorites(
                        session,
                        recipe_id,
)

                if not favorites:
                    print("No users have favorited this recipe.")
                else:
                    print("\nUsers who favorited recipe", recipe_id)

                    for favorite in favorites:
                        print("User ID:", favorite.user_id)

            except ValueError:
                print("Please enter a valid recipe ID.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "4":
            try:
                user_id = int(input("Enter user ID: "))
                recipe_id = int(input("Enter recipe ID: "))

                with SessionLocal.begin() as session:
                    deleted = delete_favorite(
                        session,
                        user_id,
                        recipe_id,
)

                if deleted:
                    print("Favorite deleted successfully!")
                else:
                    print("Favorite not found.")

            except ValueError:
                print("Please enter valid IDs.")
            except Exception as error:
                print("ERROR:", error)

        else:
            print("Invalid choice. Please try again.")