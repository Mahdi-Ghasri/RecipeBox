from database.connection import SessionLocal

from services.user_profiles import (
    create_user_profile,
    get_user_profile,
    list_user_profiles,
    update_user_profile,
    delete_user_profile,
)

def show_user_profiles_menu():
    while True:
        print("\n===== MANAGE USER PROFILES =====")
        print("1. Add Profile")
        print("2. List Profiles")
        print("3. View Profile")
        print("4. Update Profile")
        print("5. Delete Profile")
        print("0. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            try:
                user_id = int(input("Enter user ID: "))
                full_name = input("Enter full name: ").strip()
                avatar_url = input("Enter avatar URL (optional): ").strip()
                bio = input("Enter bio (optional): ").strip()

                if not full_name:
                    print("Full name cannot be empty.")
                    continue

                with SessionLocal.begin() as session:
                    profile = create_user_profile(
                                            session,
                                            user_id,
                                            full_name,
                                            avatar_url or None,
                                            bio or None,
)
                    saved_id = profile.user_id

                print("Profile created! User ID:", saved_id)

            except ValueError:
                print("Please enter a valid user ID.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "2":
            try:
                with SessionLocal() as session:
                    profiles = list_user_profiles(session)

                    if not profiles:
                        print("No profiles found.")

                    for profile in profiles:
                        print(profile.user_id, "-", profile.full_name)

            except Exception as error:
                print("ERROR:", error)

        elif choice == "3":
            try:
                user_id = int(input("Enter user ID: "))

                with SessionLocal() as session:
                    profile = get_user_profile(session, user_id)

                    if profile is None:
                        print("Profile not found.")
                    else:
                        print("User ID:", profile.user_id)
                        print("Full Name:", profile.full_name)
                        print("Avatar:", profile.avatar_url)
                        print("Bio:", profile.bio)

            except ValueError:
                print("Please enter a valid user ID.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "4":
            try:
                user_id = int(input("Enter user ID: "))
                full_name = input("Enter new full name: ").strip()
                avatar_url = input("Enter new avatar URL: ").strip()
                bio = input("Enter new bio: ").strip()

                if not full_name:
                    print("Full name cannot be empty.")
                    continue

                with SessionLocal.begin() as session:
                    profile = update_user_profile(
                        session,
                        user_id,
                        full_name,
                        avatar_url or None,
                        bio or None,
)
                    updated = profile is not None

                if updated:
                    print("Profile updated successfully!")
                else:
                    print("Profile not found.")

            except ValueError:
                print("Please enter a valid user ID.")
            except Exception as error:
                print("ERROR:", error)

        elif choice == "5":
            try:
                user_id = int(input("Enter user ID: "))

                with SessionLocal.begin() as session:
                    deleted = delete_user_profile(session, user_id)

                if deleted:
                    print("Profile deleted successfully!")
                else:
                    print("Profile not found.")

            except ValueError:
                print("Please enter a valid user ID.")
            except Exception as error:
                print("ERROR:", error)

        else:
            print("Invalid choice.")