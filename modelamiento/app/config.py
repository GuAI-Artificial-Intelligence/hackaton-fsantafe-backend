FASES = {
    'sin_ingresar': None,
    'digiturno': 1,
    'triage': 2,
    'consulta': 3,
    'observacion': 4,
    'hospitalizacion': 5,
    'alta': 6,
    'traslado': 7
}

STEPS_BY_HOUR = 6

QUANTITY_OF_STEPS = STEPS_BY_HOUR*8

TOTAL_SIMULATION_HOURS = 24

SIMULATION_PARAMETERS = {
    'edad': {
        (0, 5):     0.129463,
        (5, 10):     0.047152,
        (10, 15):    0.042110,
        (15, 20):    0.047152,
        (20, 25):    0.078768,
        (25, 30):    0.088171,
        (30, 35):    0.088716,
        (35, 40):    0.085309,
        (40, 45):    0.060780,
        (45, 50):    0.046743,
        (50, 55):    0.045653,
        (55, 60):    0.047288,
        (60, 65):    0.043336,
        (65, 70):    0.045108,
        (70, 75):    0.033524,
        (75, 80):    0.028209,
        (80, 120):    0.042519
    },
    'convenio': {
        1: 0.8, 0: 0.2
    },
    'pacientes_por_hora': [
        4.0, 3.0, 2.0, 2.0, 3.0, 3.0, 6.0, 10.0, 15.0, 19.0, 20.0, 23.0, 21.0, 17.0, 18.0, 17.0, 17.0, 16.0, 15.0, 14.0, 12.0, 10.0, 8.0, 7.0
    ]
}

# SIMULATION_PARAMETERS = {
#     'edad': {
#         (20, 30): 0.1,
#         (31, 40): 0.3,
#         (41, 50): 0.2,
#         (51, 60): 0.4,
#         (90, 120): 0
#     },
#     'convenio': {
#         1: 0.8,
#         0: 0.2
#     },
#     'pacientes_por_hora': [29, 34, 35, 31, 35, 31, 12, 20, 30, 31, 12, 17, 24, 33, 22, 26, 18, 11, 12, 18, 27, 35, 23, 26]

# }
