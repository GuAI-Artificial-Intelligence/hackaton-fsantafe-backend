import config
import random
from mesa import Agent

class TriageAgent(Agent):
    
    def __init__(self, model, unique_id=0):
        super().__init__(unique_id, model)
        self.max_enfermeros = 1
        self.enfermeros_disponibles = 1

    def atencion(self, paciente):
        # TODO: Acá va la función de que devuelve el estato a partir de las variables
        # del agente.
        nueva_fase = paciente.fase
        triage = paciente.triage
        step_triage = paciente.step_triage
        if self.enfermeros_disponibles > 0:
            nueva_fase = config.FASES['triage']
            step_triage = self.model.schedule.steps
            self.enfermeros_disponibles -= 1
            r = random.random()
            if r>=0 and r<=0.000545:
                triage = 1
            if r>0.000545 and r<=0.056419:
                triage = 2
            if r>0.056419 and r<=0.434587:
                triage = 3
            if r>0.434587 and r<=0.9364950000000001:
                triage = 4
            if r>0.9364950000000001 and r<=1.0:
                triage = 5

        return nueva_fase, triage, step_triage

    