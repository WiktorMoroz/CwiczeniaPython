
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

departures = []

departures.append(flights[0][-1])
departures.append(flights[1][-1])
departures.append(flights[2][-1])
departures.append(flights[3][-1])
print(departures)