import os
import pytest
from unittest.mock import patch, MagicMock
import main


def test_memory_retrieval_found():
    """Test that memory retrieval finds matching context based on query terms."""
    assistant = main.MemoriAIAssistant()
    context = assistant.retrieve_memories("Tell me about Nebius Cloud")
    
    assert "Nebius Cloud" in context
    assert "NVIDIA Nemotron-4 340B" in context


def test_memory_retrieval_not_found():
    """Test behavior when query terms do not match memory store."""
    assistant = main.MemoriAIAssistant()
    context = assistant.retrieve_memories("What is the weather in Tokyo?")
    
    assert context == "No prior context found."


@patch("main.client.chat.completions.create")
def test_chat_method(mock_create):
    """Test that chat constructs system prompt with memory and triggers OpenAI API."""
    # Mock Nebius API response structure
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="MemoriAI runs on NVIDIA Nemotron-4 340B."))
    ]
    mock_create.return_value = mock_response

    assistant = main.MemoriAIAssistant()
    response = assistant.chat("hackathon")

    # Assert API was called with system prompt containing retrieved context
    assert mock_create.called
    call_args = mock_create.call_args[1]
    assert call_args["model"] == "nvidia/nemotron-4-340b-instruct"
    assert call_args["temperature"] == 0.2
    
    # Verify retrieved context was injected into system prompt
    system_message = call_args["messages"][0]["content"]
    assert "hackathon project named MemoriAI" in system_message
    assert response == "MemoriAI runs on NVIDIA Nemotron-4 340B."
    
