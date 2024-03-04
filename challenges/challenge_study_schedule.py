def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0
    for period in permanence_period:
        start_time, end_time = period
        if (
            start_time is None
            or end_time is None
            or not isinstance(start_time, int)
            or not isinstance(end_time, int)
        ):
            return None

        if start_time <= target_time <= end_time:
            count += 1

    return count
