from DietStrategy import DietStrategy
class DietKeto(DietStrategy):
    def feed(self, weight):
        print("Executing keto diet. Feeding the cat keto food for a day.")
        weight -= 1
        return weight