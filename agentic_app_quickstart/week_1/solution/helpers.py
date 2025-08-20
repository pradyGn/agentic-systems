import os
import pandas as pd
import re

def read_employee_data():
    """A tool function that returns employee data as a pandas DataFrame object.

    Returns:
        pd.DataFrame: Employee data with columns: [name, department, salary, hire_date, performance_score].
    """

    return pd.read_csv("/workspaces/agentic-app-quickstart/agentic_app_quickstart/week_1/solution/data/employee_data.csv")

def read_sample_sale_data():
    """A tool function that returns sample sale data as a pandas DataFrame object.

    Returns:
        pd.DataFrame: sample sale data with columns: [date, product, price, quantity, customer_state].
    """

    return pd.read_csv("/workspaces/agentic-app-quickstart/agentic_app_quickstart/week_1/solution/data/sample_sales.csv")

def read_weather_data():
    """A tool function that returns weather data as a pandas DataFrame object.

    Returns:
        pd.DataFrame: weather data with columns: [date, temperature, humidity, precipitation, city].
    """

    return pd.read_csv("/workspaces/agentic-app-quickstart/agentic_app_quickstart/week_1/solution/data/weather_data.csv")

def write_to_file(content: str):
    """
    Creates a new file with the provided content 
    or appends the provided content to an existing one.
    The name of the new file is: generated_tools.py

    Args:
        content (str): The text content to write into the file.
    """
    with open("/workspaces/agentic-app-quickstart/agentic_app_quickstart/week_1/solution/generated_tools.py", 'a') as f:
        f.seek(0, os.SEEK_END)
        if f.tell() > 0:
            f.write("\n")
        f.write(content)

import ast
from typing import List, Optional

def get_function_names(file_path: str) -> Optional[List[str]]:
    """
    Reads a Python script and returns a list of all top-level function names.

    This function parses the Python file using the Abstract Syntax Tree (ast)
    module to safely and accurately find function definitions.

    Args:
        file_path: The absolute or relative path to the Python script.

    Returns:
        A list of strings, where each string is a function name.
        Returns None if no functions are found or if the file cannot be read
        or parsed.
    """
    function_names = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Parse the source code into an AST
            tree = ast.parse(file.read(), filename=file_path)
        
        # Walk through all nodes in the AST
        for node in ast.walk(tree):
            # Check if a node is a function definition
            if isinstance(node, ast.FunctionDef):
                function_names.append(node.name)
                
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except SyntaxError:
        print(f"Error: The file '{file_path}' contains a syntax error and could not be parsed.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    # Return the list of names, or None if the list is empty
    return function_names if function_names else None


def add_decorator(code_string):
    """
    Finds all Python function definitions in a string and adds
    '@function_tool' on the line directly above each one.
    """
    # Regex to find a line containing a Python function definition
    # It looks for the 'def' keyword at the start of a potential function line.
    function_regex = re.compile(r"^\s*def\s+")
    
    lines = code_string.split('\n')
    new_lines = []
    
    for line in lines:
        # Check if the current line matches the function definition pattern
        if function_regex.match(line):
            new_lines.append("@function_tool")
        new_lines.append(line)
        
    return '\n'.join(new_lines)