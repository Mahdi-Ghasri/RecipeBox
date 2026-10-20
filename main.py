import models

from ui.favorites_menu import show_favorites_menu
from ui.menu import show_main_menu, get_user_choice
from ui.users_menu import show_users_menu
from ui.user_profiles_menu import show_user_profiles_menu
from ui.categories_menu import show_categories_menu
from ui.ingredients_menu import show_ingredients_menu
from ui.recipes_menu import show_recipes_menu
from ui.recipe_ingredients_menu import show_recipe_ingredients_menu

def main():
    while True:
        show_main_menu()
        choice = get_user_choice()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            show_users_menu()

        elif choice == "2":
            show_user_profiles_menu()

        elif choice == "3":
            show_categories_menu()

        elif choice == "4":
            show_ingredients_menu()

        elif choice == "5":
            show_recipes_menu()

        elif choice == "6":
            show_recipe_ingredients_menu()


        elif choice == "7":
            show_favorites_menu()

        else:
            print("Invalid choice, please try agin.")

if __name__ == "__main__":
    main()

