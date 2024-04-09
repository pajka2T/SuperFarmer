from util import bank

data = []


def create_users(n):
    for i in range(n):
        data.append(dict(rabbits=0, sheep=0, pigs=0, cows=0, horses=0, small_dogs=0, big_dogs=0))
    return data
# end def


def add_animals(user_id, res1, res2):
    if res1 == res2:
        if data[user_id][res1] == 0:
            data[user_id][res1] = min(1, bank[res1])
            bank[res1] = max(bank[res1] - 1, 0)
        else:
            data[user_id][res1] += min(2, bank[res1])
            bank[res1] -= min(2, bank[res1])
            reproduction = min(bank[res1], data[user_id][res1] // 2)
            data[user_id][res1] += reproduction
            bank[res1] -= reproduction
        return

    if res1 == "fox" or res2 == "fox":
        if data[user_id]["small_dogs"] > 0:
            data[user_id]["small_dogs"] -= 1
            bank["small_dogs"] += 1
        else:
            rabbits_to_bank = max(data[user_id]["rabbits"] - 1, 0)
            bank["rabbits"] += rabbits_to_bank
            data[user_id]["rabbits"] = min(data[user_id]["rabbits"], 1)
    if res1 == "wolf" or res2 == "wolf":
        if data[user_id]["big_dogs"] > 0:
            data[user_id]["big_dogs"] -= 1
            bank["big_dogs"] += 1
        else:
            sheep_to_bank = max(data[user_id]["sheep"] - 1, 0)
            bank["sheep"] += sheep_to_bank
            pigs_to_bank = max(data[user_id]["pigs"] - 1, 0)
            bank["pigs"] += pigs_to_bank
            cows_to_bank = max(data[user_id]["cows"] - 1, 0)
            bank["cows"] += cows_to_bank
            data[user_id]["sheep"] = 0
            data[user_id]["pigs"] = 0
            data[user_id]["cows"] = 0

    if res1 != "fox" and res1 != "wolf" and data[user_id][res1] > 0:
        data[user_id][res1] += min(1, bank[res1])
        bank[res1] -= min(1, bank[res1])
        reproduction = min(bank[res1], data[user_id][res1] // 2)
        data[user_id][res1] += reproduction
        bank[res1] -= reproduction
    if res2 != "fox" and res2 != "wolf" and data[user_id][res2] > 0:
        data[user_id][res2] += min(1, bank[res2])
        bank[res2] -= min(1, bank[res2])
        reproduction = min(bank[res2], data[user_id][res2] // 2)
        data[user_id][res2] += reproduction
        bank[res2] -= reproduction

    # print(data[user_id][res1], data[user_id][res2])
# end def


def buy_small_dog(user_id):
    if data[user_id]["sheep"] < 1:
        print("Masz za mało owiec, żeby kupić małego psa!");
        return
    data[user_id]["sheep"] -= 1
    data[user_id]["small_dogs"] += 1
# end def


def buy_big_dog(user_id):
    if data[user_id]["cows"] < 1:
        print("Masz za mało krów, żeby kupić dużego psa!")
        return
    data[user_id]["cows"] -= 1
    data[user_id]["big_dogs"] += 1
#end def

# def exchange_animals()