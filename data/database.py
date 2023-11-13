from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Apuntador a la base de datos
database_file = "data/bdHCE"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{database_file}"

# Crear engine de SQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear sesión de SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
