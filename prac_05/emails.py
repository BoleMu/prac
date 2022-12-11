email_name = {}

email = input("Email: ")
email_name[email[:"@"]] = email["@":]
print(email_name)