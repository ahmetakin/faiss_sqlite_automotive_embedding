from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent #ana path tanımladık

DATA_DIR = BASE_DIR / "data" #veriler yükleyeceğimiz
IMAGE_DIR = DATA_DIR / "images" #resimler yükleyeceğimiz
 
DB_PATH = DATA_DIR / "automotive.db" #oluşturulacak db ismi
RAW_DOCUMENTS_PATH = DATA_DIR / "raw_documents.json" #vectorize ediceğimiz örnek veriler

FAISS_INDEX_PATH = DATA_DIR / "automotive.faiss" #faiss index konumu
FAISS_META_PATH = DATA_DIR / "faiss_meta.json" #meta konumu faiss

MODEL_PATH = "/home/user/ahmet-ai/faiss_sqlite_automotive/model/Qwen3-VL-Embedding-2B" #kullanacağımız model path

TOP_K = 5
IMAGE_MAX_SIZE = 448 #maksimum resim boyutu 448x448 performans için