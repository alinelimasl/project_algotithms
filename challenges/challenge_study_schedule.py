def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0
    for period in permanence_period:
        start_time, end_time = period
        if start_time is None or end_time is None:
            return None
        if not isinstance(start_time, int) or not isinstance(end_time, int):
            return None

    count = 0
    for period in permanence_period:
        start_time, end_time = period
        if start_time <= target_time <= end_time:
            count += 1

    return count


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_times = [5, 4, 3, 2, 1]

for target_time in target_times:
    print(
        f"target_time = {target_time}: saída: {study_schedule(permanence_period, target_time)}"
    )
