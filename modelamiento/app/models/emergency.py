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
        tiempo_promedio_interconsulta,
        tiempo_promedio_examenes,
        tiempo_promedio_imagenes):

        # Grafico
        self.grid = MultiGrid(width, height, False)
        self.schedule = mesa.time.BaseScheduler(self)
        self.running = True
        self.num_pacientes_digiturno = 0
        self.num_pacientes_triage = 0
        self.num_pacientes_consulta = 0
        self.num_pacientes_observacion = 0

        self.num_pacientes_hospitalizacion = 0
        self.num_pacientes_alta = 0
        self.num_pacientes_traslado = 0

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
            model_reporters={
                "Pacientes": "num_patient_agents",
                'Digiturno': "num_pacientes_digiturno",
                'Triage': "num_pacientes_triage",
                'Consulta': "num_pacientes_consulta",
                'Observacion': "num_pacientes_observacion",
                'Hospitalizacion': "num_pacientes_hospitalizacion",
                # 'Alta': "num_pacientes_alta",
                'Trasla': "num_pacientes_traslado",
                },
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

        # Actulizar totales para graficas
        agents = self.schedule.agents
        pacientes_digiturno = [(a.fase==1) for a in agents]
        pacientes_triage = [(a.fase==2) for a in agents]
        pacientes_consulta = [(a.fase==3) for a in agents]
        pacientes_observacion = [(a.fase==4) for a in agents]

        pacientes_hospitalizacion = [(a.fase==5) for a in agents]
        pacientes_alta = [(a.fase==6) for a in agents]
        pacientes_traslado = [(a.fase==7) for a in agents]

        self.num_pacientes_digiturno = int(np.sum(pacientes_digiturno))
        self.num_pacientes_triage = int(np.sum(pacientes_triage))
        self.num_pacientes_consulta = int(np.sum(pacientes_consulta))
        self.num_pacientes_observacion = int(np.sum(pacientes_observacion))

        self.num_pacientes_hospitalizacion = int(np.sum(pacientes_hospitalizacion))
        self.num_pacientes_alta = int(np.sum(pacientes_alta))
        self.num_pacientes_traslado = int(np.sum(pacientes_traslado))

        self.datacollector.collect(self)

    @property
    def triage(self):
        agents = self.schedule.agents
        triage = [a.fase==2 for a in agents]
        return int(np.sum(triage))