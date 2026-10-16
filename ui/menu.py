def show_main_menu():
    print("\n" + "=" * 40)
    print(" RECIPEBOX")
    print("=" * 40)

    print("1. Manage Users")
    print("2. Manage User Profiles")
    print("3. Manage Categories")
    print("4. Manage Ingredients")
    print("5. Manage Recipes")
    print("6. Manage Recipe Ingredients")
    print("7. Manage Favorites")
    print("0. Exit")

    print("=" * 40)

def get_user_choice():
    return input("Enter your choice: ").strip()