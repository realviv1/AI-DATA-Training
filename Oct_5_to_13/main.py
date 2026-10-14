# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="cinema_demo",
    user="postgres",
    password="Admin@123"
)

cursor = conn.cursor()

print("Connected to PostgreSQL")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS screenings (
#     screening_id SERIAL PRIMARY KEY,
#     movie_name VARCHAR(100),
#     screen_number INT,
#     show_time VARCHAR(20),
#     available_seats INT
# )
# """)
#
# conn.commit()
#
# print("Table created")

# cursor.execute("""
# INSERT INTO screenings
# (movie_name, screen_number, show_time, available_seats)
# VALUES
# ('Silent Horizon', 1, '10:00 AM', 65),
# ('Red Planet', 2, '01:30 PM', 42),
# ('Ocean Signal', 3, '04:00 PM', 18),
# ('Silent Horizon', 1, '07:00 PM', 25)
# """)
#
# conn.commit()
#
# print("Records inserted")


# cursor.execute("SELECT * FROM screenings")
#
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)

# cursor.execute("""
# SELECT movie_name, show_time, available_seats
# FROM screenings
# WHERE available_seats < 30
# """)
#
# for row in cursor.fetchall():
#     print(row)

# cursor.execute("""
# UPDATE screenings
# SET available_seats = available_seats - 5
# WHERE screening_id = 3
# """)
#
# conn.commit()

# cursor.execute("""
# DELETE FROM screenings
# WHERE screening_id = 4
# """)
#
# conn.commit()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS rooms (
#     room_id SERIAL PRIMARY KEY,
#     room_name VARCHAR(100),
#     capacity INTEGER,
#     HOURLY_RATE DECIMAL(10,2),
#     status VARCHAR(50)
# );
# """)
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS bookings (
#     booking_id SERIAL PRIMARY KEY,
#     room_id INTEGER,
#     booked_by VARCHAR(100),
#     booking_date DATE,
#     hours INTEGER,
#     FOREIGN KEY (room_id)
#         REFERENCES rooms(room_id)
# );
# """)
# conn.commit()
#
# print("Tables created successfully")
#
#
# cursor.execute("""
# INSERT INTO rooms (room_name, capacity, hourly_rate, status)
# VALUES
# ('Focus Room', 4, 500.00, 'Available'),
# ('Conference Room', 12, 1200.00, 'Available'),
# ('Creative Studio', 8, 800.00, 'Available'),
# ('Board Room', 15, 1500.00, 'Available');
# """)
#
# cursor.execute("""
# INSERT INTO bookings (room_id, booked_by, booking_date, hours)
# VALUES
# (1, 'Amit', '2026-10-01', 2),
# (2, 'Rahul', '2026-10-02', 4),
# (3, 'Priya', '2026-10-03', 3),
# (1, 'Neha', '2026-10-04', 1),
# (4, 'Vivek', '2026-10-05', 5),
# (3, 'Ankit', '2026-10-06', 2);
# """)
#
# conn.commit()

# cursor.execute("SELECT * FROM rooms")
#
# for row in cursor.fetchall():
#     print(row)
#
# cursor.execute("SELECT * FROM bookings")
#
# for row in cursor.fetchall():
#     print(row)
# cursor.execute("""
# SELECT * FROM rooms
# WHERE capacity > 6
# """)
#
# for row in cursor.fetchall():
#     print(row)
#
# cursor.execute("""
# SELECT * FROM rooms
# WHERE status='Available'
# """)
#
# for row in cursor.fetchall():
#     print(row)
#
# cursor.execute("""
# SELECT * FROM bookings
# WHERE booked_by='Vivek'
# """)
#
# for row in cursor.fetchall():
#     print(row)

# cursor.execute("""
# UPDATE rooms
# SET hourly_rate = 600
# WHERE room_id = 1
# """)
#
# conn.commit()
#
# cursor.execute("SELECT * FROM rooms WHERE room_id=1")
# print(cursor.fetchone())

# cursor.execute("""
# UPDATE rooms
# SET status = 'Maintenance'
# WHERE room_id = 2
# """)
#
# conn.commit()
#
# cursor.execute("SELECT * FROM rooms WHERE room_id=2")
# print(cursor.fetchone())

# cursor.execute("""
# UPDATE bookings
# SET hours = hours + 2
# WHERE booking_id = 1
# """)
#
# conn.commit()
#
# cursor.execute("SELECT * FROM bookings WHERE booking_id=1")
# print(cursor.fetchone())

# cursor.execute("""
# DELETE FROM BOOKINGS
# WHERE booking_id = 7
# """)
#
# conn.commit()

# cursor.execute("select * FROM bookings")
#
# for row in cursor.fetchall():
#     print(row)

# cursor.execute("""
# SELECT
#     b.booking_id,
#     b.booked_by,
#     r.room_name,
#     b.booking_date,
#     b.hours,
#     r.hourly_rate
# FROM bookings b
# JOIN rooms r
# ON b.room_id = r.room_id
# """)
#
# for row in cursor.fetchall():
#     print(row)
#
#
# cursor.execute("""
# SELECT
#     r.room_name,
#     COUNT(b.booking_id)
# FROM rooms r
# LEFT JOIN bookings b
# ON r.room_id = b.room_id
# GROUP BY r.room_name
# """)
#
# for row in cursor.fetchall():
#     print(row)

# cursor.execute("""
# SELECT *
# FROM rooms
# ORDER BY hourly_rate DESC
# LIMIT 1
# """)
#
# print(cursor.fetchone())

cursor.execute("""
SELECT
    b.booked_by,
    r.room_name,
    b.hours,
    (b.hours * r.hourly_rate) AS booking_cost
FROM bookings b
JOIN rooms r
ON b.room_id = r.room_id
""")

for row in cursor.fetchall():
    print(row)

