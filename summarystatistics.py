import pandas as pd

class TeamStatistics:
    def __init__(self, data):
        self.data = data
        self.team_stats = self._initialize_team_stats()

    def _initialize_team_stats(self):
        stats = {}
        for team in set(self.data['home_team']).union(set(self.data['away_team'])):
            stats[team] = {
                'home_goals': 0,
                'away_goals': 0,
                'total_goals': 0,
                'draws': 0,
                'wins': 0,
                'losses': 0,
                'matches_played': 0,
                'form': ''
            }
        return stats

    def process_matches(self):
        for index, row in self.data.iterrows():
            home_team = row['home_team']
            away_team = row['away_team']
            home_score = row['home_score']
            away_score = row['away_score']

            # Update stats
            self._update_team_stats(home_team, away_team, home_score, away_score)

        # Update form for all teams
        for team in self.team_stats.keys():
            self.team_stats[team]['form'] = self._calculate_team_form(team)

    def _update_team_stats(self, home_team, away_team, home_score, away_score):
        self.team_stats[home_team]['home_goals'] += home_score
        self.team_stats[away_team]['away_goals'] += away_score
        self.team_stats[home_team]['total_goals'] += home_score
        self.team_stats[away_team]['total_goals'] += away_score
        self.team_stats[home_team]['matches_played'] += 1
        self.team_stats[away_team]['matches_played'] += 1

        if home_score == away_score:
            self.team_stats[home_team]['draws'] += 1
            self.team_stats[away_team]['draws'] += 1
        elif home_score > away_score:
            self.team_stats[home_team]['wins'] += 1
            self.team_stats[away_team]['losses'] += 1
        else:
            self.team_stats[away_team]['wins'] += 1
            self.team_stats[home_team]['losses'] += 1

    def _calculate_team_form(self, team):
        # Filter matches involving the team
        team_matches = self.data[
            (self.data['home_team'] == team) | (self.data['away_team'] == team)
        ].sort_values(by='time', ascending=False)

        last_5_matches = team_matches.head(5)

        form = []
        for _, match in last_5_matches.iterrows():
            if match['home_team'] == team:
                if match['home_score'] > match['away_score']:
                    form.append('W')
                elif match['home_score'] == match['away_score']:
                    form.append('D')
                else:
                    form.append('L')
            elif match['away_team'] == team:
                if match['away_score'] > match['home_score']:
                    form.append('W')
                elif match['away_score'] == match['home_score']:
                    form.append('D')
                else:
                    form.append('L')

        return "-".join(form)

    def get_top_teams(self, stat_name):
        sorted_teams = sorted(self.team_stats.items(), key=lambda x: x[1][stat_name], reverse=True)
        top_teams = []
        for i, (team, stats) in enumerate(sorted_teams[:3]):
            top_teams.append({
                'rank': i + 1,
                'team': team,
                'stat': stats[stat_name],
                'form': stats['form']
            })
        return top_teams

    def get_average_goals(self):
        avg_goals_per_team = {team: stats['total_goals'] / stats['matches_played'] for team, stats in self.team_stats.items()}
        sorted_avg_goals = sorted(avg_goals_per_team.items(), key=lambda x: x[1], reverse=True)
        avg_goals = []
        for i, (team, avg_goals_value) in enumerate(sorted_avg_goals[:3]):
            form = self.team_stats[team]['form']
            avg_goals.append({
                'rank': i + 1,
                'team': team,
                'avg_goals': round(avg_goals_value, 2),
                'form': form
            })
        return avg_goals