import random

p1 = ["Cual fue el ultimo animal que creo dios?\nEl delfin\n", "delfin"]
p2 = ["El escorpion dorado es el dios del internet\n", "escorpion"]
p3 = ["Que se puede ver con los ojos cerrados?\nLa oscuridad\n", "oscuridad"]
p4 = ["Catarino y los rurales se agarraron a balazos\n", "Catarino"]
p5 = ["Cual es la palabra mas larga del diccionario?\nel arroz\n", "arroz"]
p6 = ["Tiene dientes y no come, tiene cabeza y no es hombre\najo\n", "ajo"]
p7 = ["El arbol bebe agua por los pies\n", "arbol"]
p8 = ["La planta del pie es la unica que no da ni hojas, ni flores, ni frutas.\n", "pie"]
p9 = ["Donde encontrarias el domingo antes que el sabado?\nEn el diccionario\n", "diccionario"]
p10 = ["Un caballo de color blanco se mete en el mar rojo. Cuando sale del agua, como esta?\nEsta mojado\n", "mojado"]

queries = {
    'p1': p1,
    'p2': p2,
    'p3': p3,
    'p4': p4,
    'p5': p5,
    'p6': p6,
    'p7': p7,
    'p8': p8,
    'p9': p9,
    'p10': p10
}

num_questions = len(queries)
# answered_questions = 0


def answer_replace(string, sub_string, tip_string):
    num_of_char = len(sub_string)
    if tip_string is not None:
        censored_wd = tip_string
    else:
        censored_wd = '_' * num_of_char

    return string.replace(sub_string, censored_wd)


# reveal characters and append to p list
def tip_answer(t_answer):
    # get the answer length of characters
    str_len = len(t_answer)
    # generate a random position in the answer and save the value
    char_position = random.randint(0, str_len)
    char = list(t_answer)[char_position]
    # censor answer and convert to list, then get replace the random character
    censored_wd = '_' * str_len
    censor = list(censored_wd)
    censor[char_position] = char
    # return censored list converted to string
    censored_wd = "".join(censor)
    return censored_wd


while num_questions != sum(value is None for value in queries.values()):
    for q in queries:
        if queries[q] is None:
            continue
        if len(queries[q]) == 3:
            hint = queries[q][2]
        else:
            hint = None
        answer = queries[q][1]
        query = answer_replace(queries[q][0], answer, hint)
        data = input(query)
        # Code to tip answers goes here:
        # if answered_questions > prev_answered:
        #     data = input(query + )
        if data == "":
            continue
        elif len(data) != len(answer) or data.lower() != answer.lower():
            print("Equivocacion!")
        elif data.lower() == answer.lower():
            print("Es correcto!!!\n")
            queries[q] = None
            if num_questions - sum(value is None for value in queries.values()) > 1:
                # get random answer - queries[pn][1] to tip answer
                random_queries_element = random.choice(list(queries))
                while queries[random_queries_element] is None:
                    random_queries_element = random.choice(list(queries))
                else:
                    # print("random key: " + random_queries_element)
                    if len(queries[random_queries_element]) == 3:
                        # print("length: " + str(len(queries[random_queries_element])))
                        # print(queries[random_queries_element][2])
                        true_answer = queries[random_queries_element][1]
                        tmp_answer = queries[random_queries_element][2]
                        random_element = random.randint(0, len(tmp_answer))
                        discovered_chars = []
                        for c in tmp_answer:
                            if c != '_':
                                # tmp_answer.index(c)
                                discovered_chars.append(tmp_answer.index(c))
                        while random_element in discovered_chars:
                            random_element = random.randint(0, len(tmp_answer))
                        tmp_lst_answer = list(tmp_answer)
                        # tmp_lst_answer[random_element] = list(true_answer)[random_element]
                        tmp_lst_answer[random_element] = list(queries[random_queries_element][1])[random_element]
                        tmp_answer = "".join(tmp_lst_answer)
                        # print(tmp_answer)
                        queries[random_queries_element][2] = tmp_answer
                    else:
                        tip = tip_answer(queries[random_queries_element][1])
                        # print(tip)
                        queries[random_queries_element].append(tip)

print("Ganaste!")
# print(tip_answer('perro'))
