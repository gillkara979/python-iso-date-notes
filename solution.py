from datetime import date

def solve(value):
    return (lambda d: {"year": d.year, "month": d.month, "day": d.day, "weekday": d.isoweekday()})(date.fromisoformat(value))
