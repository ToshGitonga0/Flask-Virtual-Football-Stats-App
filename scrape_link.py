from odiscraper import Scraper
from parsehtml import Parser
import pandas as pd

def scrape_link():

    URL = "https://www.odibets.com"
    DRIVER_PATH = "/users/tosh/downloads/chromedriver"
    OUTPUT_HTML_FILE = "data/odibets.html"
    OUTPUT_CSV_FILE = "data/odibets.csv"

    LEAGUE_XPATH = "//*[@id='menu-list']/li[4]"
    RESULTS_XPATH = "//*[@id='app']/div/div[5]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/ul/li[2]"
    RESULTS_HTML_XPATH = "//*[@id='app']/div/div[5]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div"

    scraper = Scraper(URL, DRIVER_PATH)
    scraper.setup_driver()
    scraper.scrape_html(LEAGUE_XPATH, RESULTS_XPATH, RESULTS_HTML_XPATH, OUTPUT_HTML_FILE)

    parser = Parser(OUTPUT_HTML_FILE)
    parser.parse_html()
    parser.save_to_csv(OUTPUT_CSV_FILE)

    data = pd.read_csv(OUTPUT_CSV_FILE)
    return data