import pandas as pd
from io import StringIO
import os
from datetime import datetime
from src.configuration.configuration import OUTPUT_CSV

def process_html_content_to_dataframe(html_content):

    html_file_like = StringIO(html_content)
    df = pd.read_html(html_file_like)[0]

    df['Bank'] = 'Nations Trust'
    df['Date'] = datetime.now().strftime('%Y-%m-%d') #todays date 
    df['Time'] = datetime.now().strftime('%H:%M:%S') #todays time
    df['ST BANK CODE'] = '7162'

    # file_path = os.path.join(OUTPUT_CSV)
    # df.to_csv(file_path, index=False)
     
    return df