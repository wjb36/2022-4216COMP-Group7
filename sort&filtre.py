import csv
from typing import List
from datetime import datetime


class Earthquake:
    def __init__(self, date, latitude, longitude, depth, magnitude, time, magnitude_seismic_stations,
                 azimuthal_gap, horizontal_distance, root_mean_square, location_source, is_true):
        """
        Earthquake class to store earthquake data.

        :param date: str, date of the earthquake
        :param latitude: str, latitude of the earthquake's epicenter
        :param longitude: str, longitude of the earthquake's epicenter
        :param depth: str, depth of the earthquake
        :param magnitude: str, magnitude of the earthquake
        :param time: str, time of the earthquake
        :param magnitude_seismic_stations: str, number of seismic stations that reported the magnitude
        :param azimuthal_gap: str, azimuthal gap for the earthquake
        :param horizontal_distance: str, horizontal distance for the earthquake
        :param root_mean_square: str, root mean square value for the earthquake
        :param location_source: str, source of the location data
        :param is_true: str, whether the earthquake is verified or not
        """
        self.date = datetime.strptime(date, '%d-%b-%y') if date else None
        self.latitude = float(latitude) if latitude else None
        self.longitude = float(longitude) if longitude else None
        self.depth = float(depth) if depth else None
        self.magnitude = float(magnitude) if magnitude else None
        self.time = datetime.strptime(time, '%H:%M:%S').time() if time else None
        self.magnitude_seismic_stations = magnitude_seismic_stations if magnitude_seismic_stations else None
        self.azimuthal_gap = azimuthal_gap if azimuthal_gap else None
        self.horizontal_distance = horizontal_distance if horizontal_distance else None
        self.root_mean_square = root_mean_square if root_mean_square else None
        self.location_source = location_source if location_source else None
        self.is_true = is_true.lower() == 'true' if is_true else None


def read_earthquake_data_from_csv(file_path: str) -> List[Earthquake]:
    """
    Read earthquake data from a CSV file and return a list of Earthquake objects.

    :param file_path: str, path to the CSV file containing earthquake data
    :return: List[Earthquake], list of Earthquake objects
    """
    earthquakes = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            earthquakes.append(Earthquake(*row))
    return earthquakes

def sort_and_filter_earthquakes(earthquakes: List[Earthquake], attribute: str, top_n: int, reverse: bool = False) -> List[Earthquake]:
    """
    Sort and filter a list of Earthquake objects based on the given attribute and the number of results required.

    :param earthquakes: List[Earthquake], list of Earthquake objects
    :param attribute: str, attribute to sort the Earthquake objects by
    :param top_n: int, number of top results to return
    :param reverse: bool, whether to sort the results in descending order (default is False)
    :return: List[Earthquake], list of sorted and filtered Earthquake objects
    """
    sorted_earthquakes = sorted(earthquakes, key=lambda x: getattr(x, attribute), reverse=reverse)
    return sorted_earthquakes[:top_n]


if __name__ == '__main__':

    # Read earthquake data from CSV file
    csv_file_path = "earthquakeDatasetG7.csv"
    earthquakes = read_earthquake_data_from_csv(csv_file_path)

    # Find the top 10 earthquakes with the highest magnitude
    highest_magnitude_earthquakes = sort_and_filter_earthquakes(earthquakes, "magnitude", 10, reverse=True)
    print("Top 10 Earthquakes With The Highest Magnitude:")
    for earthquake in highest_magnitude_earthquakes:
        print(f"Date: {earthquake.date}, Magnitude: {earthquake.magnitude}")

    # Find the top 10 earthquakes with the lowest magnitude
    lowest_magnitude_earthquakes = sort_and_filter_earthquakes(earthquakes, "magnitude", 10, reverse=False)
    print("\nTop 10 Earthquakes With The Lowest Magnitude:")
    for earthquake in lowest_magnitude_earthquakes:
        print(f"Date: {earthquake.date}, Magnitude: {earthquake.magnitude}")
