import os

# Agents
from agents.patient import PatientAgent
from agents.triage import TriageAgent
import create_patients

# Models
from models.emergency import EmergencyModel

# Config
import config

# Pandas
import pandas as pd

# Visualization
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

def agent_portrayal(agent):
    portrayal = {
        'Shape': 'circle',
        'Layer': 0,
        'r': 1,
        'Color': 'gray'}
        

    # (Un)masked agents show up as (non-)filled circles
    if agent.masked == True:
        portrayal['Filled'] = 'true'
    
    if agent.fase == 1:
        portrayal['Color'] = 'lightblue'
    
    if agent.fase == 2:
        portrayal['Color'] = 'green'
    
    if agent.fase == 3:
        portrayal['Color'] = 'red'
    
    if agent.fase == 8:
        portrayal['Color'] = 'white'

    # if agent.infected == True:
    #     portrayal['Color'] = 'red'

    # if agent.immune == True:
    #     portrayal['Color'] = 'green'

    return portrayal


if __name__ == '__main__':
    # Definen la carpeta raíz del proyecto
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Get patients by step
    patients_by_step = create_patients.get_patients_by_step(steps_by_hour=6)
    num_paciente_diarios = sum(patients_by_step)

    edad_pacientes = create_patients.get_edad_pacientes(
        config.SIMULATION_PARAMETERS, num_paciente_diarios)
    convenios_pacientes = create_patients.get_convenio_pacientes(
        config.SIMULATION_PARAMETERS, num_paciente_diarios)

    model_params = {
        'patients_by_step': patients_by_step,
        'edad_pacientes': edad_pacientes,
        'convenios_pacientes': convenios_pacientes,
        'width': 49,
        'height': sum(patients_by_step),
        'tiempo_promedio_consulta': UserSettableParameter(
            'slider', 'Tiempo de consulta', 2, 5, 20, 5),
        
    }

    # grid = CanvasGrid(agent_portrayal, 50, 50, 500, 500)
    grid = CanvasGrid(agent_portrayal, 49, sum(patients_by_step), 800, 2000)

    line_charts = ChartModule([
        {'Label': 'Triage', 'Color': 'green'}, 
        {'Label': 'Infected', 'Color': 'red'},
        {'Label': 'Recovered & Immune', 'Color': 'green'}])

    server = ModularServer(EmergencyModel, [grid, line_charts], 
                            'EMERGENCIAS Fundación Santa Fé', model_params)

    server.port = 8521  # default port if unspecified
    server.launch()


    # # Create emergency model
    # emergency_model = EmergencyModel(
    #     patients_by_step=patients_by_step,
    #     edad_pacientes=edad_pacientes,
    #     convenios_pacientes=convenios_pacientes
    # )

    # counter = 0
    # for step, num_patients in enumerate(patients_by_step):
    #     # print('-------PASO-------', step)
    #     # print('---patients---', num_patients)
    #     emergency_model.step()
    #     # counter += 1
    #     # if counter == 20:
    #     #     break
    #     # print(emergency_model.schedule.steps)
    # data = emergency_model.datacollector.get_agent_vars_dataframe()
    # data.to_csv('data.csv')

    # for i in range(10):
    #     edad = list()
    #     for a in emergency_model.schedule.agents:
    #         edad.append(a.edad)
    #     print(pd.Series(edad).value_counts()/len(edad))
    #     print('')

    # for step, num_patients in enumerate(patients_by_step):
    #     print('Step:', step)
    #     print('Pacientes:', num_patients)
    #     print()

    # emergency_model = EmergencyModel(
    #     n=10,
    #     triage_agent=triage_agent
    # )

    # # Test con un solo paso
    # emergency_model.step()
    # for p in emergency_model.schedule.agents:
    #     print(p.fase)

    # # # Test con un múltiples pasos
    # for s in range(8):
    #      emergency_model.step()
