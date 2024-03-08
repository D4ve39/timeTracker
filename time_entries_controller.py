import json
import requests # For http requests
import pandas as pd
import logging
from datetime import datetime


def date_formater():
    formated_date = ''
    return formated_date

def format_date_string(date_data):
    date_object = datetime.strptime(date_data, '%Y-%m-%d')
    return date_object.date()


def format_time_string(time_data):
    date_object = datetime.strptime(time_data, '%H:%M:%S')
    return date_object.time()

class TimeCampEntry:
    """This class represents a time camp entry, with all the parameters usable in the time camp API"""
    
    def __init__(self, entry: dict) -> None:
        self.id = entry['id']
        self.duration = entry['duration']  # total duration of the entry in seconds
        self.user_id = entry['user_id']
        self.user_name = entry['user_name']
        self.task_id = entry['task_id']
        self.task_note = entry['task_note']
        self.last_modify = entry['last_modify']
        self.date = entry['date']
        self.start_time = entry['start_time'] # Received strat time of current entry
        self.end_time = entry['end_time']  # Received end time of current entry
        self.locked = entry['locked']
        self.name = entry['name']
        self.addons_external_id = entry['addons_external_id']
        self.billable = entry['billable']
        self.invoice_id = entry['invoiceId']
        self.color = entry['color']
        self.description = entry['description']
    
    def print_attributes(self):
        print('TimeCampEntry Class Attributes')
        for attr, value in vars(self).items():
            print(f'{attr} : {value}')


class EntriesFetcher:
    """This class is responsible for fetching time entries from TimeCamp API. Returns a list of TimeCampEntries objects, each corresponding to a time entry in the time camp API.
    """
    def __init__(self):
        self.api_token = self.load_credentials()
        self.entries_url = "https://app.timecamp.com/third_party/api/entries" # entries endpoint
        self.headers = {
            'Accept': 'application/json',  # change to application/json for json format or csv for csv strings
            'Authorization': f'Bearer {self.api_token}'  # Replace with your actual access token
        }

    def load_credentials(self):
        with open('api_token.json') as f:
            data = json.load(f)
            return data['api_token']
        

    def fetch_time_entries_from_period(self, period_start: str, period_end:str):
        """Fetches the time entries between the given time periods.
        Args:
            period_start (str): Period start date, in Y-M-D format
            period_end (str): Period end date, in Y-M-D format
        Returns:
            list: List of TimeCampEntry objects, each corresponding to a time entry in the time camp API, fetched from the given period.
        """
        logger.debug(f'--- Fetching entries between the {period_start} and the {period_end}')
        params = {
            'from': period_start,
            'to': period_end,
        }
        response = requests.get(self.entries_url, headers=self.headers, params=params)
        
        if response.status_code == 200:
            data = response.text
            entries_dict = json.loads(data)
            logger.debug(f'Received entry dictionaries:\n {entries_dict}')
            timecamp_entries_lst = []
            for entry in entries_dict:
                timecamp_entries_lst.append(TimeCampEntry(entry))
            return timecamp_entries_lst
        else:
            logger.error(f"Failed to fetch data. Status code: {response.status_code}")
            return None
        
    def fetch_time_entries_from_day(self, day: str):
        return self.fetch_time_entries_from_period(day, day)

if __name__ == '__main__':
    from debug_logger import setup_debug_logger
    logger = setup_debug_logger()
    
    # Entries fetching
    entries_fetcher = EntriesFetcher()
    entries_lst = entries_fetcher.fetch_time_entries_from_period('2023-10-18', '2023-10-19')
    
    print(f'Fetched a total of {len(entries_lst)} entries')
    print(f'Fetched entries:\n {entries_lst}')
    