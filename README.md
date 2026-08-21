This project collects all the Italy fuel prices data from the official [MIMIT](https://www.mimit.gov.it/it/prezzo-medio-carburanti) website, then provides them in a graph visible on [this webpage](https://marco97pa.github.io/italy_fuel_price_history/)  
# How does it work
## Scraping
The code is based on Python and uses simple libraries such as requests and BeautifulSoup to get data from the the official [MIMIT](https://www.mimit.gov.it/it/prezzo-medio-carburanti) website.
Data is then processed to get the averages of both gasoline and diesel prices of **self service** from all the fuel station in Italy.  
This processed data is then stored in [a CSV](https://github.com/marco97pa/italy_fuel_price_history/blob/main/average_prices.csv) file.
### Where and when it runs
It runs on a daily basis at 10 AM UTC when new data is for sure available on GitHub Actions.  
You can find the [running workflow here](https://github.com/marco97pa/italy_fuel_price_history/actions/workflows/fuel-prices.yml)
### Historical data
Data prior to the launch of this project has been mass imported from CSV archives of the above mentioned source and it's available on the CSV file.  
This data covers prices from 2020 to the first half of 2026. 
## Displaying the prices
The CSV data can be explored in a beautiful and simple way in a [single webpage](https://marco97pa.github.io/italy_fuel_price_history/) provided by GitHub Pages.
You can easily switch between latest 30 days view to full range view since 2020.

# Contributing
Any help in improving this repo is appreciated: just fork it and propose your changes

# Use of the data
The collected data is free to use

# Why
Fuel prices are rising in the last years in Italy because of war, economic crisis, political choices and speculation.  
This tool provides a comprehensive view of the fuel prices of the self service over time.
