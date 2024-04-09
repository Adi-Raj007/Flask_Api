import sqlite3

# connect to database
conn = sqlite3.connect('ipl.db')
# create a cursor
 
c = conn.cursor()
ipl_data =[
    ("1","2024-03-22", "CSK", "RCB","176-173"),
    ("2","2024-03-29", "PBKS", "DC",  "177-174"),
    ( "3","2024-03-29", "KKR", "SRH",  "208-204"),
    ("4", "2024-03-29", "RR",  "LSG",  "193-173"),
    ( "5","2024-03-29", "GT",  "MI",  "168-162"),
    ( "6","2024-03-29", "RCB", "PBKS", "178-176"),
    ("7", "2024-03-29", "CSK", "GT", "206-143"),
    ("8", "2024-03-29", "SRH", "MI", "277-246"),
    ("9", "2024-03-29", "RR",  "DC", "185-173"),
    ("10", "2024-03-29", "KKR", "RCB",  "186-182"),
    ("11", "2024-03-29", "LSG", "PKBS", "199-178")

         ]
c.executemany("INSERT INTO ipl_matches VALUES (?,?,?,?,?)",ipl_data)
print("command  success")
conn.commit()
conn.close()
