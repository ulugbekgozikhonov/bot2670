# import sqlite3

# db = sqlite3.connect(database="mars.db")
# cur = db.cursor()

# cur.execute(""" CREATE TABLE IF NOT EXISTS student(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name VARCHAR(125) NOT NULL,
#             age INTEGER,
#             davlat VARCHAR(125),
#             phone_number VARCHAR(50),
#             gender BOOLEAN
#             )""")

# students = [
# ("Ali Karimov", 20, "Uzbekistan", "+998901000001", 1),
# ("John Smith", 22, "United States", "+12025550001", 1),
# ("Emma Johnson", 21, "Canada", "+14035550002", 0),
# ("Liam Brown", 23, "United Kingdom", "+447700900001", 1),
# ("Olivia Davis", 24, "Australia", "+61491570156", 0),
# ("Noah Wilson", 25, "Germany", "+4915112345678", 1),
# ("Ava Martinez", 22, "France", "+33612345678", 0),
# ("William Anderson", 26, "Italy", "+393331234567", 1),
# ("Sophia Thomas", 23, "Spain", "+34600123456", 0),
# ("James Taylor", 27, "Netherlands", "+31612345678", 1),

# ("Isabella Moore", 20, "Belgium", "+32470123456", 0),
# ("Benjamin Jackson", 28, "Switzerland", "+41791234567", 1),
# ("Mia Martin", 22, "Austria", "+436641234567", 0),
# ("Lucas Lee", 24, "Sweden", "+46701234567", 1),
# ("Charlotte Perez", 21, "Norway", "+4790123456", 0),
# ("Henry White", 23, "Denmark", "+4520123456", 1),
# ("Amelia Harris", 25, "Finland", "+358401234567", 0),
# ("Alexander Clark", 26, "Poland", "+48500123456", 1),
# ("Evelyn Lewis", 24, "Czech Republic", "+420601234567", 0),
# ("Daniel Walker", 27, "Slovakia", "+421901234567", 1),

# ("Harper Hall", 22, "Hungary", "+36301234567", 0),
# ("Michael Allen", 23, "Romania", "+40740123456", 1),
# ("Abigail Young", 21, "Bulgaria", "+359881234567", 0),
# ("Ethan King", 24, "Greece", "+306912345678", 1),
# ("Ella Wright", 22, "Portugal", "+351912345678", 0),
# ("Jacob Scott", 25, "Ireland", "+353871234567", 1),
# ("Aria Green", 23, "Iceland", "+3546112345", 0),
# ("Logan Adams", 26, "Ukraine", "+380671234567", 1),
# ("Scarlett Baker", 20, "Belarus", "+375291234567", 0),
# ("Mason Nelson", 27, "Lithuania", "+37061234567", 1),

# ("Chloe Carter", 22, "Latvia", "+37120123456", 0),
# ("Elijah Mitchell", 24, "Estonia", "+37251234567", 1),
# ("Victoria Perez", 23, "Luxembourg", "+352621234567", 0),
# ("Sebastian Roberts", 28, "Liechtenstein", "+4237912345", 1),
# ("Grace Turner", 21, "Monaco", "+37761234567", 0),
# ("David Phillips", 25, "San Marino", "+378661234567", 1),
# ("Lily Campbell", 22, "Malta", "+35699123456", 0),
# ("Joseph Parker", 26, "Cyprus", "+35796123456", 1),
# ("Hannah Evans", 24, "Japan", "+819012345678", 0),
# ("Matthew Edwards", 23, "South Korea", "+821012345678", 1),

# ("Zoe Collins", 27, "China", "+8613712345678", 0),
# ("Samuel Stewart", 21, "India", "+919812345678", 1),
# ("Nora Sanchez", 22, "Pakistan", "+923001234567", 0),
# ("Jack Morris", 25, "Bangladesh", "+8801712345678", 1),
# ("Leah Rogers", 23, "Sri Lanka", "+94771234567", 0),
# ("Owen Reed", 24, "Nepal", "+9779812345678", 1),
# ("Avery Cook", 22, "Bhutan", "+97517123456", 0),
# ("Gabriel Morgan", 26, "Thailand", "+66811234567", 1),
# ("Luna Bell", 20, "Vietnam", "+84901234567", 0),
# ("Anthony Murphy", 27, "Malaysia", "+60123456789", 1),

