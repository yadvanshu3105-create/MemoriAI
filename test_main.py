import os
import pytest
from unittest.mock import patch, MagicMock


@patch("openai.OpenAI")
def test_memory_retrieval_found(mock_openai):
    """Test memory retrieval works when relevant keywords match."""
    import main
    assistant = main.MemoriAIAssistant()
    context = assistant.retrieve_memories("Tell me about Nebius Cloud")
    assert "Nebius Cloud" in context


@patch("openai.OpenAI")
def test_memory_retrieval_not_found(mock_openai):
    """Test search when no terms match memory store."""
    import main
    assistant = main.MemoriAIAssistant()
    context = assistant.retrieve_memories("weather forecast Tokyo")
    assert context == "No prior context found."


@patch("openai.OpenAI")
def test_chat_method(mock_openai_class):
    """Test chat execution using mocked OpenAI client."""
    # Set up mock response BEFORE creating the assistant
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="MemoriAI response."))
    ]
    mock_client.chat.completions.create.return_value = mock_response
    mock_openai_class.return_value = mock_client

    import main
    assistant = main.MemoriAIAssistant()
    response = assistant.chat("hackathon")

    assert response == "MemoriAI response."
    
