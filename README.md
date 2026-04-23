# README.md
```markdown
# MCP 从零开发实战项目
基于 Python 3.13 + FastMCP 实现自定义 MCP Server，包含文件读取工具、计算器工具，适配官方 MCP Inspector 调试器。

## 环境要求
- Python >= 3.13
- Conda 虚拟环境
- mcp & mcp[cli] 依赖库

## 1. 创建 Conda 虚拟环境
```bash
conda create -n MCP python=3.13
conda activate MCP
```

## 2. 安装依赖
```bash
pip install mcp mcp[cli]
```

## 3. 项目代码说明
项目文件 `test.py` 内置两个自定义 MCP 工具：
1. **get_desktop_files**
   获取当前用户桌面所有文件列表
2. **calculator**
   基础四则运算计算器，支持 `+ - * /`

## 4. 启动 MCP 服务
### 方式1：原生 stdio 后台服务启动
终端无任何输出即代表**服务启动成功、持续运行**
```bash
python test.py
```

### 方式2：MCP 官方调试器启动（推荐，用于调用测试）
```bash
mcp dev test.py
```
自动打开 MCP Inspector 网页调试界面。
<img width="1696" height="849" alt="image" src="https://github.com/user-attachments/assets/5938063f-b3b2-4a4d-9dd9-74b88c38f5ab" />
<img width="1401" height="598" alt="image" src="https://github.com/user-attachments/assets/ef4ccef8-b466-4e73-9179-0076dede9af4" />

## 5. MCP Inspector 配置与调用
网页调试器默认配置修改：
- 传输类型：`STDIO`
- 命令（command）：`python`
- 参数（args）：`test.py`

操作流程：
1. 修改配置后点击 **连接**
2. 左侧展示已注册工具
3. 选择工具填入对应参数，点击 `Call` 即可调用并返回结果
