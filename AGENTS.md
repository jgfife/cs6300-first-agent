# Agent Development Guide

## Build/Test/Run Commands
- **Install dependencies**: `make install` (creates virtual environment and installs requirements)
- **Run main demo**: `make code-agent-gemini-demo` 
- **Manual run**: `. .virtual_environment/bin/activate; src/code_agent_gemini_demo.py`
- **No formal test suite configured** - add tests in a `tests/` directory if needed

## Code Style Guidelines
- **Python version**: 3.12+ (see Makefile install-deb target)
- **Imports**: Standard library first, then third-party, then local (see existing code)
- **Classes**: Use type annotations for class attributes (e.g., `name: str = "calculator"`)
- **Functions**: Include docstrings with Args/Returns sections for public methods
- **Naming**: snake_case for variables/functions, PascalCase for classes
- **Environment**: Use `dotenv` for API keys, store in `.env` file
- **Error handling**: Use standard Python exceptions, no specific patterns observed

## Project Structure
- Main code in `src/` directory
- Use virtual environment `.virtual_environment/`
- API keys: Store Gemini API key as `GEMINI_API_KEY` in `.env` file
- Dependencies managed via `requirements.txt`

## Framework-Specific Notes  
- Uses `smolagents` framework with `OpenAIServerModel` for Gemini API compatibility
- Custom tools inherit from `smolagents.Tool` base class
- Agent initialization requires `tools`, `model`, and optional `additional_authorized_imports`