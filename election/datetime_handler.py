from datetime import date, datetime, timedelta
import pytz

WIBTimezone = pytz.timezone('Asia/Jakarta')

# Change this in accordance with time to vote and show result
TIME_FOR__SURPRISE_BRIEFING = 5

ELECTION_YEAR = 2021
ELECTION_MONTH = 7
ELECTION_DAY = 9
ELECTION_TIME = WIBTimezone.localize(datetime(ELECTION_YEAR, ELECTION_MONTH, ELECTION_DAY, hour=15, minute=41))

RESULT_YEAR = 2021
RESULT_MONTH = 7
RESULT_DAY = 9
RESULT_TIME = WIBTimezone.localize(datetime(RESULT_YEAR, RESULT_MONTH, RESULT_DAY, hour=17, minute=6))

def result_available(aboveSixtySixPercentage = False) -> bool:
    now = datetime.now(WIBTimezone)
    if(aboveSixtySixPercentage):
        return now > RESULT_TIME + timedelta(minutes = TIME_FOR__SURPRISE_BRIEFING)
    return now > RESULT_TIME

def get_current_time() -> datetime:
    return datetime.now(WIBTimezone)

def get_election_time() -> datetime:
    return ELECTION_TIME

def get_result_time() -> datetime:
    return RESULT_TIME

def can_vote() -> bool:
    return (get_current_time() > ELECTION_TIME and get_current_time() < RESULT_TIME)