from mesa import Agent
import config as config

class PatientAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = None

    def step(self):
        new_state = self.state
        if self.state == config.STATES['digiturno']:
            new_state = self.model.triage_agent.change_patient_state(self)
        self.state = new_state