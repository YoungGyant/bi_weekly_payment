from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    total_hours = 0
    total_pay = 0
    if request.method == 'POST':
        week1_hours = float(request.form.get('week1_hours', 0))
        week2_hours = float(request.form.get('week2_hours', 0))
        hourly_rate = float(request.form.get('hourly_rate', 0))
        overtime_rate = hourly_rate * 1.5
        hourly_MAX = 80

        total_hours = week1_hours + week2_hours
        if total_hours > hourly_MAX:
            overtime_hours = total_hours - hourly_MAX
            regular_hours = hourly_MAX
            total_pay = (regular_hours * hourly_rate) + (overtime_hours * overtime_rate)
        else:
            total_pay = total_hours * hourly_rate

    return render_template('index.html', total_hours=total_hours, total_pay=total_pay)