def study_schedule(permanence_period, target_time):
    if len(permanence_period) == 0 or target_time is None or target_time < 0:
        return None

    for period in permanence_period:
        if period[0] > period[1]:
            return None

    present_students = set()
    for period in permanence_period:
        if period[0] <= target_time <= period[1]:
            present_students.add(period[0])

            return len(present_students)
