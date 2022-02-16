import requests
from bs4 import BeautifulSoup

def main():
    request_func()
    

def request_func():
    html = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    request = requests.get(html)
    status = request.status_code
    print("Status: ",status)
    if status == 200:
        print("We've been contacted. The shredding process begins...")
        parse_html(request)
    else:
        print("Connection failed.")

def parse_html(url):
    header=[]
    imdb_rating= []
    years = []
    soup = BeautifulSoup(url.text,"html.parser")
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    
    
    for movie in movies:
        title = movie.find('td' , class_="titleColumn").a.text
        year = movie.find('td', class_="titleColumn").span.text.strip('()')
        header.append(title)
        years.append(year)

    for i in range(0, len(header)):
        print("Name of the Movie: {} Year: {}".format(header[i],years[i]))


main()