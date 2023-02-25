import os
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

POSTGRES_USER = os.environ.get('POSTGRES_USER', 'words')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'words')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '9876')
POSTGRES_DBNAME = os.environ.get('POSTGRES_DBNAME', 'words')

engine = create_engine(
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DBNAME}'
)

metadata = MetaData()

WordsDB = Table(
    'words', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('word', String),
    Column('length', Integer)
)

with engine.connect() as conn:
    metadata.create_all(engine)
