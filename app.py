from flask import Flask, render_template, url_for, request
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)


def getVals():
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
    arr = []
    for item, event_name in zip(content, event_names):
        # Extracting start date and time, end date and time, and event description using regular expressions
        match = re.match(pattern, item.get_text(strip=True))
        if match:
            date_time_start = match.group('date_time_start')
            date_time_end = match.group('date_time_end')
            event_description = match.group('location')
            print("Event Name:", event_name)
            print("Start Date and Time:", date_time_start)
            print("Location:", event_description)
            print()
            arr.append([event_name, (date_time_start + " to " + date_time_end), event_description])
    return arr




@app.route('/')
@app.route('/home')
def home():
    html = ''
    names = getVals()
    print(names)
    index = 0

    with open('templates/map.html', 'r') as file:
        line = file.readline()
        while line:
            if 'name: \"' in line and index < len(names):
                html+= 'name: "' + names[index][0] + '",\n'
                html+= 'date: "' + names[index][1] + '",\n'
                html+= 'address: "' + names[index][2] + '",\n'
                file.readline()
                file.readline()
                index+=1
            else:
                html += line
            line = file.readline()
    with open('templates/map.html', 'w') as file:
        file.write(html)

    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)