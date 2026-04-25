from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
IMAGE_DIR = DATA_DIR / "images"

DB_PATH = DATA_DIR / "automotive.db"
RAW_DOCUMENTS_PATH = DATA_DIR / "raw_documents.json"

FAISS_INDEX_PATH = DATA_DIR / "automotive.faiss"
FAISS_META_PATH = DATA_DIR / "faiss_meta.json"

MODEL_PATH = "/home/user/ahmet-ai/faiss_sqlite_automotive/model/Qwen3-VL-Embedding-2B"

TOP_K = 5
IMAGE_MAX_SIZE = 448