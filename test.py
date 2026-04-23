import os
from mcp.server.fastmcp import FastMCP

# 创建 MCP 服务，名称为 FileSystem
mcp = FastMCP("FileSystem")

# 工具1：获取桌面文件列表
@mcp.tool()
def get_desktop_files() -> list:
    """获取当前用户的桌面文件列表"""
    return os.listdir(os.path.expanduser("~/Desktop"))

# 工具2：基础计算器
@mcp.tool()
def calculator(a: float, b: float, operator: str) -> float:
    """执行基础数学运算（支持 + - * /）
    Args:
        operator: 运算符，必须是 '+', '-', '*', '/' 之一
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        raise ValueError("无效运算符")

if __name__ == "__main__":
    # 启动服务，使用 stdio 传输
    mcp.run(transport='stdio')