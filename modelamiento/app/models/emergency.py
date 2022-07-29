import mesa
from mesa import Model
from mesa.space import MultiGrid

# Agents
from agents.patient import PatientAgent
from agents.triage import TriageAgent

# numpy
import numpy as np


class EmergencyModel(Model):
    
    def __init__(
        self,
        patients_by_step,
        edad_pacientes,
        convenios_pacientes,
        width,
        height,
        tiempo_promedio_consulta):

        self.grid = MultiGrid(width, height, False)
        self.schedule = mesa.time.BaseScheduler(self)
        self.running = True

        # Creación de agentes pacientes
        self.patients_by_step = patients_by_step
        self.pacientes_ingresados = 0
        self.num_patient_agents = sum(self.patients_by_step)
        for i in range(self.num_patient_agents):
            a = PatientAgent(
                unique_id=i, 
                model=self,
                edad=edad_pacientes[i],
                convenio=convenios_pacientes[i]
                )
            self.schedule.add(a)

            # Grafico
            self.grid.place_agent(a, (0, self.num_patient_agents-i-1))

        # Creación de agentes que cambian el estado del paciente
        self.triage_agent = TriageAgent(self)

        self.datacollector = mesa.DataCollector(
            model_reporters={"Pacientes": "num_agents"},
            agent_reporters={
                "Fase": "fase", "Edad": "edad", "Imagenes": "imagenes",
                "Examenes":"examenes", "Interconsulta":"interconsulta",
                "Convenio":"convenio","Diagnostico":"diagnostico", "Triage":"triage",
                "StepDigiturno": 'step_digiturno', "StepTriage": 'step_triage'
                }
        )
        


    def step(self):
        self.triage_agent.enfermeros_disponibles += 1
        self.pacientes_ingresados += self.patients_by_step[self.schedule.steps]
        self.schedule.step()
        self.datacollector.collect(self)

    @property
    def triage(self):
        agents = self.schedule.agents
        triage = [a.fase==2 for a in agents]
        return int(np.sum(triage))