import pandas as pd
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    # Create a simple DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    return f"Hello, World! DataFrame shape: {df.shape}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
