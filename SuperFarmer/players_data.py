from util import Animal, Bank, Defence, Predators, exchange_cost


class Player:
    """
    Class responsible for storing all player data.
    """
    def __init__(self, id: int) -> None:
        self.id = id
        self.animals = {
            Animal.RABBIT: 0,
            Animal.SHEEP: 0,
            Animal.PIG: 0,
            Animal.COW: 0,
            Animal.HORSE: 0,
        }
        self.dogs = {Defence.SMALLDOG: 0, Defence.BIGDOG: 0}

    def add_animals(
        self, animal1: Animal, animal2: Animal, bank: Bank
    ) -> tuple[str, str]:
        """
        Function adding animals to the player bank.
        :param animal1:
        :param animal2:
        :param bank:
        :return:
        """
        print(animal1, animal2)

        if (
            isinstance(animal1, Animal)
            and isinstance(animal2, Animal)
            and animal1 == animal2
        ):
            if self.animals[animal1] == 0:
                self.animals[animal1] = min(1, bank.animals[animal1])
                bank.animals[animal1] = max(bank.animals[animal1] - 1, 0)
            else:
                self.animals[animal1] += min(2, bank.animals[animal1])
                bank.animals[animal1] -= min(2, bank.animals[animal1])
                reproduction = min(bank.animals[animal1], self.animals[animal1] // 2)
                self.animals[animal1] += reproduction
                bank.animals[animal1] -= reproduction
            return "OK", "OK"
        if isinstance(animal1, Animal) and self.animals[animal1] > 0:
            self.animals[animal1] += min(1, bank.animals[animal1])
            bank.animals[animal1] -= min(1, bank.animals[animal1])
            reproduction = min(bank.animals[animal1], self.animals[animal1] // 2)
            self.animals[animal1] += reproduction
            bank.animals[animal1] -= reproduction
        if isinstance(animal2, Animal) and self.animals[animal2] > 0:
            self.animals[animal2] += min(1, bank.animals[animal2])
            bank.animals[animal2] -= min(1, bank.animals[animal2])
            reproduction = min(bank.animals[animal2], self.animals[animal2] // 2)
            self.animals[animal2] += reproduction
            bank.animals[animal2] -= reproduction

        return_info_1 = "OK"
        return_info_2 = "OK"

        if animal1 == Predators.FOX or animal2 == Predators.FOX:
            if self.dogs[Defence.SMALLDOG] > 0:
                self.dogs[Defence.SMALLDOG] -= 1
                bank.dogs[Defence.SMALLDOG] += 1
                return_info_1 = Defence.SMALLDOG
            else:
                rabbits_to_bank = max(self.animals[Animal.RABBIT] - 1, 0)
                bank.animals[Animal.RABBIT] += rabbits_to_bank
                self.animals[Animal.RABBIT] = min(self.animals[Animal.RABBIT], 1)
                return_info_1 = Predators.FOX
        if animal1 == Predators.WOLF or animal2 == Predators.WOLF:
            if self.dogs[Defence.BIGDOG] > 0:
                self.dogs[Defence.BIGDOG] -= 1
                bank.dogs[Defence.BIGDOG] += 1
                return_info_2 = Defence.BIGDOG
            else:
                sheep_to_bank = self.animals[Animal.SHEEP]
                bank.animals[Animal.SHEEP] += sheep_to_bank
                pigs_to_bank = self.animals[Animal.PIG]
                bank.animals[Animal.PIG] += pigs_to_bank
                cows_to_bank = self.animals[Animal.COW]
                bank.animals[Animal.COW] += cows_to_bank
                self.animals[Animal.SHEEP] = 0
                self.animals[Animal.PIG] = 0
                self.animals[Animal.COW] = 0
                return_info_2 = Predators.WOLF

        return return_info_1, return_info_2

    # end def

    def buy_small_dog(self, bank: Bank) -> int:
        """
        Function which allows player to buy a small dog.
        :param bank:
        :return:
        """
        if self.animals[Animal.SHEEP] < 1:
            return -1
        if bank.dogs[Defence.SMALLDOG] <= 0:
            return -2
        self.animals[Animal.SHEEP] -= 1
        self.dogs[Defence.SMALLDOG] += 1
        bank.dogs[Defence.SMALLDOG] -= 1
        return 1

    # end def

    def buy_big_dog(self, bank: Bank) -> int:
        """
            Function which allows player to buy a big dog.
            :param bank:
            :return:
        """
        if self.animals[Animal.COW] < 1:
            return -1
        if bank.dogs[Defence.BIGDOG] <= 0:
            return -2
        self.animals[Animal.COW] -= 1
        self.dogs[Defence.BIGDOG] += 1
        bank.dogs[Defence.BIGDOG] -= 1
        return 1

    # end def

    def exchange_animals(
        self,
        animal_from: Animal,
        no_animals_to_exchange: int,
        animal_to: Animal,
        bank: Bank,
    ) -> int:
        """
        Function allowing player to exchange animals.
        :param animal_from:
        :param no_animals_to_exchange:
        :param animal_to:
        :param bank:
        :return:
        """
        if not isinstance(animal_from, Animal) or not isinstance(animal_to, Animal):
            return -1

        if animal_to in exchange_cost[animal_from]:
            if no_animals_to_exchange < exchange_cost[animal_from][animal_to]:
                return -2

            no_new_animals = min(
                no_animals_to_exchange // exchange_cost[animal_from][animal_to],
                bank.animals[animal_to],
            )
            self.animals[animal_to] += no_new_animals
            bank.animals[animal_to] -= no_new_animals
            self.animals[animal_from] -= (
                no_new_animals * exchange_cost[animal_from][animal_to]
            )
            bank.animals[animal_from] += (
                no_new_animals * exchange_cost[animal_from][animal_to]
            )
            if no_new_animals <= 0:
                return 2
            return 1
        else:
            no_new_animals = min(
                no_animals_to_exchange * exchange_cost[animal_to][animal_from],
                bank.animals[animal_to],
            )
            self.animals[animal_to] += no_new_animals
            bank.animals[animal_to] -= no_new_animals
            self.animals[animal_from] -= (
                no_new_animals // exchange_cost[animal_to][animal_from]
            )
            bank.animals[animal_from] += (
                no_new_animals // exchange_cost[animal_to][animal_from]
            )
            if no_new_animals <= 0:
                return 2
            return 1

    # end def


# end class


def create_players(n: int) -> list[Player]:
    """
    Function creating list of players.
    :param n:
    :return:
    """
    players = []
    for i in range(0, n):
        new_player = Player(i)
        players.append(new_player)
    return players


# end def
