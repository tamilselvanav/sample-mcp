from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def add (a: int, b: int) -> int:
    """Add two integers."""
    return a + b