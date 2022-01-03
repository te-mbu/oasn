import pandas
import ast
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt


def str_to_dict(string):
    return ast.literal_eval(string)


df = pandas.read_csv(
    "EP_Data_Extended.csv", quotechar='"', skipinitialspace=True, low_memory=False
)

trackers = pandas.read_csv(
    "data_trackers.csv", quotechar='"', skipinitialspace=True, low_memory=False
)

info_trackers = pandas.read_csv(
    "data_trackers.csv", quotechar='"', skipinitialspace=True, low_memory=False
)

handles = df.loc[:, "handle"]
trackers = df.loc[:, "trackers"]

# Get all handles in a list
handles = handles.values.tolist()

# Get all trackers in a list
trackers_permissions = trackers.values.tolist()


dict_trackers = {}
dict_permissions = {}

# Count nb of each tracker and each permission
for el in trackers_permissions:
    if type(el) == str:
        el = el.split(",")
        for nb in el:
            if nb and nb.isdigit() and nb in dict_trackers:
                dict_trackers[nb] += 1
            elif nb and nb.isdigit():
                dict_trackers[nb] = 1
            elif "permission" in nb and nb in dict_permissions:
                dict_permissions[nb] += 1
            else:
                dict_permissions[nb] = 1

# most_permissions = sorted(dict_permissions.items(), reverse=True, key=lambda t: t[1])
ordered_trackers = sorted(dict_trackers.items(), key=lambda x: x[1], reverse=True)


# change dictionary key - tracker id to tracker name

result = {}

for track in ordered_trackers[:20]:
    if track[0] != "000":
        key = str_to_dict(info_trackers[track[0]][0])

        # merge all google trackers
        if "Google" in key["name"] or "com.google" in key["network_signature"]:
            if "Google" in result.keys():
                result["Google"] += track[1]
            else:
                result["Google"] = track[1]

        # merge all facebook trackers
        elif "Facebook" in key["name"] or "com.facebook" in key["network_signature"]:
            if "Facebook" in result.keys():
                result["Facebook"] += track[1]
            else:
                result["Facebook"] = track[1]
        else:
            key = key["name"]
            result[key] = track[1]


# Get histo
plt.bar(list(result.keys()), result.values())
plt.xticks(rotation="vertical")
plt.show()


# Get pie chart of different categories

cat_result = {}

for track in ordered_trackers[:50]:
    if track[0] != "000":
        key = str_to_dict(info_trackers[track[0]][0])
        for categories in key["categories"]:

            if categories and categories in cat_result.keys():
                cat_result[categories] += 1
            else:
                cat_result[categories] = 1

keys = cat_result.keys()
values = cat_result.values()

fig, ax = plt.subplots()
ax.pie(values, labels=keys, autopct="%1.1f%%")
ax.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.


plt.show()