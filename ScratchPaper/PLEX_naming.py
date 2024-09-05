
ep_names = []

def plex_naming():
    title = input("What is the title of your show?: ")
    episodes = int(input("How many episodes in the season?: "))
    season = "0" + input("Which season is it?: ")
    
    for x in range(1,episodes+1):
        if int(x) < 10:
            ep_num = "0" + str(x)
        else:
            ep_num = x
        filename = title + "-s" + season + "e" + str(ep_num)
    
        print(filename)
        # ep_names.append(filename)
    return ep_names

plex_naming()
print(ep_names)
