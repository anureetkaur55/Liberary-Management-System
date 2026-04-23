import datetime

books = {}

def calculate_fine(issue_date, allowed_days):
    today = datetime.date.today()
    days_passed = (today - issue_date).days

    if days_passed <= allowed_days:
        return 0

    extra_days = days_passed - allowed_days
    fine = 0

    for day in range(1, extra_days + 1):
        week = (day - 1) // 7 + 1
        fine += 10 * week

    return fine