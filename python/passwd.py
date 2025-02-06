import bcrypt

password = b"password"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print("It matches!")
else:
    print("Didn't match")

