# Unique Integers - Data Structures and Algorithms Assignment

## Overview
This project is part of the Data Structures and Algorithms course for Enterprise Web Development students. The task is to process a list of integers from an input file and generate an output file with unique integers sorted in increasing order.

## Task Description
- Read integers from an input file (one per line).
- Output a file listing unique integers, sorted, with no duplicates.

## File Structure
Organize your files as follows:

## Input Requirements
- Each line can contain a single integer, positive or negative.
- Skip empty lines, lines with non-integer values, and lines with multiple integers.

## Output Requirements
- The output file should contain unique integers sorted in ascending order.
- Each integer should appear on a new line.

## Implementation
My code should include:
- `UniqueInt::processFile(std::string inputFilePath, std::string outputFilePath)`
- `UniqueInt::readNextItemFromFile(FILE* inputFileStream)`

