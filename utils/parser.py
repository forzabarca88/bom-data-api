from bs4 import BeautifulSoup

class BomPage(object):
    '''
    base class for parsing BOM page
    '''
    def __init__(self, url):
        self._url = url

    def _parse(self):
        raise NotImplementedError

    def get_data(self):
        raise NotImplementedError