from datetime import datetime, timedelta


def get_last_passed_minute_utc():
    current_minute = datetime.strptime(datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
    return current_minute - timedelta(minutes=1)


def build_timeframe(timeframe_end, duration_in_minutes=30):
    # builds a list of full minutes from start to end of timeframe
    timeframe_start = timeframe_end - timedelta(minutes=duration_in_minutes) + timedelta(minutes=1)
    timeframe = list()
    timeframe.append(timeframe_start)
    current_timeframe_index = timeframe_start
    while current_timeframe_index < timeframe_end:
        current_timeframe_index += timedelta(minutes=1)
        timeframe.append(current_timeframe_index)
    return timeframe

