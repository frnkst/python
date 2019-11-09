import getpass
import hashlib
import requests

user_password = getpass.getpass('Enter password you want to check: ')
hashed_user_password = hashlib.sha1(user_password.encode()).hexdigest().upper()
response = requests.get("https://api.pwnedpasswords.com/range/" + hashed_user_password[:5])

for pawned_hash in response.content.splitlines():
    hash_string, amount = pawned_hash.decode().split(":")
    if hashed_user_password[:5] + hash_string == hashed_user_password:
        print("Password found in %s breaches" % amount)
