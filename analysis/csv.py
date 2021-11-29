from os import path

"""
open() -->  https://docs.python.org/3/library/functions.html#open
"""


def main():
    pass


def launch_analysis(data_file):
    directory = path.dirname(__file__)
    path_to_file = path.join(directory, "../data", data_file)

    with open(path_to_file, "r") as file:
        preview = file.readline()

    print(f"afficher previsualisation du fichier csv : {preview}")


if __name__ == '__main__':
    launch_analysis('current_mps.csv')
