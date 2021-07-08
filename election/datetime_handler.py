from datetime import date, datetime
import pytz

WIBTimezone = pytz.timezone('Asia/Jakarta')

# Change this in accordance with time to vote and show result
RESULT_YEAR = 2021
RESULT_MONTH = 7
RESULT_DAY = 10
RESULT_TIME = WIBTimezone.localize(datetime(RESULT_YEAR, RESULT_MONTH, RESULT_DAY, hour=22, minute=30))

ELECTION_YEAR = 2021
ELECTION_MONTH = 7
ELECTION_DAY = 7
ELECTION_DATE = WIBTimezone.localize(datetime(ELECTION_YEAR, ELECTION_MONTH, ELECTION_DAY))

def result_available() -> bool:
    now = datetime.now(WIBTimezone)
    return now > RESULT_TIME

def get_current_time() -> datetime:
    return datetime.now(WIBTimezone)

def get_election_date() -> datetime:
    return ELECTION_DATE

def get_result_time() -> datetime:
    return RESULT_TIME