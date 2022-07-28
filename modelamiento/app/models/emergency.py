import mesa
from mesa import Model
from agents.patient import PatientAgent

class EmergencyModel(Model):
    
    def __init__(
        self,
        n,
        triage_agent):

        # Creación de agentes pacientes
        self.num_agents = n
        self.schedule = mesa.time.BaseScheduler(self)
        for i in range(self.num_agents):
            a = PatientAgent(i, self)
            self.schedule.add(a)
        
        # Creación de agentes que cambian el estado del paciente
        self.triage_agent = triage_agent

    def step(self):
        self.schedule.step()