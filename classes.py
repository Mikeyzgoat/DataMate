import numpy as np
import pandas as pd
from nltk.corpus import stopwords # to remove stopwords
from nltk.stem import PorterStemmer # stemming
from nltk.stem.wordnet import WordNetLemmatizer # lemmatization
from pydantic import BaseModel
from api import UploadFile
from sklearn.feature_extraction.text import TfidfVectorizer
import PyPDF2 as pdf

class FileHandler(BaseModel):
    file: UploadFile

class TextCleaner():
    pass

class PDFHandler():
    pass

class CSVHandler():
    pass

class WebDataHandler():
    # web scraper based on URL passed into form or from csv files
    pass