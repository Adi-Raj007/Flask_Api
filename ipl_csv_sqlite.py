import sqlite3
import csv

# Function to create a SQLite database and populate it with data from a CSV file
def create_and_populate_database(csv_file, db_file):
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create a table to store IPL match data
    cursor.execute('''CREATE TABLE IF NOT EXISTS ipl_matches (
                        City TEXT,
                        Date TEXT,
                        Season TEXT,
                        MatchNumber TEXT,
                        Team1 TEXT,
                        Team2 TEXT,
                        TossWinner,
                        TossDecision,
                        SuperOver TEXT,
                        WinningTeam TEXT,
                        WonBy TEXT,
                        Margin REAL,
                        Player_of_Match TEXT
                      )''')

    # Read data from CSV file and insert into the table
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Insert data into the table
            cursor.execute('''INSERT INTO ipl_matches (
                                City, Date, Season, MatchNumber, Team1, Team2,TossWinner ,TossDecision, SuperOver, WinningTeam, WonBy,
                                Margin, Player_of_Match
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)''',
                           (row['City'], row['Date'], row['Season'],row['MatchNumber'], row['Team1'],
                            row['Team2'], row['TossWinner'] ,row['TossDecision'],row['SuperOver'],
                            row['WinningTeam'], row['WonBy'], row['Margin'] , row['Player_of_Match']))

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Example usage
if __name__ == '__main__':
    # Specify the CSV file and database file paths
    csv_file = '/home/aditya/Data science/Data_sets/filtered_data_ipl.csv'
    db_file = 'ipl_filter_data.db'

    # Create and populate the SQLite database
    create_and_populate_database(csv_file, db_file)
