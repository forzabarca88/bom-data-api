from bs4 import BeautifulSoup
import requests
from bomparser import BomParser

class BomRequest(object):
    '''
    Class used for managing requests for data from BOM
    '''

    def __init__(self):
        self.urls = BomUrls()
        self.parser = BomParser()

    def get_all_summary_observations(self):
        raise NotImplementedError

class BomUrls(object):
    '''
    Class for managing the various URLs for BOM data
    '''

    def __init__(self):
        self._base_url = 'http://www.bom.gov.au'
        self._site_map_url = '/site-map'
        self._site_map_data = self._get_site_map_data()
        self._site_map_links = self._site_map_data.find_all('a')
        self._state_map = {
            'vic': {
                'title': 'Latest Weather Observations for Victoria',
                'url': None
                },
            'nsw': {
                'title': 'Latest Weather Observations for New South Wales',
                'url': None
                },
            'wa': {
                'title': 'Latest Weather Observations for Western Australia',
                'url': None
                },
            'nt': {
                'title': 'Latest Weather Observations for Northern Territory',
                'url': None
                },
            'sa': {
                'title': 'Latest Weather Observations for South Australia',
                'url': None
                },
            'act': {
                'title': 'Latest Weather Observations for the Canberra Area',
                'url': None
                },
            'qld': {
                'title': 'Latest Weather Observations for Queensland',
                'url': None
                }
        }
        self._get_summary_observations()

    def _get_site_map_data(self):
        data = requests.get('{}{}'.format(self._base_url, self._site_map_url)).text
        return BeautifulSoup(data, 'lxml')

    def _get_summary_observations(self):
        for state in self._state_map:
            for link in self._site_map_links:
                if link.get('title', '').lower().find(
                        self._state_map[state]['title'].lower()) == 0:
                    self._state_map[state]['url'] = link.get('href')
                    break
        
