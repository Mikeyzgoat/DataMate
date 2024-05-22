import numpy as np
import pandas as pd
import nltk
from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel

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
