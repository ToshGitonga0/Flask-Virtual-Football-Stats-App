import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:
    def __init__(self, url, driver_path):
        self.url = url
        self.driver_path = driver_path
        self.driver = None
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        ]

    def setup_driver(self):
        user_agent = random.choice(self.user_agents)
        chrome_options = Options()

        chrome_options.add_argument(f"user-agent={user_agent}")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

        chrome_service = Service(self.driver_path)

        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def scrape_html(self, league_xpath, results_xpath, results_html_xpath, output_file):
        self.driver.get(self.url)
        print("\n")
        print("="*30, "Successful", "="*30)
        print("\n")

        wait = WebDriverWait(self.driver, 10)

        try:
            close_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.roadblock-close button")))
            close_button.click()
            print("Modal closed successfully.")
        except Exception as e:
            print("No modal found or unable to close modal:")

        
        # Navigate through elements
        l_button = wait.until(EC.visibility_of_element_located((By.XPATH, league_xpath)))
        l_button.click()
        time.sleep(2)

        r_button = wait.until(EC.visibility_of_element_located((By.XPATH, results_xpath)))
        r_button.click()
        time.sleep(5)
        
        # Get the HTML content
        element = wait.until(EC.visibility_of_element_located((By.XPATH, results_html_xpath)))
        html_content = element.get_attribute('outerHTML')
        
        # Save to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print("HTML content saved to file.")
        self.driver.quit()
