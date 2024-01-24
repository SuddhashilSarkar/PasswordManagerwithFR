import tkinter as tk
from encrypter import encrypt, decrypt, write_to_csv, read_from_csv, get_encryption_key

# Create the main window
root = tk.Tk()
root.geometry("800x600")
root.title("Password Manager")

# Call the function to get the encryption key
encryption_key = get_encryption_key()

if encryption_key:
    def store_password():
        # Function to switch to the password storage screen
        title_label.config(text="Store Password")
        button_frame.pack_forget()
        entry_frame.pack()
        platform_entry.delete(0, "end")
        user_id_entry.delete(0, "end")
        password_entry.delete(0, "end")

    def retrieve_password():
        # Function to switch to the password retrieval screen
        title_label.config(text="Retrieve Password")
        button_frame.pack_forget()
        search_frame.pack()
        platform_search_entry.delete(0, "end")

    def save_password():
        # Function to save the password to the database (CSV file)
        platform = platform_entry.get()
        user_id = user_id_entry.get()
        password = password_entry.get()
        data = (platform, user_id, password)
        write_to_csv('db.csv', data, encryption_key)
        entry_frame.pack_forget()
        button_frame.pack()

    def search_password():
        # Function to search for a password and display it
        platform_to_search = platform_search_entry.get()
        data = read_from_csv('db.csv', encryption_key)
        found = False
        for platform, user_id, password in data:
            if platform == platform_to_search:
                result_label.config(text=f"Platform: {platform}\nUser ID: {user_id}\nPassword: {password}")
                found = True
                break
        if not found:
            result_label.config(text="Platform not found in the database")

    # Create and configure labels
    title_label = tk.Label(root, text="Password Manager", font=("Helvetica", 20))
    title_label.pack(pady=20)

    # Create and configure button frame
    button_frame = tk.Frame(root)
    button_frame.pack()

    store_button = tk.Button(button_frame, text="Store Password", command=store_password)
    store_button.pack(pady=10)

    retrieve_button = tk.Button(button_frame, text="Retrieve Password", command=retrieve_password)
    retrieve_button.pack(pady=10)

    # Create and configure entry frame for password storage
    entry_frame = tk.Frame(root)
    platform_label = tk.Label(entry_frame, text="Platform Name:")
    platform_label.pack()
    platform_entry = tk.Entry(entry_frame)
    platform_entry.pack()

    user_id_label = tk.Label(entry_frame, text="User ID:")
    user_id_label.pack()
    user_id_entry = tk.Entry(entry_frame)
    user_id_entry.pack()

    password_label = tk.Label(entry_frame, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(entry_frame)
    password_entry.pack()

    save_button = tk.Button(entry_frame, text="Save Password", command=save_password)
    save_button.pack(pady=10)

    # Create and configure entry frame for password retrieval
    search_frame = tk.Frame(root)
    search_label = tk.Label(search_frame, text="Enter Platform:")
    search_label.pack()
    platform_search_entry = tk.Entry(search_frame)
    platform_search_entry.pack()

    search_button = tk.Button(search_frame, text="Search", command=search_password)
    search_button.pack(pady=10)

    result_label = tk.Label(search_frame, text="")
    result_label.pack()

root.mainloop()
