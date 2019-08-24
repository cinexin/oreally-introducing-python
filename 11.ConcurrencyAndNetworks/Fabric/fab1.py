# We can run Python code locally from a fabric file directly without SSH...
def iso():
    from datetime import date
    print(date.today().isoformat())