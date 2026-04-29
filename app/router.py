import re


PRODUCT_CODE_PATTERN = re.compile(r"\b[A-Z0-9]+(?:-[A-Z0-9]+)+\b")


IMAGE_WORDS = [
    "görsel",
    "resim",
    "fotoğraf",
    "foto",
    "image",
    "picture",
    "ürün resmi",
    "parça görseli"
]


def extract_product_codes(query: str):
    return PRODUCT_CODE_PATTERN.findall(query.upper())


def is_image_request(query: str) -> bool:
    q = query.lower()
    return any(word in q for word in IMAGE_WORDS)


def detect_query_intent(query: str):
    product_codes = extract_product_codes(query)

    if product_codes:
        return {
            "intent": "product_code",
            "product_codes": product_codes,
            "only_images": is_image_request(query)
        }

    if is_image_request(query):
        return {
            "intent": "image_search",
            "product_codes": [],
            "only_images": True
        }

    return {
        "intent": "semantic_search",
        "product_codes": [],
        "only_images": False
    }