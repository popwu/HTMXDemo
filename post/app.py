from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# 首页
@app.route("/")
def index():
    return render_template("index.html")


# 表单提交的 POST 路由
@app.route("/submit", methods=["POST"])
def submit_form():
    username = request.form.get("username")

    if not username or len(username) < 3:
        return jsonify({"error": "用户名必须至少包含3个字符"}), 400

    return render_template("success_page.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
