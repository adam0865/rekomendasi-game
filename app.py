from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
import markdown

# Ganti dengan API Key Gemini kamu
genai.configure(api_key="AIzaSyDk2L0RkKFDkuge3WizL6olilUsjWG8_UM")

app = Flask(__name__)
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit', methods=['GET', 'POST'])  # Tambahkan POST jika ingin terima POST
def submit():
    if request.method == 'POST':
        # proses form
        pass


@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()
        device = data.get("device", "")
        genre = data.get("genre", "")
        mood = data.get("mood", "")

        prompt = (
            f"Saya sedang mencari game dengan genre {genre}, untuk perangkat {device}, "
            f"dan saya ingin game dengan suasana {mood}. "
            f"Tolong rekomendasikan beberapa game terbaik yang cocok dengan kriteria saya, "
            f"dalam bentuk poin-poin. Selalu mulai dengan 'Halo Sobat GameHunter!'"
        )

        response = model.generate_content(prompt)
        reply_raw = response.text
        reply_html = markdown.markdown(reply_raw)

        return jsonify({"reply": reply_html})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
