flights = [
    [
        'United Airlines',
        'UA123',
        'New York',
        'Los Angeles',
        '10:00 AM',
    ],
    [
        'Delta Airlines',
        'DL456',
        'Chicago',
        'Houston',
        '11:30 AM',
    ],
    [
        'American Airlines',
        'AA789',
        'Dallas',
        'San Francisco',
        '08:15 AM',
    ],
    [
        'Southwest Airlines',
        'WN012',
        'Los Angeles',
        'Denver',
        '09:45 AM',
    ],
]

delta_airlines = flights.pop(1)
print(len(flights))
flights.append(delta_airlines)
flight_number = []
flight_number.append(flights[0][1])
flight_number.append(flights[1][1])
flight_number.append(flights[2][1])
flight_number.append(flights[3][1])
print(flight_number)