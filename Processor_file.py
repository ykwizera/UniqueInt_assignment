import os
import time
import tracemalloc

class CustomNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class CustomLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = CustomNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = CustomNode(value)

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

class UniqueInt:
    def processFile(inputFilePath, outputFilePath):
        unique_integers = CustomLinkedList()
        unique_set = CustomSet()

        tracemalloc.start()
        start_time = time.time()

        with open(inputFilePath, 'r') as inputFile:
            for line in inputFile:
                line = line.strip()
                if UniqueInt.isValidInteger(line):
                    number = int(line)
                    if not unique_set.contains(number):
                        unique_set.add(number)
                        unique_integers.append(number)

        sorted_unique_integers = UniqueInt.custom_sort(unique_integers.to_list())

        with open(outputFilePath, 'w') as outputFile:
            for number in sorted_unique_integers:
                outputFile.write(f"{number}\n")

        current, peak = tracemalloc.get_traced_memory()
        end_time = time.time()
        tracemalloc.stop()

        print(f"Processing {inputFilePath} completed.")
        print(f"Time taken: {end_time - start_time} seconds")
        print(f"Memory used: {peak - current} bytes")

    def isValidInteger(line):
        if not line:
            return False
        try:
            int(line)
            return True
        except ValueError:
            return False

    def custom_sort(array):
        # Implementing a simple bubble sort for demonstration
        n = len(array)
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

class CustomSet:
    def __init__(self):
        self.elements = CustomLinkedList()

    def add(self, value):
        if not self.contains(value):
            self.elements.append(value)

    def contains(self, value):
        current = self.elements.head
        while current:
            if current.value == value:
                return True
            current = current.next
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
