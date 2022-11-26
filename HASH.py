import hashlib

def getHashedPassword(password):
    hash = hashlib.md5(password.encode())
    return hash.hexdigest()