# ("Aria Rivera", 22, "Singapore", "+6591234567", 0),
# ("Christopher Cooper", 23, "Indonesia", "+6281234567890", 1),
# ("Layla Richardson", 25, "Philippines", "+639171234567", 0),
# ("Andrew Cox", 24, "Cambodia", "+85591234567", 1),
# ("Penelope Howard", 21, "Laos", "+8562012345678", 0),
# ("Joshua Ward", 26, "Myanmar", "+959123456789", 1),
# ("Riley Torres", 22, "Mongolia", "+97699123456", 0),
# ("Nathan Peterson", 28, "Kazakhstan", "+77011234567", 1),
# ("Sofia Gray", 23, "Kyrgyzstan", "+996701234567", 0),
# ("Aaron Ramirez", 24, "Tajikistan", "+992901234567", 1),

# ("Camila James", 22, "Turkmenistan", "+99365123456", 0),
# ("Ryan Watson", 27, "Iran", "+989121234567", 1),
# ("Ellie Brooks", 21, "Iraq", "+9647712345678", 0),
# ("Jonathan Kelly", 26, "Saudi Arabia", "+966501234567", 1),
# ("Violet Sanders", 24, "United Arab Emirates", "+971501234567", 0),
# ("Dylan Price", 23, "Qatar", "+97455123456", 1),
# ("Stella Bennett", 22, "Kuwait", "+96550123456", 0),
# ("Isaac Wood", 25, "Oman", "+96890123456", 1),
# ("Aurora Barnes", 24, "Jordan", "+962791234567", 0),
# ("Hudson Ross", 27, "Israel", "+972501234567", 1),

# ("Brooklyn Henderson", 23, "Egypt", "+201001234567", 0),
# ("Charles Coleman", 26, "South Africa", "+27821234567", 1),
# ("Savannah Jenkins", 22, "Nigeria", "+2348012345678", 0),
# ("Thomas Perry", 24, "Kenya", "+254712345678", 1),
# ("Claire Powell", 21, "Ethiopia", "+251912345678", 0),
# ("Julian Long", 25, "Ghana", "+233201234567", 1),
# ("Paisley Patterson", 23, "Morocco", "+212612345678", 0),
# ("Isaiah Hughes", 28, "Algeria", "+213551234567", 1),
# ("Madelyn Flores", 24, "Tunisia", "+21620123456", 0),
# ("Christian Washington", 22, "Argentina", "+5491112345678", 1),

# ("Anna Butler", 25, "Brazil", "+5511912345678", 0),
# ("Levi Simmons", 23, "Chile", "+56912345678", 1),
# ("Lucy Foster", 24, "Colombia", "+573001234567", 0),
# ("Nathaniel Gonzales", 26, "Peru", "+51912345678", 1),
# ("Bella Bryant", 21, "Mexico", "+5215512345678", 0),
# ("Connor Alexander", 27, "Cuba", "+5351234567", 1),
# ("Madison Russell", 22, "Dominican Republic", "+18091234567", 0),
# ("Adam Griffin", 25, "Panama", "+50761234567", 1),
# ("Ruby Diaz", 24, "Costa Rica", "+50683123456", 0),
# ("Eli Hayes", 26, "New Zealand", "+64211234567", 1),
# ]

# cur.executemany(""" INSERT INTO student(name,age,davlat,phone_number,gender)
#                 VALUES(?,?,?,?,?)""",students)

# studentlar = cur.execute("SELECT * FROM student WHERE gender = ? AND age >  ? AND age < ? ",(True,20,25)).fetchall()
# for student in studentlar:
#     print(student[1],student[2],student[3],student[-1])

# db.commit()
# db.close()

import sqlite3

def create_table():
    db = sqlite3.connect(database="mars.db")
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id BIGINTEGER NOT NULL UNIQUE,
        ism VARCHAR(125) NOT NULL,
        yosh INTEGER,
        davlat VARCHAR(125),
        millat VARCHAR(125) 
    )""")
    db.commit()
    db.close()

def insert_user(data: dict):
    db = sqlite3.connect(database="mars.db")
    cur = db.cursor()
    cur.execute("""INSERT INTO users(id, ism, yosh, davlat, millat)
        VALUES(?,?,?,?,?)
    """, (data.get('id'), data.get('ism'), data.get('yosh'), data.get('davlat'), data.get('millat')))
    db.commit()
    db.close()


def get_user(id: int):
    db = sqlite3.connect(database="mars.db")
    cur = db.cursor()
    users = cur.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
    db.close()
    return users