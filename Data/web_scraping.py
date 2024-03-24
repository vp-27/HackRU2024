import requests
from bs4 import BeautifulSoup
import re

# Making a GET request
r = requests.get('https://newbrunswick.rutgers.edu/events')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Finding the desired content
s = soup.find('div', class_='events-list')
content = s.find_all('p')

# Regular expression pattern to match date, start time, end time, and event description
pattern = r'(?P<date_time_start>.*?)\s*-\s*(?P<date_time_end>.*?)\s*\|\s*(?P<event>.*)'

# Processing each item in the content
for item in content:
    # Extracting start date and time, end date and time, and event description using regular expressions
    match = re.match(pattern, item.get_text(strip=True))
    if match:
        date_time_start = match.group('date_time_start')
        date_time_end = match.group('date_time_end')
        event_description = match.group('event')
        print("Start Date and Time:", date_time_start)
        print("End Date and Time:", date_time_end)
        print("Event:", event_description)
        print()