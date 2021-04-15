from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/prime/<int:n>")
def prime(n):

    if n == 2:
        res = {
            "Number": n,
            "num_st": True
        }

        return jsonify(res)
    if n < 1:
        res = {
            "Number": n,
            "num_st": False
        }

    for i in range (2,n):
        if n%i == 0:
            res = {
                "Number": n,
                "num_st": False
            }
            break
    else:
        res = {
            "Number": n,
            "num_st": True
        }
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)