# 识别图片的文字 成功 上传至github
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxxpyautogui
# 打包命令 pyinstaller E:\python项目\自动化项目\main12.py --onefile --icon=E:\python项目\自动化项目\图标头像.ico
import pyperclip
import requests
from aip import AipOcr
import pyautogui
import datetime
import os
import time
import tkinter as tk
import tkinter.filedialog as fd
#""" 你的 APPID AK SK """
APP_ID = '去百度云申请一个文字识别api，每月免费1000次'
API_KEY = '去百度云申请一个文字识别api，每月免费1000次'
SECRET_KEY = '去百度云申请一个文字识别api，每月免费1000次'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
file_path =None
def select_file():
    root = tk.Tk()
    root.withdraw()
    global file_path
    file_path = fd.askopenfilename(filetypes=[("JPG图片", "*.jpg"), ("PNG图片", "*.png")], title="选择文件", multiple=False)
    if file_path:
        pyperclip.copy(file_path)
        print(".", end="")
        time.sleep(0.1)
        print(".", end="")
        time.sleep(0.1)
        print(".", end="")
        time.sleep(0.1)
        print(".", end="")
        time.sleep(0.1)
        print(".", end="")
        time.sleep(0.1)
        print(".", end="")
        time.sleep(0.1)
        print(".", end="")
        time.sleep(0.1)
        print(".", end="")
        time.sleep(0.1)
        print(".", end="")
        time.sleep(0.1)
        print("..........................................................................")
        time.sleep(1)
        print('图片已经获取，正在识别')
select_file()
""" 读取文件 """
def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()
image = get_file_content(file_path)
#url = "https://www.x.com/sample.jpg"
#pdf_file = get_file_content(file_name)
# 调用通用文字识别（标准版）
res_image = client.basicGeneral(image)
#res_url = client.basicGeneralUrl(url)
#res_pdf = client.basicGeneralPdf(pdf_file)
words_result = res_image.get("words_result")
words = [result.get("words") for result in words_result]
result = "\n".join(words)
#print(result)
#print(res_url)
#print(res_pdf)
pyperclip.copy(result)
print(".", end="")
time.sleep(0.1)
print(".", end="")
time.sleep(0.1)
print(".", end="")
time.sleep(0.1)
print(".", end="")
time.sleep(0.1)
print(".", end="")
time.sleep(0.1)
print(".", end="")
time.sleep(0.1)
print(".", end="")
time.sleep(0.1)
print(".", end="")
time.sleep(0.1)
print(".", end="")
time.sleep(0.1)
print("..........................................................................")
time.sleep(1)
print("识别的内容已经如下，并且已经复制到剪贴板")
print("..........................................................................")
print(result)
print("..........................................................................")











