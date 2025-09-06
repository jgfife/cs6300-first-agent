#!/usr/bin/env python3

import pytest
import os
import sys
from pathlib import Path

# Add the src directory to the Python path so we can import the agent
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from investment_research_agent import jefe


class TestInvestmentResearchAgent:
    """Test suite for the investment research agent."""
    
    def test_apple_ceo_question(self):
        """Test that the agent correctly identifies Tim Cook as Apple's CEO"""
        question = "Who is the CEO of Apple?"
        
        # Run the agent
        answer = jefe.run(question)
        
        # Convert answer to string if it's not already
        answer_str = str(answer).lower()
        
        # Verify Tim Cook is mentioned in the response
        assert "tim cook" in answer_str, f"Expected 'Tim Cook' in response but got: {answer}"
        
        # Verify CEO or Chief Executive is mentioned
        ceo_mentioned = ("ceo" in answer_str or 
                        "chief executive" in answer_str or 
                        "chief executive officer" in answer_str)
        assert ceo_mentioned, f"Expected CEO/Chief Executive reference but got: {answer}"
        
    def test_agent_responds_to_investment_questions(self):
        """Test that the agent can handle general investment questions"""
        question = "What is Apple's stock ticker symbol?"
        
        # Run the agent
        answer = jefe.run(question)
        
        # Convert answer to string if it's not already
        answer_str = str(answer).lower()
        
        # Should mention AAPL
        assert "aapl" in answer_str, f"Expected 'AAPL' in response but got: {answer}"
        
    def test_non_investment_question_rejection(self):
        """Test that the agent rejects non-investment questions"""
        question = "What is the weather today?"
        
        # Run the agent
        answer = jefe.run(question)
        
        # Convert answer to string if it's not already
        answer_str = str(answer).lower()
        
        # Should reject non-investment questions
        rejection_phrases = [
            "i can only answer investment-related questions",
            "investment-related",
            "not investment-related"
        ]
        
        rejected = any(phrase in answer_str for phrase in rejection_phrases)
        assert rejected, f"Expected rejection of non-investment question but got: {answer}"


if __name__ == "__main__":
    # Check for API key before running tests
    if not os.getenv("GEMINI_API_KEY"):
        print("Warning: GEMINI_API_KEY not found in environment variables")
        print("Make sure to set it in your .env file or environment")
    
    pytest.main([__file__, "-v"])