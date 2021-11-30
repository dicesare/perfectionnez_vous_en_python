# coding: utf-8
import argparse
import logging as log

from analysis import xml as x_an, csv as c_an

"""
documnet argparse --> https://docs.python.org/3/library/argparse.html
"""
log.basicConfig(level=log.INFO)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension",
                        help="""Type of file to analyse. Is it a CSV or an XML ?""")
    parser.add_argument("-d", "--datafile",
                        help="""CSV file containing pieces of information about the members of parliament""")
    parser.add_argument("-i", "--info", action="store_true",
                        help="""information about the file""")
    return parser.parse_args()


def main():
    args = parse_arguments()
    try:
        datafile = args.datafile
        if datafile is None:
            raise Warning("You must indicate a datafile")
        else:
            try:
                if args.extension == "xml":
                    x_an.launch_analysis(datafile)
                elif args.extension == "csv":
                    c_an.launch_analysis(datafile, args.info)
            except FileNotFoundError as e:
                log.error(f"the File is not found : {e}")
            finally:
                log.info("################### Analysis is over #####################")
    except Warning as e:
        log.warning(e)


if __name__ == "__main__":
    main()
