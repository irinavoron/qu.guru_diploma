import os

from selene import browser
import allure
from allure_commons.types import AttachmentType


def add_screenshot():
    png = browser.driver.get_screenshot_as_png()
    allure.attach(png, 'screenshot', AttachmentType.PNG, '.png')


def add_logs():
    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'logs', AttachmentType.TEXT, '.log')


def add_html():
    html = browser.driver.page_source
    allure.attach(html, 'html', AttachmentType.HTML, '.html')


def add_video():
    selenoid_url = os.getenv('SELENOID_URL')
    video_url = f'https://{selenoid_url}/video/{browser.driver.session_id}.mp4'
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video', AttachmentType.HTML, '.html')
