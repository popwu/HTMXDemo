import json
from flask import Flask, render_template, jsonify, request
import math

app = Flask(__name__)


# 读取 JSON 数据
def load_data():
    with open("data.json", "r") as f:
        return json.load(f)


@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 10  # 每页显示10条数据

    data = load_data()
    total_items = len(data)
    total_pages = math.ceil(total_items / per_page)

    start = (page - 1) * per_page
    end = start + per_page

    paged_data = data[start:end]
    return render_template("index.html", data=paged_data, page=page, per_page=per_page, total_pages=total_pages)


if __name__ == "__main__":
    app.run(debug=True)
