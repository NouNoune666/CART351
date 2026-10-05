import requests

from rich.console import Console
from rich.table import Table
console = Console()

url = "https://swapi.info/api/planets"
def fetch_swapi_data():
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for HTTP errors
        data = response.json()
        # print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

data = fetch_swapi_data() #returns a list
#each item on the list is a dictionary

# testing testing
# print(len(data))
# print(data[0]["name"])

if data: 
    table = Table(title="Star Wars API Exercise")
    table.add_column("NAME", justify="left", style="#D0429B")
    table.add_column("DIAMETER", justify="left", style ="#3B719E")
    table.add_column("POPULATION", justify="left", style="#197373")

    for planets in data[0:13]:
        name = (planets["name"])
        diameter = (planets["diameter"])
        population = (planets["population"])
       
        table.add_row(name, diameter, population)

console.print(table)