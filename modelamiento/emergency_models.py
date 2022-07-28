import mesa
from mesa import Agent, Model


STATES = {
    'sin_ingresar': None,
    'digiturno': 1,
    'triage': 2,
    'consulta': 3
    # TODO: adicionar más
}

STEPS_BY_HOUR = 6
QUANTITY_OF_STEPS = STEPS_BY_HOUR*24



class PatientAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = None

    def step(self):
        new_state = self.state
        if self.state == STATES['digiturno']:
            new_state = self.model.triage_agent.change_patient_state(self)
        self.state = new_state



class PatientModel(Model):
    
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
    


class TriageAgent(object):
    
    def __init__(self):
        self.max_staff = 2
        self.available_staff = 2

    def change_patient_state(self, agent):
        # TODO: Acá va la función de que devuelve el estato a partir de las variables
        # del agente.
        if self.available_staff > 0:
            new_state = STATES['triage']
        return new_state


class ConsultaAgent(object):
    
    def __init__(self):
        self.max_staff = 2
        self.available_staff = 2
    
    def change_patient_state(self, agent):
        pass



# ------ Simulación ------#

triage_agent = TriageAgent()
patient_model = PatientModel(
    n=10, 
    triage_agent=triage_agent
)

# Test con un solo paso
patient_model.step()
for p in patient_model.schedule.agents:
    print(p.state)

# # Test con un múltiples pasos
# for s in range(QUANTITY_OF_STEPS):
#     patient_model.step()