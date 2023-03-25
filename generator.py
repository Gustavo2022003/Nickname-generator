from random import choice, randint
import converToJson


def generator_nickname(NSL_game, word, num, total=10):
    generated_nickname = [word]

    if len(word) == 0 and len(num) == 0:  # if the user doesn't want to add any words and numbers
        count = 0
        while count < total:
            count += 1
            random_number = randint(0,1)
            if random_number == 0:
                pre_load = f"{choice(NSL_game)}{choice(NSL_game)}"
            else:
                pre_load = f"{choice(NSL_game)}_{choice(NSL_game)}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load.capitalize())

    elif len(word) == 0:  # if the user doesn't want to add any words
        count = 0
        while count < total:
            count += 1
            random_number = randint(0,3)
            if random_number == 0:
                pre_load = f"{choice(NSL_game)}{choice(NSL_game)}_{str(choice(num)).replace('[', '').replace(']', '')}"
            elif random_number == 1:
                pre_load = f"{choice(NSL_game)}_{choice(NSL_game)}_{str(choice(num)).replace('[', '').replace(']', '')}"
            elif random_number == 2:
                pre_load = f"{choice(NSL_game)}{choice(NSL_game)}{str(choice(num)).replace('[', '').replace(']', '')}"
            else:
                pre_load = f"{choice(NSL_game)}_{choice(NSL_game)}{str(choice(num)).replace('[', '').replace(']', '')}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load.capitalize())

    elif len(num) == 0:  # if the user doesn't want to add any numbers
        count = 0
        while count < total:
            count += 1
            random_number = randint(0,3)
            if random_number == 0:
                pre_load = f"{choice(NSL_game)}{choice(word)}"
            elif random_number == 1:
                pre_load = f"{choice(word)}{choice(NSL_game)}"
            elif random_number == 2:
                pre_load = f"{choice(word)}_{choice(NSL_game)}"
            else:
                pre_load = f"{choice(NSL_game)}_{choice(word)}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load.capitalize())

    elif len(word) > 1 and len(num) > 0:  # if the user wants to add more than one word and one number
        count = 0
        while count < total:
            count += 1
            random_number = randint(0,3)
            if random_number == 0:
                pre_load = f"{choice(word)}{choice(word)}"
            elif random_number == 1:
                pre_load = f"{choice(word)}_{choice(word)}"
            elif random_number == 2:
                pre_load = f"{choice(word)}{choice(word)}_{choice(num)}"
            else:
                pre_load = f"{choice(word)}{choice(word)}{choice(num)}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load.capitalize())


    # if the user wants to add more than one word and any numbers
    elif len(word) > 1 and len(num) > 1:
        count = 0
        while count < total:
            count += 1
            pre_load = f"{choice(word)}{choice(word)}_{choice(num)}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load.capitalize())

    else:
        print("Error - unexpected input")

    generated_nickname = generated_nickname[1:]
    converToJson.convertToJson(generated_nickname)
    return generated_nickname
