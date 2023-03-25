from random import choice, randint
import converToJson


def generator_nickname(NSL_game, word, num, total=10):
    generated_nickname = [word]

    if len(word) == 0 and len(num) == 0:  # if the user doesn't want to add any words or numbers
        count = 0
        while count < total:
            count += 1
            pre_load = f"{choice(NSL_game)}{choice(NSL_game)}_{randint(0, 999)}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load.capitalize())

    elif len(word) == 0:  # if the user doesn't want to add any words
        count = 0
        while count < total:
            count += 1
            pre_load = f"{choice(NSL_game)}{choice(NSL_game)}_{str(choice(num)).replace('[', '').replace(']', '')}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load.capitalize())

    elif len(num) == 0:  # if the user doesn't want to add any numbers
        count = 0
        while count < total:
            count += 1
            random_number = randint(0,1)
            if random_number == 1:
                pre_load = f"{choice(NSL_game)}{choice(word)}_{randint(0, 999)}"
            else:
                pre_load = f"{choice(word)}{choice(NSL_game)}_{randint(0, 999)}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load.capitalize())

    elif len(word) > 1 and len(num) > 0:  # if the user wants to add more than one word
        count = 0
        while count < total:
            count += 1
            pre_load = f"{choice(word)}{choice(word)}_{str(choice(num)).replace('[', '').replace(']', '')}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load.capitalize())

    # if the user wants to add more than one word but doesn't want to add any numbers
    elif len(word) > 1 and len(num) == 0:
        count = 0
        while count < total:
            count += 1
            pre_load = f"{choice(word)}{choice(word)}_{randint(0, 999)}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load.capitalize())

    else:
        print("Error - unexpected input")

    generated_nickname = generated_nickname[1:]
    converToJson.convertToJson(generated_nickname)
    return generated_nickname
