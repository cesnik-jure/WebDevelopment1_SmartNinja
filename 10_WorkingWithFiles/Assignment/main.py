with open("input.csv", "r") as input_file:
    input_data = input_file.read().splitlines()

    for row in input_data:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}")
