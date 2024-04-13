from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# (1) 비동기 방식 - Starlette
# (2) 데이터 검증 - pydantic

# 동기용 데이터 베이스 설정 (pip install pymysql)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://ighan65:han00719()@oz-fastapi.cfl1xmdrg1qo.ap-northeast-2.rds.amazonaws.com/oz-fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)