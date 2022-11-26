class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserEntity:
    def __init__(self, username, password, email, address, job, phoneNumber):
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.job = job
        self.phoneNumber = phoneNumber

class UserLoginDto:
    def __init__(self, username, password):
        self.username = username
        self.password = password