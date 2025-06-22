with open('commercial_irac.py', 'w') as f:
    f.write('''\
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import PyPDF2
from google.colab import files
from docx import Document
import re
import pickle
import os
from google.colab import drive

class IRACDatabase:
    def __init__(self):
        self.db_file = "irac_style_db.pkl"
        self.examples_file = "irac_training_examples.txt"
        self.init_storage()

    # [PASTE ALL YOUR ORIGINAL CLASS METHODS HERE]
    # Keep identical indentation and content

class CommercialIRACGenerator:
    def __init__(self):
        self.trainer = IRACDatabase()
        self.model = pipeline(
            "summarization", 
            model="facebook/bart-large-cnn",
            device=0
        )
        # [PASTE ALL YOUR ORIGINAL CLASS METHODS HERE]

def commercial_irac_workflow():
    # [PASTE YOUR COMPLETE WORKFLOW FUNCTION HERE]
    # Maintain exact original formatting

if __name__ == "__main__":
    commercial_irac_workflow()
''')