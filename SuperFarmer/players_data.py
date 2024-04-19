from util import bank, Predators
from util import Animal
from util import Defence

# data = []


class Player:
    def __init__(self, id):
        self.id = id
        self.animals = {Animal.RABBIT: 0, Animal.SHEEP: 0, Animal.PIG: 0, Animal.COW: 0, Animal.HORSE: 0}
        self.dogs = {Defence.SMALLDOG: 0, Defence.BIGDOG: 0}

    def add_animals(self, animal1, animal2):
        print(animal1, animal2)

        # Oba zwierzęta są hodowlane
        if isinstance(animal1, Animal) and isinstance(animal2, Animal):
            if animal1 == animal2:
                if self.animals[animal1] == 0:
                    self.animals[animal1] = min(1, bank[animal1])
                    bank[animal1] = max(bank[animal1] - 1, 0)
                else:
                    self.animals[animal1] += min(2, bank[animal1])
                    bank[animal1] -= min(2, bank[animal1])
                    reproduction = min(bank[animal1], self.animals[animal1] // 2)
                    self.animals[animal1] += reproduction
                    bank[animal1] -= reproduction
                return
        if isinstance(animal1, Animal) and self.animals[animal1] > 0:
            print("Trzeci")
            self.animals[animal1] += min(1, bank[animal1])
            bank[animal1] -= min(1, bank[animal1])
            reproduction = min(bank[animal1], self.animals[animal1] // 2)
            self.animals[animal1] += reproduction
            bank[animal1] -= reproduction
        if isinstance(animal2, Animal) and self.animals[animal2] > 0:
            print("Czwarty")
            self.animals[animal2] += min(1, bank[animal2])
            bank[animal2] -= min(1, bank[animal2])
            reproduction = min(bank[animal2], self.animals[animal2] // 2)
            self.animals[animal2] += reproduction
            bank[animal2] -= reproduction

        # Sprawdzenie, czy zwierzęta nie są drapieżnikami
        if animal1 == Predators.FOX or animal2 == Predators.FOX:
            print("Drugi")
            if self.dogs[Defence.SMALLDOG] > 0:
                self.dogs[Defence.SMALLDOG] -= 1
                bank[Defence.SMALLDOG] += 1
            else:
                rabbits_to_bank = max(self.animals[Animal.RABBIT] - 1, 0)
                bank[Animal.RABBIT] += rabbits_to_bank
                self.animals[Animal.RABBIT] = min(self.animals[Animal.RABBIT], 1)
        if animal1 == Predators.WOLF or animal2 == Predators.WOLF:
            if self.dogs[Defence.BIGDOG] > 0:
                self.dogs[Defence.BIGDOG] -= 1
                bank[Defence.BIGDOG] += 1
            else:
                sheep_to_bank = max(self.animals[Animal.SHEEP] - 1, 0)
                bank[Animal.SHEEP] += sheep_to_bank
                pigs_to_bank = max(self.animals[Animal.PIG] - 1, 0)
                bank[Animal.PIG] += pigs_to_bank
                cows_to_bank = max(self.animals[Animal.COW] - 1, 0)
                bank[Animal.COW] += cows_to_bank
                self.animals[Animal.SHEEP] = 0
                self.animals[Animal.PIG] = 0
                self.animals[Animal.COW] = 0

        print(self.animals)
        return

    def buy_small_dog(self):
        if self.animals[Animal.SHEEP] < 1:
            print("Masz za mało owiec, żeby kupić małego psa!");
            return
        self.animals[Animal.SHEEP] -= 1
        self.dogs[Defence.SMALLDOG] += 1

    # end def

    def buy_big_dog(self):
        if self.animals[Animal.COW] < 1:
            print("Masz za mało krów, żeby kupić dużego psa!")
            return
        self.animals[Animal.COW] -= 1
        self.dogs[Defence.BIGDOG] += 1
    # end def
# end class


def create_users(n):
    players = []
    for i in range(1, n+1):
        newPlayer = Player(i)
        players.append(newPlayer)
    return players
# end def


#def exchange_animals(user_id, animal1, animal2):
