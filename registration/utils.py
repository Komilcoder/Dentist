import re


pattern = r'example@gmail.com'



def is_email_valid(email):
    if not email:
        return False,"Please provide email"
    if not re.match(pattern, email):
        return False,"Please make sure email is correct"
    return True,email


