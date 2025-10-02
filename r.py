from browser_use import Agent, ChatGoogle, Browser, Tools
from dotenv import load_dotenv
import asyncio
import pyperclip
import google.generativeai as genai
import os
import aiohttp
import pyautogui
import time
from pywinauto import Application

tools = Tools()

@tools.action(description='save image as to a folder')
async def download_and_save():
    custom_dir = r"e:\fxx"
    custom_name = "brave_saved_img.jpg"
    save_path = os.path.join(custom_dir, custom_name)

    # 1. Right-click in the center of screen
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    pyautogui.rightClick(center_x, center_y)
    time.sleep(1)

    # 2. "Save image as…" from context menu
    # 2. Press keyboard shortcut (usually "v" selects "Save image as..." in Chrome/Brave)
    pyautogui.press('v')
    time.sleep(1.5)

    # 3. Type full path in Save dialog
    pyautogui.typewrite(save_path)
    time.sleep(0.5)

    # 4. Press Enter to save
    pyautogui.press('enter')

    print("✅ Image saved to:", save_path)

load_dotenv()

llm = ChatGoogle(model="gemini-2.5-flash")

browser = Browser(
    executable_path='C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe',
    user_data_dir=' C:\\Users\\Muzahir\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data',
    profile_directory='Profile 2'
)

downdir = f"e:\\xx"

task = f"""
  - go to https://gemini.google.com/u/0/app/42bf913c108eb212
  - wait for chat to load
  - hover over and click on 'generated image'
  - wait for it to open
  - don't click on download button 
  - just save image as to folder
"""

agent = Agent(
    task=task, 
    browser=browser,
    llm=llm, 
    tools=tools
    )

async def main():
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
