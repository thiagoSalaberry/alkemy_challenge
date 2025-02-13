from transforms.index import normalized_df, combined_df, df_cines_alone
from sqlalchemy import create_engine
from connections import DB_URL

engine = create_engine(DB_URL)

normalized_df.to_sql("normalized", con=engine,
                     if_exists="replace", index=False)
print("El proceso terminó")
