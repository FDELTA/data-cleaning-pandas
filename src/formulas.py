import re
california = ["(.*)?california(.*)?"]
def areas (x) :
    California = "CALIFORNIA"
    x = x.lower()
    if type(x) != str:
        return 'Unknown'
    else:
        for a in california:
            if re.search (a,x):
                x = California
                return x
        return 'Unknown'