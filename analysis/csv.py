import pprint
from os import path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pda

"""
open() -->  https://docs.python.org/3/library/functions.html#open
"""


class SetOfParliamentMembers:
    def __init__(self, name):
        self.dataframe = None
        self.name = name

    def __repr__(self):
        return f"SetOfParliamentMember: {len(self.dataframe)} members()"

    def __iter__(self):
        self.iterator_state = 0
        return self

    def __next__(self):
        if self.iterator_state >= len(self):
            raise StopIteration()
        result = self[self.iterator_state]
        self.iterator_state += 1
        return result

    def data_from_csv(self, csv_file):
        self.dataframe = pda.read_csv(csv_file, sep=";")
        pass

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        proportions = counts / nb_mps
        labels = [f"Female ({counts[0]})", f"Male ({counts[1]})"]

        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
            proportions,
            labels=labels,
            autopct="%1.1f pourcents"
        )
        plt.title(f"{self.name} ({nb_mps})")
        plt.show()

    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        all_parties = data["parti_ratt_financier"].dropna().unique()

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers(f"MPs from party '{party}'")
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result


def launch_analysis(data_file,
                    by_party=False,
                    info=False,
                    display_names=False,
                    search_name=None,
                    index=None,
                    group_fist=None,
                    by_age=None):
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(path.join("data", data_file))
    sopm.display_chart()
    # print(f"info : {info}")
    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()

    if info:
        print()
        print(repr(sopm))

    if display_names:
        print()
        print(sopm)

    if search_name is not None:
        is_present = search_name in sopm
        print()
        print("Testing if {} is present: {}".format(search_name, is_present))

    if index is not None:
        index = int(index)
        print()
        pprint.pprint(sopm[index])  # prints the dict a nice way

    if group_fist is not None:
        groupfirst = int(group_fist)
        parties = sopm.split_by_political_party()
        parties = parties.values()
        parties_by_size = sorted(parties, reverse=True)

        print()
        print("Info: the {} biggest groups are :".format(groupfirst))
        for p in parties_by_size[0:groupfirst]:
            print(p.name)

        s = sum(parties_by_size[0:groupfirst])

        s.display_chart()

    if by_age is not None:
        by_age = int(by_age)  # by_age was still a string, passed by the command line
        for age_group, s in sopm.split_by_age(by_age).items():
            print()
            print("-" * 50)
            print(age_group + ":")
            s.display_chart()
            print()
            print("{} : Distribution by party:".format(age_group))
            print()
            pprint.pprint(s.number_mp_by_party())


"""
    path_to_file = path.join("data", data_file)

    directory = path.dirname(__file__)
    file_name = path.basename(path_to_file)
    log.info("Opening data file {} from directory '{}'".format(file_name, directory))
    try:
        with open(path_to_file, "r") as file:
            preview = file.readline()
        log.info(f"afficher previsualisation du fichier csv : {preview}")
    except FileNotFoundError as e:
        log.critical(f"File not found : {e}")
    except:
        log.critical("destination unknow")
"""

if __name__ == "__main__":
    launch_analysis('current_mps.csv')
