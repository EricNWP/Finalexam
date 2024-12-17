from DietStrategy import DietStrategy
class DietCake(DietStrategy):
    def feed(self, weight):
        print("Executing cake diet. Feeding the cat cake for a day.")
        weight += 2
        return weight