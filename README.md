# Investment Research Agent

An AI-powered investment research assistant built with Hugging Face smolagents and Google Gemini.

## Features

- **Investment-focused Q&A**: Answers questions about companies, stocks, and financial topics
- **Web search capabilities**: Uses DuckDuckGo search and webpage content extraction
- **CEO identification**: Accurately identifies company leadership (tested with Apple/Tim Cook)
- **Interactive CLI**: Chat-based interface with conversation logging
- **Comprehensive testing**: Full test suite with pytest framework

## Quick Start

### 1. Setup Environment
```bash
# Install dependencies
pip install -r requirements.txt

# Set up your Gemini API key
export GEMINI_API_KEY="your_api_key_here"
# Or create a .env file with: GEMINI_API_KEY=your_api_key_here
```

### 2. Run the Agent
```bash
# Interactive mode
python src/investment_research_agent.py

# Example questions to try:
# - "Who is the CEO of Apple?"
# - "What is Tesla's stock ticker symbol?"
# - "Tell me about Microsoft's recent earnings"
```

### 3. Run Tests
```bash
# Run all tests
pytest tests/ -v

# Run just the CEO test
pytest tests/test_investment_research_agent.py::TestInvestmentResearchAgent::test_apple_ceo_question -v
```

## API Setup

### Gemini API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Click "Get API key" 
3. Create a new API key
4. Set it as `GEMINI_API_KEY` environment variable

### Supported Models
- Primary: `gemini-2.5-flash` (configured in code)
- API Base: `https://generativelanguage.googleapis.com/v1beta/openai/`
- Compatibility: Uses OpenAI-compatible API format

## Project Structure

```
cs6300-first-agent/
├── src/
│   └── investment_research_agent.py    # Main agent implementation
├── tests/
│   ├── test_investment_research_agent.py # Test suite
│   └── README.md                        # Testing documentation
├── logs/                                # Conversation logs (auto-created)
├── requirements.txt                     # Dependencies
├── pytest.ini                         # Test configuration
```

## Architecture

- **jefe (CodeAgent)**: Main orchestrator that manages sub-agents and handles user queries
- **seeker (ToolCallingAgent)**: Specialized search agent with web search and page visit capabilities
- **visit_webpage**: Custom tool for fetching and converting web content to markdown
- **DuckDuckGoSearchTool**: Built-in search functionality

## Testing

The test suite verifies:
- ✅ Correct CEO identification (Tim Cook for Apple)
- ✅ Stock ticker symbol retrieval (AAPL for Apple) 
- ✅ Investment question handling
- ✅ Non-investment question rejection

See `tests/README.md` for detailed testing documentation.

## Development

Built with:
- **smolagents**: Hugging Face agent framework
- **Google Gemini**: LLM backend via OpenAI-compatible API
- **DuckDuckGo**: Web search capabilities
- **pytest**: Testing framework
- **requests + markdownify**: Web content processing
