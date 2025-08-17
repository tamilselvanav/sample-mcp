## Name
Sample mcp server - It's simple mcp server to two integers.
  
## Installation

To install this MCP server using `uvx`, run the following command:

```sh
uvx --from git+https://github.com/tamilselvanav/sample-mcp.git mcp-server
```

This will add the MCP server as specified in the configuration:

```json
{
	"mcpServers": {
		"add_tool": {
			"command": "uvx",
			"args": [
				"--from",
				"git+https://github.com/tamilselvanav/sample-mcp.git",
				"mcp-server"
			]
		}
	}
}
```
