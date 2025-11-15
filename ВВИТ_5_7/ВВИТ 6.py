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
        return False

class Vehicle:

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"Марка машины: {self.make}, модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make: str, model: str, fuel_type:str):
        super().__init__(make,model) #вызываем конструктор базового класса
        self.fuel_type = fuel_type #новый атрибут 

    def get_info(self):
        return f"Марка машины: {self.make}, модель: {self.model}, тип топлива: {self.fuel_type}"


if __name__ == "__main__":
    user = UserAccount("arhip", "arh1p@mail.ru", "sadh-213s-3lrew-42kf")
    user.set_password("22031232")
    print(user.check_password("22031232"))

    car = Car("Mercedes", "G-Class", "Бензин")
    print(car.get_info())
