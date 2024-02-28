words = ["email@gmail.com", "email@hotmail.com", "email[at]yahoo.com"]
not_email = [word for word in words if "@" not in word]

print(not_email)