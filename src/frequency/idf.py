import math


def compute_inverse_data_frequency(documents: list):
    n: int = len(documents)
    dict_answer: dict = dict.fromkeys(documents[0].keys(), 0)

    for document in documents:
        for word, val in document.items():
            if val > 0:
                dict_answer[word] += 1

    for word, val in dict_answer.items():
        dict_answer[word] = int(math.log(n/float(val)))

    print(
        f'first: {documents[0]}\n'
        f'second: {documents[1]}\n'
        f'answer: {dict_answer}'
    )
    return dict_answer
