import re


PRODUCT_CODE_PATTERN = re.compile(r"\b[A-Z0-9]+(?:-[A-Z0-9]+)+\b")


IMAGE_WORDS = [
    "görsel", "resim", "fotoğraf", "foto",
    "image", "picture", "ürün resmi", "parça görseli"
]

KNOWN_BRANDS = [
    "BOSCH",
    "POWERLINE",
    "EVER START",
    "TOTAL",
    "SHELL",
    "CASTROL",
    "SBS",
    "OSIMCO",
    "BREMBO",
    "PERFORMENCE PLUS",
    "PERFORMANCE PLUS"
]

RECOMMENDATION_WORDS = [
    "en iyi",
    "hangisi daha iyi",
    "daha iyi",
    "öner",
    "oner",
    "tavsiye",
    "karşılaştır",
    "karsilastir",
    "fiyat performans",
    "kaliteli",
    "tercih edilmeli",
    "en ucuz",
    "ucuz",
    "en pahalı",
    "pahalı",
    "fiyatı düşük",
    "fiyati dusuk"
]

PART_KEYWORDS = {
    "battery": ["akü", "aku", "batarya", "battery"],
    "brake_system": ["fren", "balata", "brake", "pad"],
    "engine_system": ["motor yağı", "motor yagi", "yağ", "yag", "oil", "engine oil"]
}

STRICT_FAMILY_RULES = {
    "battery": {
        "keywords": ["akü", "aku", "batarya", "battery"],
        "include_product_prefixes": ["BAT-12V"],
        "exclude_product_prefixes": ["ACC-BATT"],
        "exclude_words": ["şarj cihazı", "charger", "takviye"]
    },
    "brake_pad": {
        "keywords": ["fren balatası", "fren balata", "balata"],
        "include_product_prefixes": ["BRK-PAD"],
        "exclude_product_prefixes": ["BRAKE-DISC", "CLUTCH"],
        "exclude_words": ["disk", "debriyaj", "baskı balata"]
    },
    "engine_oil": {
        "keywords": ["motor yağı", "motor yagi", "yağ", "yag", "engine oil"],
        "include_product_prefixes": ["ENGINE-OIL"],
        "exclude_words": ["şanzıman", "transmission"]
    }
}


def detect_strict_family(query: str):
    q = query.lower()

    for family, rule in STRICT_FAMILY_RULES.items():
        for kw in rule["keywords"]:
            if kw in q:
                return family

    return None


def is_recommendation_request(query: str) -> bool:
    q = query.lower()
    return any(word in q for word in RECOMMENDATION_WORDS)

    
def extract_product_codes(query: str):
    return PRODUCT_CODE_PATTERN.findall(query.upper())


def is_image_request(query: str) -> bool:
    q = query.lower()
    return any(word in q for word in IMAGE_WORDS)


def extract_brand(query: str):
    q = query.upper()
    for brand in KNOWN_BRANDS:
        if brand in q:
            if brand == "PERFORMANCE PLUS":
                return "PERFORMENCE PLUS"
            return brand
    return None


def extract_part_keywords(query: str):
    q = query.lower()
    matched = []

    for _, keywords in PART_KEYWORDS.items():
        for kw in keywords:
            if kw in q:
                matched.extend(keywords)
                break

    return list(set(matched))


def clean_query_terms(query: str):
    q = query.lower()

    remove_words = [
        "görselini", "görsel", "resmini", "resim",
        "fotoğrafını", "fotoğraf", "foto",
        "getir", "göster", "bul", "ürün", "kodlu", "parça"
    ]

    for word in remove_words:
        q = q.replace(word, " ")

    terms = [x.strip() for x in q.split() if len(x.strip()) >= 2]
    return terms


def detect_query_intent(query: str):
    product_codes = extract_product_codes(query)
    brand = extract_brand(query)
    part_keywords = extract_part_keywords(query)
    only_images = is_image_request(query)
    query_terms = clean_query_terms(query)
    strict_family = detect_strict_family(query)

    if product_codes:
        intent = "product_code"
    elif only_images:
        intent = "image_search"
    elif is_recommendation_request(query):
        intent = "recommendation"
    else:
        intent = "semantic_search"

    return {
        "intent": intent,
        "product_codes": product_codes,
        "only_images": only_images,
        "brand": brand,
        "part_keywords": part_keywords,
        "query_terms": query_terms,
        "strict_family": strict_family        
    }