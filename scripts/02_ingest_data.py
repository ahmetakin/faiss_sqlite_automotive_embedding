from app.db import init_db
from app.ingest import ingest_all

if __name__ == "__main__":
    init_db()
    ingest_all()