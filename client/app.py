from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

# URL de l'API FastAPI
API_URL = "http://127.0.0.1:8000"

# Route pour la page de liste des montres
@app.route('/')
def index():
    # Récupérer les montres en vente depuis l'API
    response = requests.get(f"{API_URL}/watches")
    watches = response.json() if response.status_code == 200 else []
    return render_template('index.html', watches=watches)

# Route pour la page de détails d'une montre
@app.route('/watch/<int:watch_id>')
def watch_detail(watch_id):
    # Récupérer les détails d'une montre spécifique depuis l'API
    response = requests.get(f"{API_URL}/watches/{watch_id}")
    if response.status_code == 200:
        watch = response.json()
        return render_template('watch_detail.html', watch=watch)
    else:
        return f"Montre {watch_id} non trouvée", 404

if __name__ == '__main__':
    app.run(debug=True)
