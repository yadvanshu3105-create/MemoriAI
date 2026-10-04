import os
import pytest
from unittest.mock import MagicMock

import main


def test_memory_retrieval_found():
    """Test memory retrieval returns matching stored memory."""
    assistant = main.MemoriAIAssistant()
    context = assistant.retrieve_memories("Tell me about Nebius Cloud")
    assert "Nebius Cloud" in context


def test_memory_retrieval_not_found():
    """Test memory retrieval returns fallback string when no keywords match."""
    assistant = main.MemoriAIAssistant()
    context = assistant.retrieve_memories("weather forecast Tokyo")
    assert context == "No prior context found."


def test_chat_method():
    """Test chat method response without making real API network requests."""
    assistant = main.MemoriAIAssistant()

    # 1. Build the expected OpenAI return object structure: response.choices[0].message.content
    mock_message = MagicMock()
    mock_message.content = "MemoriAI response."

    mock_choice = MagicMock()
    mock_choice.message = mock_message

    mock_response = MagicMock()
    mock_response.choices = [mock_choice]

    # 2. Replace the real API client method with a mock object returning mock_response
    assistant.client.chat.completions.create = MagicMock(return_value=mock_response)

    # 3. Call chat method
    response = assistant.chat("hackathon")

    # 4. Assert response matches mocked content and API method was invoked
    assert response == "MemoriAI response."
    assert assistant.client.chat.completions.create.called
    
