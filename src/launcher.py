import re

from src.frequency import idf, tf
from src.clustering import k_means_clustering

def pre_calculation(data: str) -> list:
    deleted_symbols: str = str(re.split(', |\\|_|-|!', data.lower()))
    list_for_data: list = deleted_symbols.split(' ')
    unique_data: set = set(list_for_data)
    dict_for_data: dict = dict.fromkeys(unique_data, 0)

    print(
        f'size: {len(unique_data)}\n'
        f'data: {unique_data}'
    )

    for now in list_for_data:
        dict_for_data[now] += 1

    print(f'stored: {dict_for_data}')
    return [dict_for_data, list_for_data]


def calculate_tf(data: str) -> dict:
    dict_for_data, list_for_data = pre_calculation(data)

    return tf.compute_term_frequency(dict_for_data, list_for_data)


def calculate_itf(data_1: str, data_2: str):
    dict_for_data_1: list = pre_calculation(data_1)[0]
    dict_for_data_2: list = pre_calculation(data_2)[0]

    return idf.compute_inverse_data_frequency([dict_for_data_1, dict_for_data_2])


def union_documents() -> str:
    all_in_one: str = ''

    for i in range(10):
        with open(f'docs/{i}.txt', 'r') as file:
            for item in file:
                all_in_one += str(item)

    return all_in_one


def calculate_k_means():
    all_in_one: str = union_documents()
    response: list = pre_calculation(all_in_one)

    dict_for_data: dict = response[0]
    list_for_data: list = response[1]
    dataset: list = []

    tf.compute_term_frequency(dict_for_data, list_for_data)
    idf.compute_inverse_data_frequency(list_for_data)

    for key, value in dict_for_data.items():
        dataset.append([value, len(key)])

    k_means_clustering(dataset, 3)


if __name__ == '__main__':
    calculate_k_means()
