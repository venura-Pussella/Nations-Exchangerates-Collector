import uuid
def convert_df_to_cosmos_db_format(df):
    
    cosmos_db_documents = []
    for _, row in df.iterrows():
        rate_document = {
            "id": str(uuid.uuid4()),
            "timestamp": f"{row['Date']}T{row['Time']}Z",
            "code": row['Currency Code'],
            "currency": str(row['Currency']) if row['Currency'] else None,
            "dd_buying": float(row['DD Buying Rate']) if row['DD Buying Rate'] else None,
            "mid_rates": float(row['Mid Rates']) if row['Mid Rates'] else None,
            "dd_selling": float(row['DD Selling Rate']) if row['DD Selling Rate'] else None,
            # "telegraphic_buying_rate": float(row['Telegraphic Buying Rate']) if row['Telegraphic Buying Rate'] else None,
            # "telegraphic_selling_rate": float(row['Telegraphic Selling Rate']) if row['Telegraphic Selling Rate'] else None,
            "bank": row['Bank'],
            "st_bank_code": row['ST BANK CODE']
        }
        cosmos_db_documents.append(rate_document)
    
    return cosmos_db_documents