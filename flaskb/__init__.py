import os

from flask import Flask
# 導入 db.py
from . import db
# 導入 auth.py
from . import auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #一般程式開發倉儲不會存放 flaskb.sqlite, 或數位簽章
        # app.instance_path 目錄為 instance, 在 .gitignore 設定不上傳遠端倉儲
        #DATABASE=os.path.join(app.instance_path, 'flaskb.sqlite'),
        DATABASE=os.path.join('./flaskb/', 'flaskb.sqlite'),
    )
    # 起始資料庫
    db.init_app(app)
    # 註冊 auth.py 中的 bp
    app.register_blueprint(auth.bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return '開始寫 lab-booking 程式!'

    return app