class UserAccount:

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password: str) -> None:
        self.__password = new_password

    def check_password(self, password: str) -> bool:
        if password == self.__password:
            return True
        else:
            return False

class Users:
    usr_1 = UserAccount('Kirill', 'example@gmail.com', 'qwerty_1234567890')

Users.usr_1.set_password("Mte-Tes-Uf2-S04-I2q")
print(Users.usr_1.check_password('1234')) #False
print(Users.usr_1.check_password('Mte-Tes-Uf2-S04-I2q')) #True

