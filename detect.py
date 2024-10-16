import csv

# Function to round sensor values based on thresholds
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

    fingers = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky', 'Wrist rotation-X (Up and down)', 'Wrist rotation-Y (Left)', 'Wrist rotation-Z (Elbow Twist)']

    # Iterate through the rows of the CSV file to find the matching combination sign
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Collect all finger values from the current row and convert them to float
            row_values = [float(row[finger]) for finger in fingers]

            # Check if the rounded sensor values match the row values
            if rounded_values == row_values:
                print(f"Match found for {row['Letter']}")
                return row['Letter']
    return

# Example usage

while(1):
    data = list(map(float, input("Enter the sensor data separated by spaces: ").split()))
    csv_file = 'ASL_Gestures.csv'
    result = sign_detect(data, csv_file)
    print(f"Detected sign: {result}")
