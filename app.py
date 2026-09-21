from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("query")
    
    # Demo: código potencialmente inseguro
    result = query

    return str(result)

if __name__ == "__main__":
    app.run()
