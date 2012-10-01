import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from sqlalchemy import create_engine

from m2tool.conf import M2_DB_ENV, M2_DEFAULT_DB_PATH

engine = create_engine("sqlite+pysqlite:///{0}".format(os.environ.get(M2_DB_ENV, M2_DEFAULT_DB_PATH)))
Metadata = MetaData(bind=engine)
Model = declarative_base(metadata=Metadata)
Session = sessionmaker(bind=engine)

