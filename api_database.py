from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


# Function to fetch IPL matches from SQLite database
def fetch_ipl_matches():
    conn = sqlite3.connect('ipl.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ipl_matches")
    rows = cursor.fetchall()
    conn.close()
    matches = []
    for row in rows:
        match = {"id": row[0], "date": row[1], "winner": row[2], "loser": row[3], "score": row[4]}
        matches.append(match)
    return matches

@app.route('/ipl_matches', methods=['GET'])
def get_ipl_matches():
    matches = fetch_ipl_matches()
    return jsonify({"matches": matches})

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)
