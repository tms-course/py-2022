class Auto:
    def __init__(
            self, 
            brand: str, 
            age: int, 
            mark: str, 
            color: str = None, 
            weight: float = None
    ) -> None:
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self) -> None:
        print('move')

    def birthday(self) -> None:
        self.age += 1

    def stop(self) -> None:
        print('stop')