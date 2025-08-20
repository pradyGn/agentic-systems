# Dynamic AI Agentic Workflow for Data Analysis & XGBModeling

This project implements a sophisticated dual-agent system with short term memory designed for interactive data analysis. One agent dynamically generates new Python functions (tools) in response to user requests, while a second agent utilizes these tools to provide answers and insights from various datasets.

***

## 💡 How It Works

The system operates on a two-agent pipeline, separating the tasks of tool creation and task execution. This creates a powerful workflow where the system can "learn" to perform new tasks on the fly.

### The Toolmaker: `PythonFunctionGenrationAgent`

This agent acts as a specialized Python code generator. When a user makes a request that requires a new data manipulation, analysis, or visualization function, this agent takes charge.

-   It **does not** answer the user's question directly.
-   Instead, it **writes a complete Python function** that can solve the request.
-   It uses the `write_to_file` tool to save this new function into the `generated_tools.py` file.
-   This process effectively expands the system's capabilities at runtime.
-   It **does not** write a Python function if the user's request can be answered from memory.

### The Answerer: `GenieAgent`

This is the primary user-facing agent. It leverages the full suite of available functions to answer a user's question.

-   It has access to both the pre-defined tools and any new tools created by the `PythonFunctionGenrationAgent`.
-   It uses the context from the chat history to provide relevant and accurate answers.

![Flowchart showing a user request going to the Toolmaker Agent, which writes a tool to a file. The Answerer Agent then uses this new tool to respond to the user.](https://i.imgur.com/your-image-url.png)

***

## 📂 Codebase Structure

The project is organized into several key files that define the agents, their tools, and supporting logic.

-   `custom_agents.py`: This is the core of the project, defining the instructions, models, and toolsets for the two main agents: `PythonFunctionGenrationAgent` and `GenieAgent`.

-   `tools.py`: This file contains the initial set of functions exposed to the agents as tools. These include functions for reading data (`read_employee_data`, `read_sample_sale_data`, etc.) and the critical `write_to_file` function that allows the Toolmaker agent to create new tools. It automatically adds the necessary `@function_tool` decorator to any generated code.

-   `helpers.py`: A collection of utility functions that support the agents and tools. This includes functions for reading CSV files and programmatically manipulating Python code strings (e.g., `add_decorator`).

-   `generated_tools.py`: This file is **dynamically created and populated** by the `PythonFunctionGenrationAgent`. It stores all the new functions written by the agent, making them available for the `GenieAgent` to use in subsequent requests.

-   `main.py`: The main entry point for the application. It contains the primary conversation loop that orchestrates the agents, handles user input, and manages the dynamic reloading of tools.

***

## ✨ Key Features

-   **Dynamic Tool Generation**: The system's primary strength is its ability to create new functions at runtime to solve novel problems without manual intervention.
-   **Data-Driven**: Comes equipped with tools to read and process data from multiple CSV files, including employee, sales, and weather data.
-   **Text-Based Plotting**: Can generate data visualizations directly in the terminal using the `plotext` library.
-   **Modular Agent Architecture**: The separation of concerns between the "Toolmaker" and "Answerer" agents creates a clean, powerful, and extensible workflow.

***

## 🚀 Prerequisites & Setup

Before running the application, you need to install the required Python libraries.

1.  It's recommended to run this project in a container. Open this repository in VS Code, click "Reopen in Container" or use the command palette (Cmd+Shift+P) and select "Dev Containers: Reopen in Container".

2.  Install all the necessary dependencies from the `requirements.txt` file:
    ```bash
    uv pip install -r /workspaces/agentic-systems/agentic_app_quickstart/week_1/solution/requirements.txt
    ```

***

### How to Run

Once you have installed the dependencies, start the application by running the main script from your terminal:

```bash

cd agentic_app_quickstart/week_1/solution/

python main.py

```

This will launch the interactive chat session. You can ask questions that require the agent to generate new functions for analysis or plotting.

Example Prompts:

-   Give me some interesting insights.

-   Give me some intersting co-relations.

-   What is the highest salary in the Engineering department?

    -   (Follow-up question suggestion) Whats this person's salary?

-   Show me the total sales quantity per product.

-   Plot the Salaries vs Department.

-   Is there a co-relation between weather and sales?

-   Which employee has the highest performance score?

    -   (Follow-up question suggestion) Whats this person's salary?

-   (My Favourite): Train a simple xgboost model on salary prediction based on department, hire date and performance score. Tell me salary of individual with the following feature -  Marketing, 2022-05-08, 3.0


You can end the conversation at any time by typing `quit` or `exit`.