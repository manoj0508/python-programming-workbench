from pathlib import Path


def get_openai_api_key():
    key_path = Path(__file__).resolve().parent.parent / "openapiKey.txt"
    return key_path.read_text(encoding="utf-8").strip()