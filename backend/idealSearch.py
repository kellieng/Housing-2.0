# Implement Algorithm Here:
import json
# -ideal_search: Finds a room with a size that matches the group size and takes preferences into account

def idealSearch(data, groupSize, preferred):
    # check to see if groupSize matches the room size available
    # preferred is a list of their preferred dorms in order from first to last, can be up to 3 <= x <= 5 dorms
    # returns a string of the best dorm available for them
    # data is read from a json file

    if (len(preferred) < 3) or (len(preferred) > 5):
        return "ERROR: invalid amount of preferences"
    
    return "null"

f = open("campus.json")
data = json.load(f)
groupSize = 4
preferred1 = ["Nason", "Sharp", "Davison"]
preferred2 = ["Sharp", "Hall"]

print(idealSearch(data, groupSize, preferred1))