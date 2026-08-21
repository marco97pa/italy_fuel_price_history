import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Official MIMIT website URL for fuel prices in Italy
URL = "https://www.mimit.gov.it/it/prezzo-medio-carburanti/regioni"

resp = requests.get(URL)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "html.parser")

""" Get all prices for a specific fuel type passed as a parameter """
def get_all_prices(fuel_name):
    prices = []

    # Find all <th> elements with the specified fuel name (each one corresponds to a region)
    headers = soup.find_all(
        "th",
        scope="row",
        string=lambda s: s and fuel_name in s
    )
    
    for th in headers:
        # Find the parent row <tr> of the <th> element
        tr = th.find_parent("tr")
        if not tr:
            continue

        # Find all <td> cells in the row
        tds = tr.find_all("td")
        if not tds:
            continue

        # The price is the last cell (PREZZO MEDIO)
        price_cell = tds[-1]
        price = price_cell.get_text(strip=True)
        prices.append(float(price))

    return prices

""" Calculate the average of a list of numbers """
def average(array):
    return round(sum(array) / len(array) if array else 0, 3)

""" Append the average price to a CSV file """
def append_average_to_csv(gasoline, diesel,filename="average_prices.csv"):
    # Get current date
    date = datetime.now().strftime("%Y-%m-%d")
    # Append the average prices to the CSV file
    with open(filename, "a") as f:
        f.write(f"{date},{gasoline},{diesel}\n")

""" Main execution """
diesel_avg = average(get_all_prices("Gasolio"))
gasoline_avg = average(get_all_prices("Benzina"))
print(f"Average Gasoline Price: {gasoline_avg} euro/litres")
print(f"Average Diesel Price: {diesel_avg} euro/litres")
append_average_to_csv(gasoline_avg, diesel_avg)