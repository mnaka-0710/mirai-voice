from apps.extensions import db
from apps.models import User
from apps.app import app  # Flask アプリ本体をインポート

with app.app_context():  # DB操作にはアプリコンテキストが必要
    user = User.query.filter_by(email="mro2423019@stu.o-hara.ac.jp").first()
    if user:
        db.session.delete(user)
        db.session.commit()
        print("ユーザーを削除しました")
    else:
        print("該当ユーザーは存在しません")
