from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from apps.extensions import db
from apps.models import User
from werkzeug.security import check_password_hash
from flask import session

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder='static',
    static_url_path='/auth/static'
)

@auth.route("/")
def index():
    return render_template("auth/index.html")


# ----------------------------
# 新規登録（表示＋DB保存）
# ----------------------------
@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        print("POST 受信:", name, email, password)  

        # メールの重複確認
        existing = User.query.filter_by(email=email).first()
        print("既存ユーザー:", existing)
        if existing:
            flash("このメールアドレスはすでに登録されています。")
            return redirect(url_for("auth.signup"))

        # パスワードをハッシュ化して保存
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()
        print("ユーザー追加成功")

        # 登録完了画面にリダイレクト
        return redirect(url_for("auth.success"))

    # GET: 登録フォーム表示
    return render_template("auth/signup.html")


# ----------------------------
# 登録完了画面
# ----------------------------
@auth.route("/success")
def success():
    return render_template("auth/success.html")  # テンプレート名 success.html に注意


# ----------------------------
# ログイン画面（まだロジックなし）
# ----------------------------
@auth.route("/login")
def login():
    return render_template("auth/login.html")
