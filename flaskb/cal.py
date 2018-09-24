from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
    , make_response
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskb.db import get_db
# 導入 flaskb 目錄下的 cal_endar.py
from flaskb import cal_endar 
import datetime

bp = Blueprint('cal', __name__, url_prefix='/cal')

@bp.route('/list')
def cal_list():
    td = datetime.date.today()
    month = request.args.get('month', default = td.month, type = int)
    year = request.args.get('year', default = td.year, type = int)
    # 利用 cal_endar.py 中的 Calendar 類別, 建立 cal 案例
    cal = cal_endar.Calendar()
    # 呼叫 cal 案例中的 test() 方法
    output = cal.draw_month(month, year)
    return render_template('cal/cal_list.html', output=output)