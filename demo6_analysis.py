# Data Lifecycle: Storage.
# Reading from a CSV file.
# and writing the validated data out using pickle
import pickle
import csv
from typing import List
from warnings import WarningMessage

from weatherreading import WeatherReading


def valid_temperature(temperature: float):
    return -40 < temperature < 85


def valid_pressure(pressure: float):
    return 300 < pressure < 1200


def valid_humidity(humidity: float):
    return 20 < humidity < 80


def valid_reading(temperature: float, pressure: float, humidity: float):
    return valid_temperature(temperature) and valid_pressure(pressure) and valid_humidity(humidity)


def get_readings_from_file(filename: str, skip_first_line: bool) -> List[WeatherReading]:
    with open(filename, "r") as file:
        # Note that we're stating that the list is a List of WeatherReading instances
        all_readings: list[WeatherReading] = []
        first_line = True

        for line in file:
            if skip_first_line and first_line:
                first_line = False
                continue

            split = line.split(",")
            temperature = float(split[0])
            pressure = float(split[1])
            humidity = float(split[2])
            if valid_reading(temperature, pressure, humidity):
                reading = WeatherReading(temperature, pressure, humidity)
                all_readings.append(reading)

        return all_readings




if __name__ == "__main__":
    filename = input("Enter CSV file name: ")
    all_readings = get_readings_from_file(filename, True)

    # Echo the input to output.
    print("Your readings:")
    for reading in all_readings:
        print(f"\tTemp: {reading.temperature}", end="")
        print(f"\tPressure: {reading.pressure}", end="")
        print(f"\tHumidity: {reading.humidity}")

    pickle_demo = open('pickle_demo.bin', 'wb')
    pickle.dump(all_readings, pickle_demo)
    pickle_demo.close()


def max_teperature():
    # get readings from main function
    data = get_readings_from_file("weather.csv", True)
    maxT = 0.0
    # for loop to keep track of the largest value
    for x in range(len(data)):
        # if current max temp is 0 or if our pointer temp is larger than max
        # then max temp is the value of our pointer
        if (maxT == 0.0 or data[x].temperature > maxT):
            maxT = data[x].temperature
    print("Maximum Temperature: ", maxT)

max_teperature()

def min_pressure():
    data = get_readings_from_file("weather.csv", True)
    minP = 1200.0  # Maximum amount of pressure that the data can not exceed
    for x in range(len(data)):
        # if pointer pressure 
        if (data[x].pressure < minP):
            minP = data[x].pressure
    print("Minimum Pressure: ", minP)

min_pressure()

def max_humidity():
    # get readings from main function
    data = get_readings_from_file("weather.csv", True)
    maxH = 0.0
    # for loop to keep track of the largest value
    for x in range(len(data)):
        # if current max humidity is 0 or if our pointer humidity is larger than max
        # then max humidity is the value of our pointer
        if (maxH == 0.0 or data[x].humidity > maxH):
            maxH = data[x].humidity
    print("Maximum Humidity: ", maxH)

max_humidity()
