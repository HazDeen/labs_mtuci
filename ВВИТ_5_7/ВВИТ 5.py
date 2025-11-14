class Book:

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def get_info(self) -> str:
        return f"Название книги: {self.title},Автор: {self.author},Год издания: {self.year}"

class Circle:

    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    def get_radius(self) -> int | float:
        return self.radius

    def set_radius(self, new_radius: int | float) -> None:
        self.radius = new_radius

circle_1 = Circle(23)
print(circle_1.get_radius())
circle_1.set_radius(10)
print(circle_1.get_radius())