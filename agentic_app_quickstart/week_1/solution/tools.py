import os
import pandas as pd
from agents import function_tool

from helpers import add_decorator

@function_tool
def read_employee_data():
    """A tool function that returns employee data as a pandas DataFrame object.

    Returns:
        pd.DataFrame: Employee data with columns: [name, department, salary, hire_date, performance_score].
    """

    return pd.read_csv("./data/employee_data.csv")

@function_tool
def read_sample_sale_data():
    """A tool function that returns sample sale data as a pandas DataFrame object.

    Returns:
        pd.DataFrame: sample sale data with columns: [date, product, price, quantity, customer_state].
    """

    return pd.read_csv("./data/sample_sales.csv")

@function_tool
def read_weather_data():
    """A tool function that returns weather data as a pandas DataFrame object.

    Returns:
        pd.DataFrame: weather data with columns: [date, temperature, humidity, precipitation, city].
    """

    return pd.read_csv("./data/weather_data.csv")

@function_tool
def write_to_file(content: str):
    """
    Creates a new file with the provided content 
    or appends the provided content to an existing one.
    The name of the new file is: generated_tools.py

    Args:
        content (str): The text content to write into the file.
    """
    content = add_decorator(content)
    content = f"""from helpers import read_employee_data, read_sample_sale_data, read_weather_data
from agents import function_tool

{content}"""
    with open("./generated_tools.py", 'w') as f:
        f.write(content)