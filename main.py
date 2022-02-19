
from flask import Flask
from app import views

app = Flask(__name__)

# Định nghĩa các url và các component tương ứng.

# Url: http://127.0.0.1:5000/base thì sẽ điều hướng giao diện về trang base.html
app.add_url_rule('/base','base',views.base)

# Url: http://127.0.0.1:5000/ hoặc http://127.0.0.1:5000/index thì sẽ điều hướng giao diện về trang views.html
app.add_url_rule('/', 'index', views.index)

# Url: http://127.0.0.1:5000/faceapp thì sẽ điều hướng giao diện về trang faceapp.html
app.add_url_rule('/faceapp', 'faceapp', views.faceapp)

# Url: http://127.0.0.1:5000/gender# thì sẽ trả ra kết quả trên trang faceapp.html
app.add_url_rule('/faceapp/gender', 'gender', views.gender, methods=['GET', 'POST'])

# root của project
if __name__ == "__main__":
    app.run(debug=True)
