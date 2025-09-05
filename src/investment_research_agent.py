#!/usr/bin/env python3

import re
import requests
import dotenv
import os
from contextlib import redirect_stdout
from datetime import datetime
from markdownify import markdownify
from requests.exceptions import RequestException
from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    OpenAIServerModel,
    DuckDuckGoSearchTool,
    tool
)

@tool
def visit_webpage(url: str) -> str:
    """Visits a webpage at the given URL and returns its content as a markdown string.

    Args:
        url: The URL of the webpage to visit.

    Returns:
        The content of the webpage converted to Markdown, or an error message if the request fails.
    """
    try:
        # Send a GET request to the URL with proper headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Convert the HTML content to Markdown
        markdown_content = markdownify(response.text).strip()

        # Remove multiple line breaks
        markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

        return markdown_content

    except RequestException as e:
        return f"Error fetching the webpage: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

dotenv.load_dotenv()
model_id="gemini-2.5-flash"
model = OpenAIServerModel(model_id=model_id,
                          api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
                          api_key=os.getenv("GEMINI_API_KEY"),
                          )

seeker = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), visit_webpage],
    model=model,
    max_steps=3,
    name="search_agent",
    description="Runs web searches for investment information for you.",
    instructions="You are a helpful research assistant that can search the web and visit webpages to gather information about investment-related topics. You respond with a concise summary of the information you pages you visit.",
)

jefe = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[seeker],
    additional_authorized_imports=["time", "numpy", "pandas"],
    instructions="You are a helpful research assistant that can only answer investment-related questions and visit webpages that pertain to the queried company to gather information. If the question is not investment-related, respond with 'I can only answer investment-related questions.'",
)

while True:
    try:
        question = input("How can I help you? ")
        if question.lower() in ['exit', 'quit', 'q']:
            print("Goodbye!")
            break

        answer = ""
        # Write answer to text file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"logs/investment_research_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            # Redirect stdout within this context
            with redirect_stdout(f): 
                answer = jefe.run(question)
        
        print(f"\nAnswer:\n{answer}\n")
        print(f"Full interaction logged to {filename}\n")

    except KeyboardInterrupt:
        print("\nGoodbye!")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        continue