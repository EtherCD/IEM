TRANSLATES = {
    "en": [
        {
            "title": "Working Time Calculator",
            "p": "Inverter running time calculation utility",
            "efficiency": "Inverter efficiency (%)",
            "consumption": "Load power (W)",
            "time": "Working time (h)",
            "capacity": "Battery capacity (Ah)",
            "volt": "Battery voltage (V)",
            "remainder": "Battery charge (%)",
            "default_result": "Click calculate!",
            "button": "Calculate",
"result": """
>> Result:
>>> Watt hours:
>>> Ampere consumption:
>>> Wasted ampere-hours:
>>> Required number of ampere-hours:
>>> Maximum running time:
>>> The battery will be able to power your system all the time.
>>> Not enough battery to power your system.
""".split("\n")
        },
        {
            "title": "Watts from Time Calculator",
            "p": "Load Watt Calculator",
            "time": "Working time (hour.minute)",
            "capacity": "Battery capacity (Ah)",
            "volt": "Battery voltage (V)",
            "remainder": "Battery charge consumed (%)",
            "default_result": "Click calculate!",
            "button": "Calculate",
"result": """
>> Result:
>>> Watt load:
""".split("\n")
        }
    ],
    "ru": [
        {
            "title": "Калькулятор рабочего времени",
            "p": "Утилита расчета времени работы инвертора",
            "efficiency": "КПД инвертора (%)",
            "consumption": "Мощность нагрузки (Вт)",
            "time": "Время работы (ч)",
            "capacity": "Емкость аккумулятора (Ач)",
            "volt": "Напряжение батареи (В)",
            "remainder": "Заряд батареи (%)",
            "default_result": "Нажмите рассчитать!",
            "button": "Рассчитать",
"result": """
>> Результат:
>>> Потребление Ампер:
>>> Потерянные ампер-часы:
>>> Требуемое количество ампер-часов:
>>> Максимальное время работы:
>>> Аккумулятор сможет постоянно питать вашу систему.
>>> Недостаточно батареи для питания вашей системы.
""".split("\n")
        },
        {
            "title": "Watts from Time Calculator",
            "p": "Load Watt Calculator"
        }
    ]
}


def get_replicas(lang="en"):
    return TRANSLATES[lang]
