from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# モデル定義
class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50))

# ✅ Flask 3.x対応: 直接テーブル作成を呼び出す
with app.app_context():
    db.create_all()

# 予定一覧ページ
@app.route('/')
def index():
    schedules = Schedule.query.all()
    return render_template('index.html', schedules=schedules)

# 予定追加
@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    date = request.form['date']
    new_schedule = Schedule(title=title, date=date)
    db.session.add(new_schedule)
    db.session.commit()
    return redirect(url_for('index'))

# 予定削除
@app.route('/delete/<int:id>')
def delete(id):
    s = Schedule.query.get(id)
    db.session.delete(s)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
