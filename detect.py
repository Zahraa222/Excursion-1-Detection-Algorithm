import csv

def round_sensor_value(value):
    if(0 <= value < 0.35):
        return 0
    elif(0.35 <= value < 0.65):
        return 0.5
    else:
        return 1


def sign_detect(sensor_data, csv_file):
    # Round the sensor values based on the defined threshold
    rounded_values = [round_sensor_value(value) for value in sensor_data]

    fingers = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']

    # iterate through the rows of the csv file to find the matching combination sign
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for finger in fingers:
                row_values = [float(row[finger])]
            # Check if the rounded sensor values match the row values
            if rounded_values == row_values:
                print(f"Match found for {row['Letter']}")
                return row['Letter']
    return 'No match found'

# Example usage

data = list(map(float, input("Enter the sensor data separated by spaces: ").split()))
csv_file = 'sample_Data - Alphabet.csv'
result = sign_detect(data, csv_file)
print(f"Detected sign: {result}")
