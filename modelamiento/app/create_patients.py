import random
import math
import config
import pandas as pd


# def get_patients_by_hour():
#     result = list()
#     for i in range(config.TOTAL_SIMULATION_HOURS):
#         result.append(random.randint(15, 30))
#     return result


def get_patients_by_step(steps_by_hour=6):
    patientes_by_hour = config.SIMULATION_PARAMETERS['pacientes_por_hora']
    patients_by_step = list()
    for p in patientes_by_hour:
        patients_step = math.ceil(p/steps_by_hour)
        patients_step = round(p/steps_by_hour)
        for s in range(steps_by_hour):
            patients_by_step.append(patients_step)
    return patients_by_step

def get_edad_pacientes(config, num_paciente_diarios):
    pacientes_con_edad_asignada = dict()
    for key, value in config['edad'].items():
        min_edad = key[0]
        max_edad = key[1]
        asignar_edad = True
        asignados = list()
        while asignar_edad:
            if len(pacientes_con_edad_asignada.keys()) >= num_paciente_diarios:
                asignar_edad=False
                break
            edad = random.randint(min_edad, max_edad)
            id_paciente = random.randint(0, num_paciente_diarios-1)
            if (id_paciente in pacientes_con_edad_asignada.keys()):
                continue
            if len(asignados) >= num_paciente_diarios*value:
                asignar_edad=False
                break
            pacientes_con_edad_asignada[id_paciente] = edad
            asignados.append(edad)
    return pacientes_con_edad_asignada

def get_convenio_pacientes(config, num_paciente_diarios):
    pacientes_con_convenio_asignado = dict()
    for key, value in config['convenio'].items():
        asignado_convenio = True
        asignados = list()
        while asignado_convenio:
            if len(pacientes_con_convenio_asignado.keys()) >= num_paciente_diarios:
                asignado_convenio=False
                break
            id_paciente = random.randint(0, num_paciente_diarios-1)
            if (id_paciente in pacientes_con_convenio_asignado.keys()):
                continue
            if len(asignados) >= num_paciente_diarios*value:
                asignado_convenio=False
                break
            pacientes_con_convenio_asignado[id_paciente] = bool(key)
            asignados.append(key)

    return pacientes_con_convenio_asignado


if __name__ == '__main__':
    l = list()
    for i in range(24):
        l.append(random.randint(10, 35))
    print(l)

    # config = {
    #     'edad': {
    #         (30, 40): 0.3,
    #         (41, 50): 0.2,
    #         (51, 60): 0.4,
    #         (90, 120): 0
    #     },
    #     'convenio': {
    #         1: 0.8,
    #         0: 0.2
    #     }
    # }
    # num_paciente_diarios = 283
    # edad_pacientes = get_edad_pacientes(config, num_paciente_diarios)
    # convenio_pacientes = get_convenio_pacientes(config, num_paciente_diarios)
    


    # patientes_by_step = get_patients_by_step(
    #     steps_by_hour=config.STEPS_BY_HOUR,
    # )
    # print(patientes_by_step)
    # print(len(patientes_by_step))

    # config = {
    #     'edad': {
    #         (30, 40): 0.3,
    #         (40, 50): 0.2
    #     }
    # }

    # numero_pacientes_diarios = 100

    # ids_pacientes = list(range(numero_pacientes_diarios))
    # pacientes_con_edad = list()

    # for key, value in config['edad'].items():
    #     min_edad = key[0]
    #     max_edad = key[1]
    #     asignar_edad = True
    #     pacientes_con_edad_asignada = dict()
    #     while asignar_edad:
    #         edad = random.randint(min_edad, max_edad)
    #         id_paciente = random.randint(0, numero_pacientes_diarios-1)
    #         if (id_paciente in pacientes_con_edad_asignada.keys()):
    #             continue
    #         if len(pacientes_con_edad_asignada) >= numero_pacientes_diarios*value:
    #             asignar_edad = False
    #             continue
    #         pacientes_con_edad_asignada[id_paciente] = edad
            
        
        
    



    