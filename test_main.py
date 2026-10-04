import os
import sys
from unittest.mock import patch, MagicMock

# Set dummy env variable before main imports client
os.environ["NEBIUS_API_KEY"] = "test-key"

import main
import pytest


def test_memory_retrieval_found():
    """Test that memory retrieval finds matching context based on query terms."""
    assistant = main.MemoriAIAssistant()
    context = assistant.retrieve_memories("Tell me about Nebius Cloud")
    assert "Nebius Cloud" in context


def test_memory_retrieval_not_found():
    """Test behavior when query terms do not match memory store."""
    assistant = main.MemoriAIAssistant()
    context = assistant.retrieve_memories("What is the weather in Tokyo?")
    assert context == "No prior context found."


@patch("main.client.chat.completions.create")
def test_chat_method(mock_create):
    """Test that chat constructs system prompt with memory and triggers OpenAI API."""
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="MemoriAI response."))
    ]
    mock_create.return_value = mock_response

    assistant = main.MemoriAIAssistant()
    response = assistant.chat("hackathon")

    assert mock_create.called
    assert response == "MemoriAI response."
    
