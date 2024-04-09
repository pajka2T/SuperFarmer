data = []


def create_users(n):
    for i in range(n):
        data.append(dict(rabbits=0, sheep=0, pigs=0, cows=0, horses=0, small_dogs=0, large_dogs=0))
    return data
# end def


def add_animals(user_id, res1, res2):
    if res1 == res2 and data[user_id][res1] == 0:
        data[user_id][res1] = 1
        return
    data[user_id][res1] += 1
    data[user_id][res2] += 1

    print(data[user_id][res1], data[user_id][res2])

    data[user_id][res1] += data[user_id][res1] // 2
    data[user_id][res2] += data[user_id][res2] // 2
# end def


# def exchange_animals()