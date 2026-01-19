# MCP Assignment – Agentic Banking System

## 📌 Overview

This project demonstrates an **Agentic Banking System** built using **MCP (Model Context Protocol)**, **LangChain**, and **Google Generative AI (Gemini)**. The system simulates banking operations such as retrieving customer details, account balances, and transaction history using **agents and tools** exposed through an MCP server.

The LLM interacts with banking data by calling tools via an **MCP client**, showcasing how intelligent agents can dynamically reason and act on structured data instead of relying on hard-coded logic.

---

## ⚙️ Technologies Used

* **Python 3.10+**
* **LangChain**
* **FastMCP / MCP**
* **Google Generative AI (Gemini)**
* **JSON** (for banking data storage)

---

## 🔑 Environment Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/gopal-crossml/MCP_Assignment.git
cd MCP_Assignment
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
source env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_api_key_here
```

---

## 🏦 Sample Banking Data

The `data/banking_data.json` file contains sample customer records:

* Account number
* Customer name
* Balance
* Transaction history

This data is accessed **only through MCP tools**, not directly by the agent.

---

## 🧠 MCP Server

The MCP server (`mcp_server/server.py`) exposes banking operations as tools, such as:

* Get account balance
* Get customer details
* Get transaction history

These tools are registered using MCP decorators and are callable by the LLM.

Start the MCP server:

```bash
python mcp_server/server.py
```

---

## 🤖 Banking Agent

The agent (`agents/banking_agent.py`) is built using LangChain and:

* Connects to the MCP server
* Uses Gemini LLM
* Decides which tool to call based on user queries

The agent **does not access data directly**—it always goes through MCP tools.

---

## ▶️ Running the Project

Run the main entry point:

```bash
python main.py
```

You can then ask queries like:

* "What is the balance of account 1001?"
* "Show transactions for account 1002"
* "Give customer details for account 1003"

---

## 🎯 Key Learning Outcomes

* Understanding **Model Context Protocol (MCP)**
* Building **tool-driven agents**
* Separating data access from reasoning logic
* Integrating **LangChain + Gemini + MCP**
* Designing scalable agentic systems

---

## 🚀 Future Enhancements

* Add write operations (deposit / withdraw)
* Integrate database instead of JSON
* Add authentication & authorization
* Multiple specialized agents (Fraud, Support, Analytics)

---

## 👨‍💻 Author

**Gopal Chopra**
MCP & Agentic AI Practice Project

---

## 📄 License

This project is for educational purposes only.
