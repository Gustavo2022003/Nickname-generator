from random import choice, randint

def generator_nickname(NSL_game, word, num):
    generated_nickname = [word]

    if len(word) == 0 and len(num) == 0: # if the user doesn't want to add any words or numbers
        count = 0
        while count < len(NSL_game):
            count += 1
            pre_load = f"{choice(NSL_game)}{choice(NSL_game)}_{randint(0, 999)}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load)

    elif len(word) == 0: # if the user doesn't want to add any words
        count = 0
        while count < len(NSL_game):
            count += 1
            pre_load = f"{choice(NSL_game)}{choice(NSL_game)}_{str(choice(num)).replace('[', '').replace(']', '')}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load)

    elif len(num) == 0: # if the user doesn't want to add any numbers
        count = 0
        while count < len(NSL_game):
            count += 1
            pre_load = f"{choice(NSL_game)}{choice(word)}_{randint(0, 999)}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load)
        
    elif len(word) > 1 and len(num) > 0: # if the user wants to add more than one word
        count = 0
        while count < len(NSL_game):
            count += 1
            pre_load = f"{choice(word)}{choice(word)}_{str(choice(num)).replace('[', '').replace(']', '')}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load)

    elif len(word) > 1 and len(num) == 0: # if the user wants to add more than one word but doesn't want to add any numbers
        count = 0
        while count < len(NSL_game):
            count += 1
            pre_load = f"{choice(word)}{choice(word)}_{randint(0, 999)}"
            if pre_load in generated_nickname:
                continue
            else:
                generated_nickname.append(pre_load)

    else:
        print("Error - unexpected input")

    return generated_nickname
