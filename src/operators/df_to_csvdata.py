import io
import csv

def write_exchange_rates_to_csv_data(exchange_rates_df):
    
    # Create an in-memory string buffer
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)

    # Write the header with the new 'Date', 'Time', and 'Bank' columns
    writer.writerow([
        "Currency Code", 
        "Currency", 
        "DD Buying Rate", 
        "Mid Rates", 
        "DD Selling Rate", 
        "Bank", 
        "Date", 
        "Time",
        "ST BANK CODE",
    ])

    # Write the data rows
    for index, row in exchange_rates_df.iterrows():
        writer.writerow(row)

    # Get the CSV data as a string
    csv_data = csv_buffer.getvalue()
    csv_buffer.close()
    
    return csv_data
