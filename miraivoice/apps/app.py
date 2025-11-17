from flask import Flask
from apps.auth.views import auth
from apps.extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///miraivoice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret-key"

# SQLAlchemy をアプリに紐付け
db.init_app(app)

# Blueprint を登録
app.register_blueprint(auth, url_prefix='')

# DB 初期化（初回のみ）
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
