import csv
import numpy as np
from scipy.spatial import distance


def read_world_cities(csv_file):
    all_cities = []
    all_lat_lon = []
    with open (csv_file,'r') as f:
        reader = csv.reader(f)
        for city in reader:
            all_cities.append({"city":city[1], "state": city[8], "country":city[5], "latitude":city[2], "longitude":city[3]})
            all_lat_lon.append([city[2], city[3]])
    all_lat_lon = np.array(all_lat_lon)
    return all_cities, all_lat_lon


def georeverse(point):
    all_cities, all_lat_lon = read_world_cities('world_cities.csv')
    result = all_lat_lon[distance.cdist([point], all_lat_lon).argmin()]
    for city in all_cities:
        if result[0] == city['latitude'] and result[1] == city['longitude']:
            return city
    return None