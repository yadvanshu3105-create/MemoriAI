import os
import pytest
from unittest.mock import patch, MagicMock

import main


def test_memory_retrieval_found():
    """Test memory retrieval works when relevant keywords match."""
    assistant = main.MemoriAIAssistant()
    context = assistant.retrieve_memories("Tell me about Nebius Cloud")
    assert "Nebius Cloud" in context


def test_memory_retrieval_not_found():
    """Test search when no terms match memory store."""
    assistant = main.MemoriAIAssistant()
    context = assistant.retrieve_memories("weather forecast Tokyo")
    assert context == "No prior context found."


@patch("main.OpenAI")
def test_chat_method(mock_openai_class):
    """Test chat execution using mocked OpenAI client."""
    # Set up mock OpenAI instance and its chat completion chain
    mock_client = MagicMock()
    mock_openai_class.return_value = mock_client

    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="MemoriAI response."))
    ]
    mock_client.chat.completions.create.return_value = mock_response

    assistant = main.MemoriAIAssistant()
    response = assistant.chat("hackathon")

    assert response == "MemoriAI response."
    
