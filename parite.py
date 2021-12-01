# coding: utf-8
import argparse
import logging as log
import re
import sys

from analysis import xml as x_an, csv as c_an

"""
documnet argparse --> https://docs.python.org/3/library/argparse.html
"""

log.basicConfig(level=log.INFO)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datafile", help="""CSV file containing pieces of
        information about the members of parliament""")
    parser.add_argument("-p", "--byparty", action='store_true', help="""displays
        a graph for each political party""")
    parser.add_argument("-i", "--info", action='store_true', help="""information about
        the file""")
    parser.add_argument("-n", "--displaynames", action='store_true', help="""displays
        the names of all the mps""")
    parser.add_argument("-s", "--searchname", help="""search for a mp name""")
    parser.add_argument("-I", "--index", help="""displays information about the Ith mp""")
    parser.add_argument("-a", "--byage", help="""displays a graph for the MPs splitted
    #        between those who are over and those who are under the value of --byage""")
    parser.add_argument("-g", "--groupfirst", help="""displays a graph groupping all the 'g'
        biggest political parties""")
    return parser.parse_args()


def main():
    args = parse_arguments()
    print(args)
    try:
        datafile = args.datafile
        if datafile is None:
            raise Warning("You must indicate a datafile")
    except Warning as e:
        log.warning(e)
    else:
        print(args.datafile)
        ext = re.search("^.+\.(\D{3})$", args.datafile)
        print(ext)
        extension = ext.group(1)
        if extension == "xml":
            x_an.launch_analysis(datafile)
        elif extension == "csv":
            c_an.launch_analysis(args.datafile,
                                 args.byparty,
                                 args.info,
                                 args.displaynames,
                                 args.searchname,
                                 args.index,
                                 args.groupfirst,
                                 args.byage)

    finally:
        log.info("################### Analysis is over #####################")


if __name__ == "__main__":
    main()
