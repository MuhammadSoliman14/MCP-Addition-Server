#!/usr/bin/env python3
"""
Simple MCP server using FastMCP that adds two numbers
"""

from fastmcp import FastMCP
from typing import Union
import os
import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

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

# Create FastAPI wrapper for HTTP access
app = FastAPI(title="MCP Addition Server")

@app.get("/")
async def root():
    return {"message": "MCP Addition Server is running", "tools": ["add_numbers"]}

@app.post("/add")
async def add_endpoint(x: Union[int, float], y: Union[int, float]):
    """HTTP endpoint for addition"""
    result = add_numbers(x, y)
    return {"result": result, "x": x, "y": y}

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)