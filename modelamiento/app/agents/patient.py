from mesa import Agent
import config as config


class PatientAgent(Agent):
    def __init__(
        self, unique_id, model,
        edad, convenio
                 ):
        super().__init__(unique_id, model)
        self.fase: str = config.FASES['sin_ingresar']
        self.edad: int = edad
        self.imagenes: bool = False
        self.examenes: bool = False
        self.interconsulta: bool = False
        self.convenio: str = convenio
        self.diagnostico: str = None

    def step(self):
        nueva_fase = self.fase
        if self.fase == config.FASES['digiturno']:
            nueva_fase = self.model.triage_agent.cambiar_fase_paciente(self)
        self.fase = nueva_fase
