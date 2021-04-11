from bs4 import BeautifulSoup
import lxml
import http.server
import socketserver
import server
import requests
from time import sleep


def find_jobs():
    r = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=Turkey').text
    soup = BeautifulSoup(r, 'lxml')
    cards = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    with open('results.txt', 'w') as results:
        for card in cards:
            job_title = card.find('a').text.replace(' ', '').strip()
            company_name = card.find(
                'h3', class_='joblist-comp-name').text.replace(' ', '').strip()
            key_skills = card.find('ul', class_='list-job-dtl clearfix').find(
                'span', class_='srp-skills').text.replace(' ', '').strip()
            posted_when = card.find('span', class_='sim-posted').span.text
            more_info = card.find('h2').a['href']
            results.write(job_title+' / ')
            results.write(company_name + '\n')
            results.write('Key skills: ' + key_skills + '\n')
            results.write('More info: ' + more_info + '\n')
            results.write(posted_when+'\n')
            results.write('*******************************'*2 + '\n')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 60
        print(f'Waiting {time_wait} seconds')
        sleep(60)
