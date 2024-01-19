# import modules for flask project
from flask import Flask, render_template
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ['ALPHA_API_KEY']

if API_KEY:
    print(f'API Key: {API_KEY}')
else:
    print("key not found")
