#!/usr/bin/env python3
# %%
from models.emergency import EmergencyModel
from agents.triage import TriageAgent
import matplotlib.pyplot as plt

triage_agent = TriageAgent()
emergency_model = EmergencyModel(
    n=10,
    triage_agent=triage_agent
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
print("DATOS DE LOS PACIENTES EN CADA PASO\n", patients_data)
