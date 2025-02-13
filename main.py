from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from send_emails import create_and_send_emails


ROOT_FOLDER = Path(__file__).parent
EXECUTABLE_PATH = ROOT_FOLDER / 'bin' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    for option in options:
        chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=EXECUTABLE_PATH
    )

    browser = webdriver.Chrome(
        chrome_options,
        chrome_service,
    )

    return browser


options = '--headless',
browser = make_chrome_browser(*options)

url = 'https://www.amazon.com.br/Lian-Li-O11Vision-'\
    'Computador-Traseira-O11VPW/dp/B0DJPY63XL'

browser.get(url)

product_name = browser.find_element(By.ID, 'productTitle').text
results = browser.find_element(By.ID, 'corePrice_feature_div')
results_tags = results.find_elements(By.TAG_NAME, 'span')

product_price = ''.join((
    results_tags[4].text, ',', results_tags[6].text
)).replace('.', '').replace(',', '.')


if float(product_price) < 1100:
    create_and_send_emails(product_name, url)
