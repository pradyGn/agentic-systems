import asyncio
from custom_agents import function_gen_agent, answer_user_agent
from agents import Runner
import importlib

import generated_tools
import helpers
from agentic_app_quickstart.week_1.solution.tools import read_employee_data, read_sample_sale_data, read_weather_data

agents = {
    "repond": answer_user_agent,
    "function_generation": function_gen_agent,
}

async def run_conversation_with_handoffs():
    """
    Main conversation loop that handles agent handoffs.

    This function:
    1. Starts with the reception agent
    2. Processes user input
    3. Checks if agent wants to handoff to another agent
    4. Switches agents as needed
    5. Continues the conversation with the new agent
    """
    print("Our reception agent will help you get started.")
    print("Type 'quit' or 'exit' to end the conversation.\n")

    memory = []; m_size = 3

    while True:
        if len(memory) == m_size + 1:
            memory = memory[:-1]
        memory_str = "".join(memory)

        # Get user input
        user_input = input("You: ")

        # Check if user wants to exit
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Thank you for contacting us. Goodbye! 👋")
            break

        # try:
            # Run the current agent
        _ = await Runner.run(starting_agent=agents["function_generation"], input=f"{memory_str}\nUser Input: {user_input}")

        generated_tools = importlib.import_module("generated_tools")
        generated_tools = importlib.reload(generated_tools)
        func_str_lis = helpers.get_function_names("generated_tools.py")
        func_lis = [getattr(generated_tools, f) for f in func_str_lis]
        agents["repond"].tools = [read_employee_data, read_sample_sale_data, read_weather_data] + func_lis

        result = await Runner.run(starting_agent=agents["repond"], input=f"{memory_str}\nUser Input: {user_input}")
        response = result.final_output

        current_inp = f"User Input: {user_input}\n"
        current_out = f"Agent Response: {response}\n"
        current_chat = f"{current_inp}{current_out}"
        memory.append(current_chat)

        # Display the agent's response
        print(f"Agent: {response}\n")

        # except Exception as e:
        #     print(f"❌ An error occurred: {str(e)}")
        #     print("Please try again.\n")

async def main():
    """
    Main function that demonstrates the handoff system.

    Try asking questions like:
    - "I'm having trouble logging in" (should transfer to tech support)
    - "What's the price of your premium plan?" (should transfer to sales)
    - "I was charged twice this month" (should transfer to billing)
    - "Hello, I need some general help" (stays with reception)
    """
    await run_conversation_with_handoffs()


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())