import os
import json
import pandas as pd


def load_txt(filepath):
    """

    :param filepath: str
    :return: str
    """
    with open(filepath, 'r') as file:
        data = file.read()
    return data


def save_txt(filepath, data):
    """

    :param filepath: string
    :param data: string
    :return: bool
    """
    with open(filepath, 'w') as file:
        file.write(data)
    return True


def load_json(filepath):
    """

    :param filepath: string
    :return: dict
    """
    with open(filepath) as file:
        data = json.load(file)
    return data


def save_json(filepath, data):
    """

    :param filepath: string
    :param data: dict
    :return: bool
    """
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    return True


def load_csv_df(filepath):
    """
    Loads csv in to pandas DataFrame
    :param filepath: string
    :return: pandas.DataFrame
    """
    data = pd.read_csv(filepath)
    return data


def save_csv(filepath, data):
    """
    Note: This save without headers or index. Remove if necessary

    :param filepath: string
    :param data: pandas.DataFrame
    :return: bool
    """
    data.to_csv(filepath, header=False, index=False)