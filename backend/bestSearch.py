# Implement Algorithm Here:
# -best_search: like ideal_search, but does not take preferences into account

import json

# if sorted by year first then halls
def bestSearch(groupSize, year):
    f = open('campus.json')
    data = json.load(f)
    if year == "freshmen":
        # load freshmen dorms
        for x in data["freshmen"]:
            print(x)
    elif year == "sophomore":
        # load soph dorms
        for x in data["sophomore"]:
            print(x)
    elif year == "junior":
        # load jun dorms
        for x in data["junior"]:
            print(x)
    elif year == "senior":
        # load sen dorms
        for x in data["senior"]:
            print(x)
    f.close()

# would it be more convenient if we sort by year first or dorm
