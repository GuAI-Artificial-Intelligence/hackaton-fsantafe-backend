#!/usr/bin/env python3
# %%
import matplotlib.pyplot as plt
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

# Get patients by step
patients_by_step = create_patients.get_patients_by_step(steps_by_hour=6)
num_paciente_diarios = sum(patients_by_step)

print('Patientes by step:', patients_by_step)

edad_pacientes = create_patients.get_edad_pacientes(
    config.SIMULATION_PARAMETERS, num_paciente_diarios)
convenios_pacientes = create_patients.get_convenio_pacientes(
    config.SIMULATION_PARAMETERS, num_paciente_diarios)

# Creation of agents
triage_agent = TriageAgent()

# Create emergency model
emergency_model = EmergencyModel(
    patients_by_step=patients_by_step,
    triage_agent=triage_agent,
    edad_pacientes=edad_pacientes,
    convenios_pacientes=convenios_pacientes
)


emergency_patients = emergency_model.datacollector.get_model_vars_dataframe()
print(emergency_patients.head(11))
#emergency_patients.plot()

patients_data = emergency_model.datacollector.get_agent_vars_dataframe()
print(patients_data.head(11))
# %%
for i in range(6):
    emergency_model.step()
# %%
emergency_patients = emergency_model.datacollector.get_model_vars_dataframe()
print("DATOS DEL MODELO EMERGENCIAS\n",emergency_patients)
# %%
patients_data = emergency_model.datacollector.get_agent_vars_dataframe()
print("DATOS DE LOS PACIENTES EN CADA PASO\n", patients_data.head(10))
