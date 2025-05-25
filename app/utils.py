import re


def is_meaningful(text: str) -> bool:
    return bool(text and text.strip() and any(c.isalpha() for c in text.split()))


def preprocess(text_data: str) -> str:
    text = text_data.replace('\n', ' ').replace('\t', ' ')
    text = text.lower()
    text = re.sub(r'[^а-яё\s]', '', text)
    text = " ".join(text.split())

    return text
