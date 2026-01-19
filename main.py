import asyncio
from agents.banking_agent import banking_agent

bank_agent = asyncio.run(banking_agent())
async def run_main():
    print("\n Banking MCP Agent Ready\n")

    query1 = "Get customer details for Rahul Sharma"
    response1 = await bank_agent.ainvoke({"messages":[{"role":"user", "content":query1}]})
    print(response1["messages"][-1].content)
    query2 = "What is the balance of account ACC1002?"
    response2 = await bank_agent.ainvoke({"messages":[{"role":"user", "content":query2}]})
    print(response2["messages"][-1].content)
    query3 = "Show transaction history for ACC1001"
    response3=await bank_agent.ainvoke({"messages":[{"role":"user", "content":query3}]})
    print(response3["messages"][-1].content)

if __name__ == "__main__":
    
    asyncio.run(run_main())


