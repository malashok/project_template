import pandas as pd


def output_to_console(text):
    '''
    Function to print text in console.

    Parameters:
        text: text to print
    '''
    print(text)


def output_to_file(file_path, text):
    '''
    Function to print text in file.

    Parameters:
        file_path: path to file
        text: text to output
    '''
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print(file_path)
    except FileNotFoundError:
        raise FileNotFoundError


def output_to_file_pd(file_path, text):
    '''
    Function to write DataFrame to a CSV file.

    Parameters:
        file_path: path to file
        text: dataframe to output
    '''
    try:
        df = pd.DataFrame(text)
        df.to_csv(file_path, index=False)
        print(file_path)
    except FileNotFoundError:
        raise FileNotFoundError
