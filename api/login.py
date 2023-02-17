import sqlite3
import hashlib
import requests

# Initialize the database connection
conn = sqlite3.connect('logins.db')
c = conn.cursor()

# Create a table to store the login information
c.execute('CREATE TABLE IF NOT EXISTS logins (username TEXT, password TEXT)')

# Define a function to check if a password has been pwned
def check_password(password):
    hash_prefix = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()[:5]
    hash_suffix = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()[5:]
    url = f'https://api.pwnedpasswords.com/range/%7Bhash_prefix%7D'
    response = requests.get(url)
    if response.status_code == 200:
        hashes = response.text.splitlines()
        for hash in hashes:
            if hash.startswith(hash_suffix):
                return True
    return False

# Define a function to add a new login to the database
def add_login(username, password):
    # Check if the password is too common
    if check_password(password):
        print('This password has been pwned. Please choose a different one.')
        return
    # Add the login to the database
    c.execute('INSERT INTO logins (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    print('Login added successfully.')

# Define a function to check if a login exists in the database
def check_login(username, password):
    c.execute('SELECT * FROM logins WHERE username = ? AND password = ?', (username, password))
    return c.fetchone() is not None

# Close the database connection
conn.close()