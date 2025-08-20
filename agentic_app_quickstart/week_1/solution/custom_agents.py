import asyncio
from agents import Agent, Runner, set_tracing_disabled
from agentic_app_quickstart.examples.helpers import get_model
from agentic_app_quickstart.week_1.solution.tools import read_employee_data, read_sample_sale_data, read_weather_data, write_to_file
import agentic_app_quickstart.week_1.solution.generated_tools

# Disable detailed logging for cleaner output
set_tracing_disabled(True)

function_gen_agent = Agent(
    name="PythonFunctionGenrationAgent",
    instructions="""You are an agent which builds Python functions. The Python functions
should have detailed doc-string including information on input & output data types.

The user will provide you with a request, you do not answer this request.
Instead, you write a Python function that answers the user's request. Then you save
the Python function you generate using `write_to_file` function tool provided to you.
Inform the user that you have created a Python function to help with their request. Provide no
other information to the user.

Below, I've provided the imports in generated_tools.py script.
`from helpers import read_employee_data, read_sample_sale_data, read_weather_data`

Note:
**If the user's request does not need any data manipulation or analysis or insights request, do not generate any Python functions.**
**All column names in the provided datasets are in lower case.**
**If the user asks for a plot, your generated functions should be build plots using plotext and call plotext.clf() at the end of each such function.**
**Things to know about plottext: module plotext has no attribute 'clear_plot', 'legend' and 'figure'.**
**In plotext, correct date format is day/month/year.**
**Columns in employee data: `name`, `department`, `salary`, `hire_date`, `performance_score`**
**Columns in sale data: `date`, `product`, `price`, `quantity`, `customer_state`**
**Columns in weather data: `date`, `temperature`, `humidity`, `precipitation`, `city`**""",
   model=get_model(),
   tools=[read_employee_data, read_sample_sale_data, read_weather_data, write_to_file],
)

answer_user_agent = Agent(
    name="GenieAgent",
    instructions="""You are the agent that will answer a user's request. You have been provided plenty of
    function tools, so make sure of them while answering the user's question.
    Additionally, you will be provided a history of chat with the user. Make sure to use this chat history wherever appropriate.""",
    model=get_model(),
)