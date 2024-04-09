

from flask import Flask, jsonify

app = Flask(__name__)

# Sample IPL match data
ipl_matches = [
    {"date": "2024-03-22", "winner": "CSK", "loser": "RCB", "score": "176-173"},
    {"date": "2024-03-29", "winner": "PBKS", "loser": "DC", "score": "177-174"},
    {"date": "2024-03-29", "winner": "KKR", "loser": "SRH", "score": "208-204"},
    {"date": "2024-03-29", "winner": "RR", "loser": "LSG", "score": "193-173"},
    {"date": "2024-03-29", "winner": "GT", "loser": "MI", "score": "168-162"},
    {"date": "2024-03-29", "winner": "RCB", "loser": "PBKS", "score": "178-176"},
    {"date": "2024-03-29", "winner": "CSK", "loser": "GT", "score": "206-143"},
    {"date": "2024-03-29", "winner": "SRH", "loser": "MI", "score": "277-246"},
    {"date": "2024-03-29", "winner": "RR", "loser": "DC", "score": "185-173"},
    {"date": "2024-03-29", "winner": "KKR", "loser": "RCB", "score": "186-182"},
    {"date": "2024-03-29", "winner": "LSG", "loser": "PKBS", "score": "199-178"},
    # Add more matches as needed
]

@app.route('/ipl_matches', methods=['GET'])
def get_ipl_matches():
    return jsonify({"matches": ipl_matches})

@app.route('/ipl_matches/<int:match_id>', methods=['GET'])
def get_ipl_match(match_id):
    if match_id < 0 or match_id >= len(ipl_matches):
        return jsonify({"error": "Match not found"}), 404
    return jsonify(ipl_matches[match_id])

if __name__ == '__main__':
    app.run(debug=True)
