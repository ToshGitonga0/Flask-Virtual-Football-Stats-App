# Flask Virtual Football Stats App

This is a **Flask web application** that scrapes football match data and processes statistics.

## Features
- **Scraping football match data**
- **Statistical Analysis** using **Pandas**
- **Web Interface** for displaying team statistics

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Flask-Virtual-Football-Stats-App.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
### Change WebDriver Path
Before running the project, ensure that you update the **Chrome WebDriver path** in the `scrape_link.py` file. Look for the `DRIVER_PATH` variable and set it to the correct path where your `chromedriver` is located.

In `scrape_link.py`, find this line:


DRIVER_PATH = "C:/path/to/your/chromedriver.exe"  # For Windows
# or
DRIVER_PATH = "/path/to/your/chromedriver"  # For macOS or Linux
