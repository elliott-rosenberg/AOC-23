import os

# Function to create the code files
def create_code_files():
    code_folder = 'code'
    if not os.path.exists(code_folder):
        os.makedirs(code_folder)

    for i in range(1, 26):
        file_name = f"{code_folder}/{str(i).zfill(2)}.py"
        with open(file_name, 'w') as f:
            f.write(f"""def solvePart1(file):
    return None

def solvePart2(file):
    return None

def process(file):
    rows = [l.strip() for l in open(file).readlines()]
    return rows

def solve(file):
    processed = process(file)
    print(f"Part 1: {{solvePart1(processed)}}")
    print(f"Part 2: {{solvePart2(processed)}}")

solve("inputs/{str(i).zfill(2)}/input1.txt")
""")

# Function to create the input folders and files
def create_input_folders_and_files():
    inputs_folder = 'inputs'
    if not os.path.exists(inputs_folder):
        os.makedirs(inputs_folder)

    for i in range(1, 26):
        day_folder = f"{inputs_folder}/{str(i).zfill(2)}"
        if not os.path.exists(day_folder):
            os.makedirs(day_folder)

        input_file_path = f"{day_folder}/input1.txt"
        open(input_file_path, 'a').close()  # Create an empty file

# Create code files and input folders
create_code_files()
create_input_folders_and_files()