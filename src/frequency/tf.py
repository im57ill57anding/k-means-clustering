def compute_term_frequency(dict_data: dict, list_data: list):
    dict_answer: dict = {}
    list_data_length: int = len(list_data)

    for word, amount in dict_data.items():
        dict_answer[word] = amount/float(list_data_length)

    print(
        f'dict_data: {dict_data}\n'
        f'list_data: {list_data}\n'
        f'term_frequency: {dict_answer}'
    )
    return dict_answer
