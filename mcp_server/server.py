import json

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Banking-MCP")

DATA_FILE = "data/banking_data.json"


def load_data():
    """
    Summary:    
        Load customer banking data from the data file.

    Args:
        None

    Returns:
        dict: Parsed JSON data containing customer records and
        related banking information.
    """
    with open(DATA_FILE, "r") as f:
        return json.load(f)


@mcp.tool()
def fetch_customer(name: str) -> str:
    """
    summary:
        Retrieve customer information by name.

    Args:
        name (str): Name of the customer to look up (case-insensitive).

    Returns:
        str: String representation of the customer record if found,
        otherwise "Customer not found".
    """
    data = load_data()
    for c in data["customers"]:
        if c["name"].lower() == name.lower():
            return str(c)
    return "Customer not found"


@mcp.tool()
def fetch_balance(account_number: str) -> str:
    """
    Summary:    
        Retrieve the account balance for a given account number.

    Args:
        account_number (str): Unique account number of the customer.

    Returns:
        str: Account balance formatted as a currency string if the account
        exists; otherwise, returns "Account not found".
    """
    data = load_data()
    for c in data["customers"]:
        if c["account_number"] == account_number:
            return f"Balance: ₹{c['balance']}"
    return "Account not found"


@mcp.tool()
def fetch_transactions(account_number: str) -> str:
    """
    Summary:
        Retrieve transaction history for a given account number.

    Args:
        account_number (str): Unique account number of the customer.

    Returns:
        str: String representation of the customer's transaction history
        if the account exists; otherwise, returns "Account not found".
    """
    data = load_data()
    for c in data["customers"]:
        if c["account_number"] == account_number:
            return str(c["transactions"])
    return "Account not found"


if __name__ == "__main__":
    mcp.run()

