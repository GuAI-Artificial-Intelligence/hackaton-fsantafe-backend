import config
import random

class ConsultaAgent(object):
    def __init__(self):
        self.max_medicos = 3
        self.medicos_disponibles = 3

        # def cambiar_fase_paciente(self, paciente):
        #     if self.available_staff > 0:
        #         nueva_fase = config.FASES['consulta']
        #     return nueva_fase

        # def atencion(self, paciente):
        #     # TODO: Acá va la función de que devuelve el estato a partir de las variables
        #     # del agente.
        #     nueva_fase = paciente.fase
        #     triage = None
        #     if self.enfermeros_disponibles > 0:
        #         nueva_fase = config.FASES['triage']
        #         self.enfermeros_disponibles -= 1
        #         r = random.random()
        #         if r>=0 and r<=0.000545:
        #             triage = 1
        #         if r>0.000545 and r<=0.056419:
        #             triage = 2
        #         if r>0.056419 and r<=0.434587:
        #             triage = 3
        #         if r>0.434587 and r<=0.9364950000000001:
        #             triage = 4
        #         if r>0.9364950000000001 and r<=1.0:
        #             triage = 5

        # return nueva_fase, triage