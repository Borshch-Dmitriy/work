from datetime import date

def get_min_max(dates):
    if len(dates) == 0:
        return ()
    max_date = max(dates)
    min_date = min(dates)
    return  min_date, max_date