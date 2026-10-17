import models

from ui.menu import show_main_menu, get_user_choice
from ui.users_menu import show_users_menu
from ui.user_profiles_menu import show_user_profiles_menu
from ui.categories_menu import show_categories_menu
from ui.ingredients_menu import show_ingredients_menu
from ui.recipes_menu import show_recipes_menu

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

        elif choice in ["6", "7"]:
            print("This section will be implemented soon.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

