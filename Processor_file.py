import os

class UniqueInt:
    def processFile(inputFilePath, outputFilePath):
        unique_integers = set()
        
        with open(inputFilePath, 'r') as inputFile:
            for line in inputFile:
                line = line.strip()
                if UniqueInt.isValidInteger(line):
                    unique_integers.add(int(line))
        
        sorted_unique_integers = sorted(unique_integers)
        
        with open(outputFilePath, 'w') as outputFile:
            for number in sorted_unique_integers:
                outputFile.write(f"{number}\n")

    def isValidInteger(line):
        if not line:
            return False
        try:
            int(line)
            return True
        except ValueError:
            return False

input_directory = 'sample_input_for_students/'
output_directory = 'sample_results/'

if not os.path.exists(input_directory):
    print(f"Error: The input directory '{input_directory}' does not exist.")
else:
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            inputFilePath = os.path.join(input_directory, filename)
            outputFilePath = os.path.join(output_directory, f"{filename}_results.txt")
            UniqueInt.processFile(inputFilePath, outputFilePath)
    print("Processing completed successfully.")
    
