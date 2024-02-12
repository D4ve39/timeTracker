import json
import requests # For http requests
import csv
import pandas as pd

def date_formater():
    formated_date = ''
    return formated_date



class EntriesFetcher:
    """This class is responsible for fetching time entries from TimeCamp API.
    """
    def __init__(self):
        self.api_token = '4a3c73ea8861c4d8eeb10ec734'
        self.entries_url = "https://app.timecamp.com/third_party/api/entries" # entries endpoint
        self.headers = {
            'Accept': 'application/json',  # change to application/json for json format or csv for csv strings
            'Authorization': 'Bearer 4a3c73ea8861c4d8eeb10ec734'  # Replace with your actual access token
        }

    def fetch_time_entries_in_period(self, period_start: str, period_end:str):
        params = {
            'from': period_start,
            'to': period_end
        }
        response = requests.get(self.entries_url, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.text
            entries_json = json.load(data)
            entries_df = pd.read_json(entries_json)
            df.to_csv("time_entries.csv", entries_df)
            return entries_df
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

class EntriesWritter:
    def __init__(self):
        self.api_token = '4a3c73ea8861c4d8eeb10ec734'
        self.entries_url = "https://app.timecamp.com/third_party/api/entries"
        self.headers = {
            'Accept': 'application/json',  # change to application/json for json format or csv for csv strings
            'Authorization': 'Bearer 4a3c73ea8861c4d8eeb10ec734'  # Replace with your actual access token
        }

    def write_time_entry(self, start_time: str, end_time: str, duration):
        pass





if __name__ == '__main__':
    entries_fetcher = EntriesFetcher()
    entries = entries_fetcher.fetch_time_entries_in_period('2023-10-01', '2023-10-04')
    print(entries)

