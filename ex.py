import pandas as pd
import requests
import numpy as np



class minor_class:

    def __init__(self) -> None:
        self.url = 'https://api.census.gov/data'
        self.dataset = "/timeseries/poverty/saipe?"
        self.variable = 'get=NAME,SAEPOV0_17_PT'
        self.county = '&for=county:201'
        self.state = '&in=state:48'
        self.year = '&time=2018'
        self.apikey = '&key=339cb547571cda5f3e85d818a501d3821e13077a'

    def call_url(self):
        assembled_url = f'{self.url}{self.dataset}{self.variable}{self.county}{self.state}{self.year}{self.apikey}'
        getrequest = requests.get(assembled_url).json() 
        return getrequest

   

    def to_csv(self):
        arr = self.call_url()
        headers = ['county_name', '<18_in_poverty', 'year', 'state_id', 'county_id']
        df = pd.DataFrame(np.array(arr[1:]), columns=headers)
        dfcsv = df.to_csv('minor.csv', index=False)
        return dfcsv


class total_pop_class:

    def __init__(self) -> None:
        self.url = 'https://api.census.gov/data'
        self.dataset = "/timeseries/poverty/saipe?"
        self.variable = 'get=NAME,SAEPOVALL_PT'
        self.county = '&for=county:201'
        self.state = '&in=state:48'
        self.year = '&time=2018'
        self.apikey = '&key=339cb547571cda5f3e85d818a501d3821e13077a'
        
    def call_url(self):
        assembled_url = f'{self.url}{self.dataset}{self.variable}{self.county}{self.state}{self.year}{self.apikey}'
        getrequest = requests.get(assembled_url).json()
        return getrequest

   
    def to_csv(self):
        arr = self.call_url()
        headers = ['county_name', 'total_poverty', 'year', 'state_id', 'county_id']
        df = pd.DataFrame(np.array(arr[1:]), columns=headers)
        dfcsv = df.to_csv('totalpop.csv', index=False)
        return dfcsv


class median_income:

    def __init__(self) -> None:
        self.url = 'https://api.census.gov/data'
        self.dataset = "/timeseries/poverty/saipe?"
        self.variable = 'get=NAME,SAEMHI_PT'
        self.county = '&for=county:201'
        self.state = '&in=state:48'
        self.year = '&time=2018'
        self.apikey = '&key=339cb547571cda5f3e85d818a501d3821e13077a'
        
    def call_url(self):
        assembled_url = f'{self.url}{self.dataset}{self.variable}{self.county}{self.state}{self.year}{self.apikey}'
        getrequest = requests.get(assembled_url).json()
        return getrequest
 

    def to_csv(self):
        arr = self.call_url()
        headers = ['county_name', 'median_income', 'year', 'state_id', 'county_id']
        df = pd.DataFrame(np.array(arr[1:]), columns=headers)
        dfcsv = df.to_csv('income.csv', index=False)
        return dfcsv


minor_object = minor_class()
total_object = total_pop_class()
median_object = median_income()

minor_object.call_url()
minor_object.to_csv()

total_object.call_url()
total_object.to_csv()

median_object.call_url()
median_object.to_csv()
