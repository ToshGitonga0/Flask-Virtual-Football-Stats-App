from flask import Flask, render_template
from summarystatistics import TeamStatistics
from scrape_link import scrape_link


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    
    data = scrape_link()

    team_stats = TeamStatistics(data)
    team_stats.process_matches()

    top_teams_by_total_goals = team_stats.get_top_teams('total_goals')
    top_teams_by_wins = team_stats.get_top_teams('wins')
    top_teams_by_losses = team_stats.get_top_teams('losses')
    top_teams_by_draws = team_stats.get_top_teams('draws')
    top_teams_by_home_goals = team_stats.get_top_teams('home_goals')
    top_teams_by_away_goals = team_stats.get_top_teams('away_goals')
    top_teams_by_avg_goals = team_stats.get_average_goals()

    return render_template('results.html', 
                           top_teams_by_total_goals=top_teams_by_total_goals,
                           top_teams_by_wins=top_teams_by_wins,
                           top_teams_by_losses=top_teams_by_losses,
                           top_teams_by_draws=top_teams_by_draws,
                           top_teams_by_home_goals=top_teams_by_home_goals,
                           top_teams_by_away_goals=top_teams_by_away_goals,
                           top_teams_by_avg_goals=top_teams_by_avg_goals)

if __name__ == '__main__':
    app.run(debug=True)
