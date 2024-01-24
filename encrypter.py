import csv
import base64
from cryptography.fernet import Fernet

def get_encryption_key():
  return b'HAV9QuNgulhb8gTlffbcvsZzK-Fa8zlSdquwT7B9Dlk='

def encrypt(text, key):
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    return encrypted_text

def decrypt(encrypted_text, key):
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_text).decode()
    return decrypted_text

def write_to_csv(filename, data, key):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        platform, id, password = data
        encrypted_platform = encrypt(platform, key)
        encrypted_id = encrypt(id, key)
        encrypted_password = encrypt(password, key)
        writer.writerow([base64.b64encode(encrypted_platform).decode(), base64.b64encode(encrypted_id).decode(), base64.b64encode(encrypted_password).decode()])

def read_from_csv(filename, key):
    results = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            encrypted_platform, encrypted_id, encrypted_password = row
            platform = decrypt(base64.b64decode(encrypted_platform), key)
            id = decrypt(base64.b64decode(encrypted_id), key)
            password = decrypt(base64.b64decode(encrypted_password), key)
            results.append((platform, id, password))
    return results

if __name__ == "__main__":
    # Replace 'your_generated_key_here' with the actual generated Fernet key
    encryption_key = b'HAV9QuNgulhb8gTlffbcvsZzK-Fa8zlSdquwT7B9Dlk='

    data_to_store = [
        ("Platform1", "12345", "Password1"),
        ("Platform2", "67890", "Password2"),
        # Add more platform, ID, and password tuples as needed
    ]

    csv_filename = "db.csv"

    for item in data_to_store:
        write_to_csv(csv_filename, item, encryption_key)

    # Reading from the CSV file
    stored_data = read_from_csv(csv_filename, encryption_key)
    for platform, id, password in stored_data:
        print("Platform:", platform)
        print("ID:", id)
        print("Password:", password)
