from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    expr = request.form.get("expression", "")
    try:
        result = eval(expr)
    except:
        result = "خطأ في المعادلة"
    return render_template("index.html", answer=result, expr=expr)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
