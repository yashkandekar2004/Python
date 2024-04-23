#write a python  code for email, url and password validation
import re

def validate_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(re.match(email_pattern, email))

def validate_url(url):
    url_pattern = re.compile(r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/?([^\s]*)$')
    return bool(re.match(url_pattern, url))

def validate_password(password):
   
    password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return bool(re.match(password_pattern, password))


email = "example@email.com"
url = "https://www.example.com"
password = "StrongP@ssword123"

if validate_email(email):
    print("Email is valid.")
else:
    print("Email is not valid.")

if validate_url(url):
    print("URL is valid.")
else:
    print("URL is not valid.")

if validate_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")