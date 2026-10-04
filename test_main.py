import os
import pytest
from unittest.mock import patch, MagicMock

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


@patch("main.client.chat.completions.create")
def test_chat_method(mock_create):
    """Test chat execution using mocked global client."""
    mock_message = MagicMock()
    mock_message.content = "MemoriAI response."

    mock_choice = MagicMock()
    mock_choice.message = mock_message

    mock_response = MagicMock()
    mock_response.choices = [mock_choice]

    mock_create.return_value = mock_response

    assistant = main.MemoriAIAssistant()
    response = assistant.chat("hackathon")

    assert response == "MemoriAI response."
    assert mock_create.called
    
