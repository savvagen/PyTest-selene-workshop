
class User(object):
    def __init__(self, email, password, firstname="", lastname=""):
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
