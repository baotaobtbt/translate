import requests
import hashlib
import random
import json
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu
from PIL import Image, ImageTk
import os
import sys

# 百度翻译 API 配置信息
APP_ID = 'APP ID'  # 替换为你的APP ID
SECRET_KEY = '替换为你的密钥'  # 替换为你的密钥


# 获取资源路径的函数
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # 打包后的临时路径
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def baidu_translate(query, from_lang='auto', to_lang='zh'):
    salt = str(random.randint(32768, 65536))
    sign = APP_ID + query + salt + SECRET_KEY
    sign = hashlib.md5(sign.encode()).hexdigest()

    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    params = {
        'q': query,
        'from': from_lang,
        'to': to_lang,
        'appid': APP_ID,
        'salt': salt,
        'sign': sign
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        result = json.loads(response.text)
        if 'trans_result' in result:
            return result['trans_result'][0]['dst']
        else:
            return "翻译失败，错误信息：" + str(result)
    else:
        return "请求失败，状态码：" + str(response.status_code)


def translate_text():
    text = entry_text.get("1.0", tk.END).strip()
    if not text:
        text_output.delete("1.0", tk.END)
        return

    selected_lang = lang_var.get()
    if selected_lang == "中文到英文":
        from_lang, to_lang = 'zh', 'en'
    else:
        from_lang, to_lang = 'en', 'zh'

    translated = baidu_translate(text, from_lang, to_lang)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, translated)


def copy_to_clipboard():
    root.clipboard_clear()
    translated_text = text_output.get("1.0", tk.END).strip()
    root.clipboard_append(translated_text)
    messagebox.showinfo("复制成功", "翻译结果已复制到剪贴板！")


def paste_from_clipboard():
    try:
        clipboard_text = root.clipboard_get()
        entry_text.delete("1.0", tk.END)
        entry_text.insert(tk.END, clipboard_text)
    except tk.TclError:
        messagebox.showwarning("粘贴失败", "剪贴板中没有可粘贴的内容！")


# 创建主窗口
root = tk.Tk()
root.title("小涛专用翻译")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# 设置窗口图标
icon_path = resource_path("bg.jpg")
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)

# 添加背景图片
bg_path = resource_path("bg.jpg")
bg_image = Image.open(bg_path)
bg_image = bg_image.resize((500, 500), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# 输入文本框
label_input = tk.Label(root, text="输入文本:", bg="#33ffff", font=("Arial", 12))
label_input.pack(pady=(10, 0))

entry_text = tk.Text(root, height=5, wrap=tk.WORD, font=("Arial", 12), bg="#cceeff")
entry_text.pack(padx=10, pady=10)

# 添加翻译按钮
btn_translate = tk.Button(root, text="翻译", command=translate_text, font=("Arial", 12))
btn_translate.pack(pady=(10, 0))

# 语言选择下拉菜单
lang_var = StringVar(root)
lang_var.set("中文到英文")

label_lang = tk.Label(root, text="选择翻译方向:", bg="#ccff99", font=("Arial", 12))
label_lang.pack(pady=(10, 0))

lang_options = ["中文到英文", "英文到中文"]
lang_menu = OptionMenu(root, lang_var, *lang_options)
lang_menu.pack(pady=(0, 10))

# 输出文本框
label_output = tk.Label(root, text="翻译结果:", bg="#ffff77", font=("Arial", 12))
label_output.pack(pady=(10, 0))

text_output = tk.Text(root, height=5, wrap=tk.WORD, font=("Arial", 12), bg="#cceeff")
text_output.pack(padx=10, pady=10)

# 复制和粘贴按钮
btn_copy = tk.Button(root, text="复制结果", command=copy_to_clipboard, font=("Arial", 12))
btn_copy.pack(side=tk.LEFT, padx=(10, 5), pady=(10, 0))

btn_paste = tk.Button(root, text="粘贴文本", command=paste_from_clipboard, font=("Arial", 12))
btn_paste.pack(side=tk.RIGHT, padx=(5, 10), pady=(10, 0))

# 运行主循环
root.mainloop()
