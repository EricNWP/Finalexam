from DietStrategy import DietStrategy
class DietNormal(DietStrategy):
    def feed(self, weight):
        print("Executing normal diet. Feeding the cat normal food for a day.")
        return weight