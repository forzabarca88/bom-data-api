from bs4 import BeautifulSoup

class BomParser(object):
    '''
    base class for parsing BOM pages
    '''

    def __init__(self, BomRequest):
        _parent_request = BomRequest

    def parse_summary_header(self):
        pass