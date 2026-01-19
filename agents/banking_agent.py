import asyncio

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

from constant import MODEL
from cred import gemini_api_key
from prompt import system_prompt


async def banking_agent() :
    """
    Summary:
        Initialize and return a banking agent integrated with MCP and Gemini LLM.

        This function creates an MCP client that connects to a local banking
        MCP server using stdio communication. It initializes a Google Gemini
        language model, converts the MCP-exposed tools into LangChain tools,
        and creates an agent configured with a predefined banking system prompt.

    Returns:
        Any: A LangChain agent instance capable of handling banking-related
             operations by invoking MCP tools.
    """

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
        tools = tools,
        system_prompt = system_prompt
    )

    return banking_agent

