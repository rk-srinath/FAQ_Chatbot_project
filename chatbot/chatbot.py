from .data_loader import load_faqs, generate_embeddings
from .preprocess import preprocess_text
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

faqs = load_faqs()
embeddings = generate_embeddings(faqs)

def get_response(user_input):
    user_input = preprocess_text(user_input)
    
    from chatbot.data_loader import model
    user_embedding = model.encode([user_input])
    
    similarities = cosine_similarity(user_embedding, embeddings)
    best_match_index = np.argmax(similarities)

    if similarities[0][best_match_index] > 0.6:
        return faqs[best_match_index]["answer"]
    else:
        return "Sorry, I didn’t understand that. Could you rephrase it?"
