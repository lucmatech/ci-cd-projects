from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Aplicação Flask com CI/CD e testes unitários funcionando!"

if __name__ == "__main__":
    app.run(debug=True)
