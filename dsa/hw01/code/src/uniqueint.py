# Define constants for integer limits
MIN_INT = -2**31
MAX_INT = 2**31 - 1

# Initialize an empty list for unique integers
unique_integers = []

# Open the input file for reading
with open("C:/Users/Administrator/Desktop/School Projects/DSA-HW01---UniqueInt/dsa/hw01/sample_inputs/sample_input_01.txt", "r") as file:

    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace

        try:
            my_int = int(line)  # Convert line to integer
            
            # Check if the integer is within the allowed range and unique
            if MIN_INT <= my_int <= MAX_INT and my_int not in unique_integers:
                unique_integers.append(my_int)  # Add unique integer to the list
        except ValueError:
            continue  # Skip lines that cannot be converted to an integer

# Sort the unique integers manually
for i in range(len(unique_integers)):
    for j in range(i + 1, len(unique_integers)):
        if unique_integers[i] > unique_integers[j]:
            # Swap if out of order
            unique_integers[i], unique_integers[j] = unique_integers[j], unique_integers[i]

# Write the sorted unique integers to the output file
with open("C:/Users/Administrator/Desktop/School Projects/DSA-HW01---UniqueInt/dsa/hw01/sample_results/sample_result.txt", "w") as output_file:
    for integer in unique_integers:
        output_file.write(f"{integer}\n")  # Write each integer on a new line

