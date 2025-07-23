import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_faqs():
    with open("data/faqs.json", "r") as f:
        faqs = json.load(f)
    return faqs

def generate_embeddings(faqs):
    questions = [faq["question"] for faq in faqs]
    embeddings = model.encode(questions)
    return embeddings
