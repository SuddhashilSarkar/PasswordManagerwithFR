from cryptography.fernet import Fernet

def generate_fernet_key():
    return Fernet.generate_key()

key = generate_fernet_key()
print("Generated Fernet Key:", key.decode())

# Save the generated key to a text file
with open("fernet_key.txt", "wb") as key_file:
    key_file.write(key)

print("Fernet Key saved to 'fernet_key.txt'")
