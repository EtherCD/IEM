def calculate_normal(efficiency: float, consumption: float, time: float, volt: float):
    watt_hours = consumption * time
    ampers = watt_hours / volt
    procent_eff = ampers - (ampers / 100 * efficiency)
    normal_ampers = ampers + procent_eff
    return (round(watt_hours, 2), round(normal_ampers, 2), round(procent_eff, 2))


def calculate_time(efficiency: float, consumption: float, capacity: float, volt: float, remainder: float):
    ampers = consumption / volt
    procent_eff = ampers - (ampers / 100 * efficiency)
    normal_ampers = ampers + procent_eff
    procent_capacity = capacity - (capacity / 100 * remainder)
    normal_give_away = capacity - procent_capacity
    time_working = normal_give_away / normal_ampers
    hours = int(time_working)
    minutes = int((time_working - hours) * 60)
    if minutes < 0: minutes = 0
    return (hours, minutes, normal_give_away, round(normal_ampers, 2))

def time_recalculation(result: float):
    hours = round(result)
    minutes = int((result - hours) * 60)
    return hours + ( 0.1 * minutes )

def calculate_reverse(time: float, capacity: float, volt: float, remainder: float):
    watts = (capacity * volt * (1 - (remainder / 100))) / time_recalculation(time)
    return (round(watts, 2), 0)