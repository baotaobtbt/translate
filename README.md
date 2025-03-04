翻译工具
这是一个简单的图形界面翻译工具，基于百度翻译 API，支持中文到英文和英文到中文的互译。程序使用 Python 编写，结合 tkinter 提供用户友好的界面，适用于日常翻译需求。

功能特点
双向翻译：支持中文到英文和英文到中文的翻译。
剪贴板操作：可以粘贴剪贴板内容到输入框，或将翻译结果复制到剪贴板。
简洁界面：使用 tkinter 构建，带有背景图片和直观的按钮布局。
错误提示：翻译失败时会显示错误信息，便于排查问题。
依赖库
requests：用于发起 HTTP 请求调用百度翻译 API。
hashlib：用于生成百度翻译 API 的签名。
tkinter：用于创建图形用户界面。
PIL (Pillow)：用于加载和处理背景图片。
json：用于解析 API 返回的 JSON 数据。
安装步骤
安装 Python

确保你的系统已安装 Python 3.6 或以上版本。可从 Python 官方网站 下载安装。

安装依赖库

打开终端或命令行，运行以下命令安装所需库：

bash
pip install requests Pillow
（tkinter、hashlib、json、os、sys 等为 Python 内置模块，无需额外安装。）

获取百度翻译 API 密钥

注册 百度翻译开放平台 账号。
创建应用获取 APP_ID 和 SECRET_KEY。
在代码中替换以下部分：
python
APP_ID = '你的APP ID'
SECRET_KEY = '你的密钥'
准备背景图片

将一张名为 bg.jpg 的图片放入程序所在目录（推荐尺寸 500x500 像素）。

运行程序

将代码保存为 translator.py，然后在终端运行：

python translator.py
使用方法
启动程序

运行脚本后，会弹出一个 500x500 像素的窗口。

输入文本

在“输入文本”框中手动输入需要翻译的内容。
或点击“粘贴文本”按钮，从剪贴板导入内容。
选择翻译方向

在下拉菜单中选择“中文到英文”或“英文到中文”。

翻译

点击“翻译”按钮，翻译结果会显示在“翻译结果”框中。

复制结果

点击“复制结果”按钮，将翻译内容复制到剪贴板。

文件结构
translator/

├── translator.py    # 主程序文件

├── bg.jpg           # 背景图片文件

└── README.md        # 本说明文件

注意事项
API 限制：百度翻译 API 有免费额度限制，超出需要付费，具体请参考百度官方文档。
网络连接：程序需联网才能调用翻译 API。

问题排查
翻译失败：检查 APP_ID 和 SECRET_KEY 是否正确，或确认网络是否正常。
图片加载失败：确保 bg.jpg 文件存在且路径正确。
贡献
欢迎提交问题或改进建议！请通过 GitHub 或其他方式联系作者。

许可
本项目仅供学习和个人使用。
