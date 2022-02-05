import requests

class Weather:
    def __init__(self):
        self.api_url = "http://api.weatherapi.com/v1/current.json"
        self.access_key = "<api_key>"
    def getWeather(self,city):
        response = requests.get(self.api_url, params= { 
            "key": self.access_key,
            "q": city
        })
        return response.json()
        
    def run(self):
        city = input("City: ")
        result = self.getWeather(city)
        print(f"{result['location']['name']} / {result['location']['country']} is currently {result['current']['temp_c']} degrees and {result['current']['condition']['text']}.")

    
def main():
    app = Weather()
    app.run()

main()