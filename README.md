# MemoriAI 🧠

Autonomous Private Virtual Assistant with Long-Term Context Memory

MemoriAI is a privacy-first, autonomous virtual assistant designed to overcome context limits and high API overhead in LLMs. Powered by NVIDIA Nemotron-4 340B on Nebius AI Cloud, MemoriAI provides low-latency, contextual interactions using dynamic memory indexing and real-time tool execution.

## ✨ Key Architectural Features

- 🧠 Persistent Memory Indexing: Dynamic indexing structures user preferences and facts into retrievable nodes rather than blowing up context windows.

- ⚡ Nebius AI Inference: Leverages NVIDIA Nemotron-4 340B for fast, sub-second response times and complex spatial/logical reasoning.

- 🔒 Privacy-First Design: Memory persistence is managed locally/encrypted, ensuring sensitive user context stays private.

- 🛠 Dynamic Tool Execution: Agentic workflows support real-time JSON tool calls without model drift.

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.10+

- pip package manager

### 1. Installation

Clone the repository and install required dependencies:

git clone https://github.com/yadvanshu3105-create/MemoriAI.git

cd MemoriAI

pip install -r requirements.txt
