import pandas as pd


def input_from_console():
    '''
    Function to get text from console.
    '''
    text = input('Enter text: ')
    return text


def input_from_file(file_path):
    '''
    Function to read from a file.

    Parameters:
        file_path: name of file

    '''
    try:
        with open(file_path, 'r') as file:
            res = file.read()
            return res
    except FileNotFoundError:
        raise FileNotFoundError


def input_from_file_pd(file_path):
    '''
    Function for reading from a file using the pandas.

    Parameters:
        file_path: name of file

    '''
    try:
        res = pd.read_csv(file_path)
        return res
    except FileNotFoundError:
        raise FileNotFoundError
