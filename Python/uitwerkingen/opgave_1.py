blue='greenpark picadilly coventgarden holborn russellsquare kingscross'
yellow='towerhill bakerstreet holborn blackfriars temple'
red='bank holborn oxford bondstreet marblearch'
brown='bakerstreet oxford picadilly charingcross'
lines_london = [blue, yellow, red, brown]


# a
set_of_stations = set()
for line in lines_london:
    stations = line.split()
    for s in stations:
        set_of_stations.add(s)

for s in set_of_stations:
    print(s)

# b

dict_of_stations = {}
for s in set_of_stations:
    neigbors = []
    for line in lines_london:
        stations = line.split()
        # s in this line?
        if s in line:
            i = stations.index(s)
            # if station has neigbors on this line
            if i > 0:
                    neigbors.append(stations[i-1])
            if i < len(stations) - 1:
                    neigbors.append(stations[i+1])
    dict_of_stations[s] = neigbors

for k,v in dict_of_stations.items():
    print(k,v)

# c

print(max(dict_of_stations, key=lambda k:len(dict_of_stations[k])))
