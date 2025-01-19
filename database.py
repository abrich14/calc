from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine(f"mysql+pymysql://admin:Arvind1991@database-1.clew6ck0y4xa.us-east-1.rds.amazonaws.com:3306/arvind", echo = True)
meta = MetaData()