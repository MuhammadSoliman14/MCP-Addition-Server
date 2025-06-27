#!/usr/bin/env python3
"""
Simple MCP server using FastMCP that adds two numbers
"""

from fastmcp import FastMCP
from typing import Union

# Create the MCP server
mcp = FastMCP("Addition Server")

@mcp.tool()
def add_numbers(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together.
    
    Args:
        x: First number to add
        y: Second number to add
    
    Returns:
        The sum of x and y
    """
    result = x + y
    return result

if __name__ == "__main__":
    import os
    # Get port from environment (Render provides this)
    port = int(os.environ.get("PORT", 8000))
    # Run the server on the specified port
    mcp.run(port=port, host="0.0.0.0")