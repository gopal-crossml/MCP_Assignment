
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient  
from constant import MODEL
from cred import gemini_api_key
import asyncio


async def banking_agent():

    client = MultiServerMCPClient(  
        {
            "Banking": {
                "transport": "stdio",  # Local subprocess communication
                "command": "python",
                # Absolute path to your math_server.py file
                "args": ["/home/gopalchopra/projects/MCP_Assignment/mcp_server/server.py"]
            }
            }
    )

    # Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model = MODEL,
        api_key = gemini_api_key,
        temperature = 0.2
    )

    # Convert MCP tools -> LangChain tools
    tools = await client.get_tools()

    # Agent
    banking_agent = create_agent(
        model = llm,
        tools = tools
    )

    return banking_agent

