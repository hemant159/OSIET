from app.dialogs import open_file_dialog

def get_user_input():
    choice = input("Enter 1").strip()

    if choice == '1':
        print("Opening file manager. Please select an image file.")
        file_path = open_file_dialog()
        
        if file_path:
            print(f"File selected: {file_path}")
        else:
            print("No file selected.")
    elif choice == '2':
        print("Opening file manager. Please select multiple image files.")
        file_paths = open_file_dialog(multiple=True)

        if file_paths:
            print(f"Files selected: {', '.join(file_paths)}")

        else:
            print("No files selected.")

    else:
        print("Invalid choice. Please enter either 1 or 2.")
