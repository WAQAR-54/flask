from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# ========================
# DATABASE CONFIG (MySQL)
# ========================
# Format:
# mysql+pymysql://USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/flask_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



# ============================
# DATABASE MODEL
# ============================
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


# ============================
# ROUTES
# ============================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/users")
def show_users():
    # yahan sirf READ ho raha hai
    users = User.query.all()
    return render_template("users.html", users=users)



# @app.route("/create-test-user")
# def create_test_user():
#     user = User(name="Ali Ahmed", email="ali@example.com")
#     db.session.add(user)
#     db.session.commit()
#     return "Test user created!"


# @app.route("/users")
# def list_users():
#     users = User.query.all()
#     return "<br>".join([f"{u.id} - {u.name} ({u.email})" for u in users])


# ============================
# CREATE TABLES & RUN APP
# ============================


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # agar table pehle se hai to kuch nahi karega, warna bana dega
    app.run(debug=True)

    
if __name__ == "__main__":
    app.run(debug=True)

