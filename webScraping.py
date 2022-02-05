
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
    list = soup.find("tbody",{"class":"lister-list"}).finda_all("tr")
    
    
    for tr in list:
        title = tr.find("td",{"class":"titleColumn"}).find("a").text
        year = tr.find("td",{"class":"titleColumn"}).find("span").text
        rate = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
        header.append(title)
        years.append(year)
        imdb_rating.append(rate.strong.text)

    for i in range(0, len(header)):
        print("Name of the Movie: {} Year: {} IMBD Rating: {}".format(header[i],years[i] ,imdb_rating[i]))


main()