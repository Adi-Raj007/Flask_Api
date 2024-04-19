from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Function to fetch IPL match data from SQLite database
def fetch_ipl_matches():
    conn = sqlite3.connect('ipl_filter_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ipl_matches")
    rows = cursor.fetchall()
    conn.close()
    matches = []
    for row in rows:
        match = {
            "City": row[0],
            "Date": row[1],
            "Season": row[2],
            "MatchNumber": row[3],
            "Team1": row[4],
            "Team2": row[5],
            "TossWinner": row[6],
            "TossDecision": row[7],
            "SuperOver": row[8],
            "WinningTeam": row[9],
            "WonBy": row[10],
            "Margin": row[11],
            "Player_of_Match": row[12],
        }
        matches.append(match)
    return matches




@app.route('/ipl_matches', methods=['GET'])
def get_ipl_matches():
    matches = fetch_ipl_matches()
    return jsonify({"matches": matches})


if __name__ == '__main__':
    app.run(debug=True)
