import getpass
import hashlib
import requests

user_password = getpass.getpass('Enter password you want to check: ')
hashed_user_password = hashlib.sha1(user_password.encode()).hexdigest().upper()
hashed_user_password_beginning = hashed_user_password[:5]

response = requests.get("https://api.pwnedpasswords.com/range/" + hashed_user_password_beginning)

for line in response.content.splitlines():
    pawned_hash, number_of_breaches = line.decode().split(":")
    if hashed_user_password_beginning + pawned_hash == hashed_user_password:
        print("Password found in %s breaches" % number_of_breaches)
