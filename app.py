from flask import Flask, jsonify
from supabase import create_client
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__)

# Obtener la URL y la clave de Supabase desde las variables de entorno
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Crear cliente de Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    data = supabase.table('usuarios').select('*').execute()
    return jsonify(data.data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
