import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urljoin # For joining next page url with base url
import re
import sys


class title_scraper():
    #Scrape a dataframe based on a keyword

    def __init__(self, keyword):
        self.keyword = keyword

    def scrape(self, outfile, max_ = 50):
        base_url = 'https://www.imdb.com/find?s=tt&q=' + '+'.join(self.keyword) + '&ref_=nv_sr_sm'

        data = []

        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(base_url, headers=headers)
        bs = BeautifulSoup(response.text, "html.parser")
        i = 0

        for movie in bs.find_all('td', 'result_text'): # find the href of each movie
            movie_url = movie.find('a').get('href')
            try: # Someimes the pages are weirdly fomatted, but its rare
                data.append(list(self.scrape_individual_movie(movie_url)))
            except:
                continue
            i += 1
            if i > max_: break


        df = pd.DataFrame(data, columns=['Title', 'Ratings', 'Number of Ratings', 'Genres', 'Release Date', 'World Wide Gross']) # convert to dataframe
        df.to_csv(outfile + '.csv')
        return df

    def scrape_individual_movie(self, movie_href):  #pull the data from each href
        movie_url = 'https://www.imdb.com' + movie_href #build the url
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(movie_url, headers=headers)
        bs = BeautifulSoup(response.text, "html.parser")
        gross = None
        for h4 in bs.find_all('h4'):
            if "Cumulative Worldwide Gross:" in h4:
                gross = h4.next_sibling.strip()
        data = bs.select("[type='application/ld+json']")[0]
        oJson = json.loads(data.text)
        title = oJson['name']
        rating = oJson['aggregateRating']['ratingValue']
        n_ratings = oJson['aggregateRating']['ratingCount']
        genre = oJson['genre']
        releaseDate = oJson['datePublished']
        if not gross is None: gross = int(re.sub(r'[$,]', '', gross))
        if type(genre) == str:
            genre = [genre]
        print('Scraping ' + title)
        return title, rating, n_ratings, ' '.join(genre), releaseDate, gross


class best_move_scraper():
    #Scrape the data from a number of imdb top lists

    def __init__(self):
        url1 = 'https://www.imdb.com/chart/bottom?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=QD93KC997JHV2JYYFTB3&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_ql_8'
        url2 = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
        url3 = 'https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=MFAVZA7VRFBFW6PVAM4J&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_3'
        self.urls = [url1, url2, url3]

    def scrape(self, outfile, _max = 100000, debug = False):
        data = []
        i = 0
        headers = {'User-Agent': 'Mozilla/5.0'}
        for url in self.urls:
            response = requests.get(url, headers=headers)
            bs = BeautifulSoup(response.text, "html.parser")
            if debug: print(bs.contents)
            for movie in bs.find_all('td', 'titleColumn'):
                movie_url = movie.find('a').get('href')
                try:
                    data.append(list(self.scrape_individual_movie(movie_url)))
                    i += 1
                except:
                    continue
                if i > _max: break

        print(data)

        df = pd.DataFrame(data, columns=['Title', 'Ratings', 'Number of Ratings', 'Genres', 'Release Date', 'World Wide Gross'])
        df.to_csv(outfile + '.csv')
        return df

    def scrape_individual_movie(self, movie_href):
        movie_url = 'https://www.imdb.com' + movie_href
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(movie_url, headers=headers)
        bs = BeautifulSoup(response.text, "html.parser")
        gross = None
        for h4 in bs.find_all('h4'):
            if "Cumulative Worldwide Gross:" in h4:
                gross = h4.next_sibling.strip()
        data = bs.select("[type='application/ld+json']")[0]
        oJson = json.loads(data.text)
        title = oJson['name']
        rating = oJson['aggregateRating']['ratingValue']
        n_ratings = oJson['aggregateRating']['ratingCount']
        genre = oJson['genre']
        releaseDate = oJson['datePublished']
        if not gross is None: gross = int(re.sub(r'[$,]', '', gross))
        if type(genre) == str:
            genre = [genre]

        print('Scraping ' + title)
        return title, rating, n_ratings, ' '.join(genre), releaseDate, gross

def imdb_scrape_top(outfile = 'Untitled'):
    best_move_scraper().scrape(outfile)

def imdb_scrape_search_term(search_term, outfile = 'Untitled'):
    title_scraper(search_term).scrape(outfile)

if __name__ == '__main__':
    imdb_scrape_search_term('star wars', 'out1')