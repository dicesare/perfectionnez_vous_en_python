from os import path
import logging as log


def launch_analysis(data_file):
    path_to_file = path.join("data", data_file)

    directory = path.dirname(__file__)
    file_name = path.basename(path_to_file)
    log.info("Opening data file {} from directory '{}'".format(file_name, directory))
    try:
        with open(path_to_file, "r") as file:
            preview = file.readline()
        log.info(f"afficher previsualisation du fichier xml : {preview}")
    except FileNotFoundError as e:
        log.critical(f"File not found : {e}")
    except:
        log.critical("destination unknow")


if __name__ == "__main__":
    launch_analysis("SyceronBrut.xml")
