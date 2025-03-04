翻译工具
项目简介
这是一个基于 Python 的简单翻译工具，使用百度翻译 API 提供中英文互译功能。工具采用图形界面（GUI），通过 tkinter 实现，适合初学者和日常使用。支持文本输入、翻译、复制和粘贴功能，同时具有美观的界面设计和背景图片。

功能特点
双向翻译：支持中文到英文和英文到中文的翻译。
剪贴板操作：可以粘贴剪贴板内容到输入框，或将翻译结果复制到剪贴板。
美观界面：使用自定义背景图片和彩色标签，增强用户体验。
错误提示：翻译失败时会显示清晰的错误信息。
跨平台支持：可在 Windows、macOS 和 Linux 上运行。
安装要求
Python 版本：Python 3.6 或以上。
依赖库：
requests：用于发送 HTTP 请求。
hashlib：生成签名所需的 MD5 加密。
tkinter：创建图形界面（通常内置于 Python）。
Pillow：处理背景图片。
百度翻译 API：
需要注册百度翻译开放平台账号（https://fanyi-api.baidu.com/）。
获取 APP_ID 和 SECRET_KEY，并替换代码中的占位符。
安装依赖库：

bash
pip install requests Pillow
使用说明
准备工作：

将 APP_ID 和 SECRET_KEY 填入代码中的对应位置：
python
APP_ID = '你的APP ID'
SECRET_KEY = '你的密钥'
确保 bg.jpg 文件（背景图片）与脚本在同一目录下，或通过 resource_path 函数正确加载。
运行程序：

直接运行脚本：
bash
python translation_tool.py
程序启动后会显示一个 500x500 像素的窗口。
操作步骤：

在“输入文本”框中输入需要翻译的内容，或点击“粘贴文本”从剪贴板粘贴。
在“选择翻译方向”下拉菜单中选择翻译方向（中文到英文或英文到中文）。
点击“翻译”按钮，翻译结果会显示在“翻译结果”框中。
点击“复制结果”按钮，将翻译结果复制到剪贴板。
文件结构
translation_tool/
├── translation_tool.py   # 主程序脚本
├── bg.jpg                # 背景图片
└── README.md             # 使用说明文档
注意事项
网络连接：程序需要联网访问百度翻译 API。
API 限制：免费版百度翻译 API 有请求频率和字符数限制，超过限制可能导致翻译失败。
图片文件：若 bg.jpg 缺失，程序仍可运行，但背景将不可见。
打包支持：使用 resource_path 函数支持 PyInstaller 打包，确保图片资源正确嵌入。
常见问题
翻译失败怎么办？

检查 APP_ID 和 SECRET_KEY 是否正确。
确保网络连接正常。
查看输出框中的错误信息，例如状态码或 API 返回的错误。
窗口图标或背景不显示？

确认 bg.jpg 文件路径正确，或检查 Pillow 库是否安装。
欢迎提交问题或改进建议！可以通过 GitHub 或其他方式联系作者。
