import config

class TriageAgent(object):
    
    def __init__(self):
        self.max_enfermeros = 1
        self.enfermeros_disponibles = 1

    def cambiar_fase_paciente(self, paciente):
        # TODO: Acá va la función de que devuelve el estato a partir de las variables
        # del agente.
        nueva_fase = paciente.fase
        if self.available_staff > 0:
            nueva_fase = config.FASES['triage']
        return nueva_fase

    