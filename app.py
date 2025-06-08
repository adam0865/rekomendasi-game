from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Ganti dengan API key Gemini kamu
genai.configure(api_key="AIzaSyDk2L0RkKFDkuge3WizL6olilUsjWG8_UM")

model = genai.GenerativeModel("gemini-2.0-flash")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt kosong."})

    try:
        response = model.generate_content(prompt)
        return jsonify({"recommendation": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
