class Cat:
    def __init__(self, name, fur, weight):
        self.__name = name
        self.__fur = fur
        self.__weight = weight
        self.__diet = None

    def set_diet(self, newDiet):
        self.__diet = newDiet
    
    def feed(self):
        self.__weight = self.__diet.feed(self.__weight)

    def get_weight(self):
        return self.__weight