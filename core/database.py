import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# On Vercel, the filesystem is read-only except for /tmp.
# Use /tmp for serverless deployments, local file for dev.
if os.environ.get("VERCEL"):
    DB_PATH = "/tmp/stvraf.db"
else:
    DB_PATH = "./stvraf.db"

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
