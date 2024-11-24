from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    @staticmethod
    def convert_to_24hr(time_str):
        try:
            return datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")
        except ValueError:
            return time_str

    def parse_html(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            html = f.read()

        soup = BeautifulSoup(html, 'html.parser')
        
        for week in soup.find_all("div", class_="rs"):
            time_str = week.find("div", class_="rs-t").find_all("div")[1].text.strip()
            converted_time = self.convert_to_24hr(time_str)  # Convert time to 24-hour format

            teams = week.find_all("div", class_="rs-g")
            for team in teams:
                team1 = team.find_all("div")[0].text.strip()
                team2 = team.find_all("div")[2].text.strip()
                score1 = team.find_all("div")[1].find_all("span")[0].text.strip()
                score2 = team.find_all("div")[1].find_all("span")[1].text.strip()
                self.data.append({
                    "time": converted_time,
                    "home_team": team1,
                    "away_team": team2,
                    "home_score": score1,
                    "away_score": score2
                })

    def save_to_csv(self, output_csv):
        df = pd.DataFrame(self.data)
        df.to_csv(output_csv, index=False)
        print(f"Data saved to {output_csv}")
