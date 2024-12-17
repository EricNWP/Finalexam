from Cat import Cat
from DietCake import DietCake
from DietKeto import DietKeto
from DietFast import DietFast
from DietNormal import DietNormal

cake = DietCake()
keto = DietKeto()
fast = DietFast()
normal = DietNormal()

fluffles = Cat("Fluffles", "Tabby", 10)

if (fluffles.get_weight() > 25):
    fluffles.set_diet(fast)

elif (fluffles.get_weight() > 15):
    fluffles.set_diet(keto)

elif (fluffles.get_weight() < 8):
    fluffles.set_diet(cake)

else:
    fluffles.set_diet(normal)

fluffles.feed()