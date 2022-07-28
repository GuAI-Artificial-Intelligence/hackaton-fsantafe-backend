import config

class TriageAgent(object):
    
    def __init__(self):
        self.max_staff = 2
        self.available_staff = 2

    def change_patient_state(self, agent):
        # TODO: Acá va la función de que devuelve el estato a partir de las variables
        # del agente.
        if self.available_staff > 0:
            new_state = config.STATES['triage']
        return new_state

    