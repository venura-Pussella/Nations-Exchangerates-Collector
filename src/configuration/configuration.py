import os

# CSV data saving path
url = "https://www.nationstrust.com/foreign-exchange-rates"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.5; rv:127.0) Gecko/20100101 Firefox/127.0"

OUTPUT_CSV = os.path.join("data", "csv", "Nation_Trust_Bank_Exchange_Rates.csv")
Basefile_name="Nation_Trust_Bank_Exchange_Rates"

# SQL connection string
# CONNECTION_STRING = 'mssql://BGL-DTS33\\MSSQLSERVER1/mydb?driver=ODBC+DRIVER+17+FOR+SQL+SERVER'
# Commercial bank exchange rate url