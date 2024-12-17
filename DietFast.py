from DietStrategy import DietStrategy
class DietFast(DietStrategy):
    def feed(self, weight):
        print("Executing fasting diet. The cat will not eat for a day.")
        weight -= 3
        return weight
