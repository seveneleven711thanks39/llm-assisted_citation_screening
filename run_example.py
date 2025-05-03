# coding: utf-8

from data_loader import df 
from screening_text_generator import *
from gemini_integration import *


if __name__ == "__main__":
    print("Here we go!")
    append_question()
    runGemini()
