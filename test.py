from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('question')
    # Traitement de la question et génération de réponse
    response = f"Voici la réponse à votre question : {question}"
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
