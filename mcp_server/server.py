import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Banking-MCP")

DATA_FILE = "data/banking_data.json"


def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


@mcp.tool()
def fetch_customer(name: str) -> str:
    data = load_data()
    for c in data["customers"]:
        if c["name"].lower() == name.lower():
            return str(c)
    return "Customer not found"


@mcp.tool()
def fetch_balance(account_number: str) -> str:
    data = load_data()
    for c in data["customers"]:
        if c["account_number"] == account_number:
            return f"Balance: ₹{c['balance']}"
    return "Account not found"


@mcp.tool()
def fetch_transactions(account_number: str) -> str:
    data = load_data()
    for c in data["customers"]:
        if c["account_number"] == account_number:
            return str(c["transactions"])
    return "Account not found"


if __name__ == "__main__":
    mcp.run()


# from mcp.server.fastmcp import FastMCP
# from tools.banking_tools import (
#     get_customer_details,
#     get_account_balance,
#     get_transaction_history
# )

# mcp = FastMCP("Banking MCP Server")


# @mcp.tool()
# def fetch_customer_details(name: str) -> str:
#     return get_customer_details(name)


# @mcp.tool()
# def fetch_account_balance(account_number: str) -> str:
#     return get_account_balance(account_number)


# @mcp.tool()
# def fetch_transaction_history(account_number: str) -> str:
#     return get_transaction_history(account_number)


# if __name__ == "__main__":
#     mcp.run()
