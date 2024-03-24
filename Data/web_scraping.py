from flask import Flask
import requests
from bs4 import BeautifulSoup
import re


app = Flask(__name__)
@app.route('/')
@app.route('/home')

def home():
    return render
# Make a GET request
r = requests.get('https://newbrunswick.rutgers.edu/events')

# Parse the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Finding the desired content
s = soup.find('div', class_='events-list')
content = s.find_all('p')

# Regular expression pattern to match date, start time, end time, and event description
pattern = r'(?P<date_time_start>.*?)\s*-\s*(?P<date_time_end>.*?)\s*\|\s*(?P<location>.*)'

# Extracting event names
event_names = [event.text.strip() for event in s.find_all('h3')]

# Processing each item in the content
for item, event_name in zip(content, event_names):
    # Extracting start date and time, end date and time, and event description using regular expressions
    match = re.match(pattern, item.get_text(strip=True))
    if match:
        date_time_start = match.group('date_time_start')
        date_time_end = match.group('date_time_end')
        event_description = match.group('location')
        print("Event Name:", event_name)
        print("Start Date and Time:", date_time_start)
        print("End Date and Time:", date_time_end)
        print("Location:", event_description)
        print()