FASES = {
    'sin_ingresar': None,
    'digiturno': 1,
    'triage': 2,
    'consulta': 3,
    'observacion': 4,
    'hospitalizacion': 5,
    'alta' : 6,
    'traslado': 7
}

STEPS_BY_HOUR = 6
QUANTITY_OF_STEPS = STEPS_BY_HOUR*8

TOTAL_SIMULATION_HOURS = 24
STEPS_BY_HOUR = 6

SIMULATION_PARAMETERS = {
    'edad': {
        (20, 30): 0.1,
        (31, 40): 0.3,
        (41, 50): 0.2,
        (51, 60): 0.4,
        (90, 120): 0
    },
    'convenio': {
        1: 0.8,
        0: 0.2
    },
    'pacientes_por_hora': [29, 34, 35, 31, 35, 31, 12, 20, 30, 31, 12, 17, 24, 33, 22, 26, 18, 11, 12, 18, 27, 35, 23, 26]

}

