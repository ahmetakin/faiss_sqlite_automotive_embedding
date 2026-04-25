import json
import sqlite3
from app.config import DB_PATH


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS items (
        vector_id INTEGER PRIMARY KEY,
        item_id TEXT NOT NULL,
        item_type TEXT NOT NULL,
        title TEXT NOT NULL,
        category TEXT,
        product_code TEXT,
        source TEXT,
        content TEXT,
        image_path TEXT,
        metadata_json TEXT
    )
    """)

    cur.execute("""
    CREATE INDEX IF NOT EXISTS idx_items_item_id
    ON items(item_id)
    """)

    cur.execute("""
    CREATE INDEX IF NOT EXISTS idx_items_category
    ON items(category)
    """)

    cur.execute("""
    CREATE INDEX IF NOT EXISTS idx_items_product_code
    ON items(product_code)
    """)

    conn.commit()
    conn.close()


def clear_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM items")
    conn.commit()
    conn.close()


def insert_item(
    vector_id: int,
    item_id: str,
    item_type: str,
    title: str,
    category: str,
    product_code: str,
    source: str,
    content: str,
    image_path: str | None,
    metadata: dict
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO items (
        vector_id,
        item_id,
        item_type,
        title,
        category,
        product_code,
        source,
        content,
        image_path,
        metadata_json
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        vector_id,
        item_id,
        item_type,
        title,
        category,
        product_code,
        source,
        content,
        image_path,
        json.dumps(metadata or {}, ensure_ascii=False)
    ))

    conn.commit()
    conn.close()


def fetch_item_by_vector_id(vector_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM items
    WHERE vector_id = ?
    """, (vector_id,))

    row = cur.fetchone()
    conn.close()

    if row is None:
        return None

    result = dict(row)
    result["metadata"] = json.loads(result.pop("metadata_json") or "{}")
    return result