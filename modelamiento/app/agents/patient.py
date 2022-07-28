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
        if (self.unique_id < self.model.pacientes_ingresados) and (self.fase == config.FASES['sin_ingresar']):
            self.fase = config.FASES['digiturno']
            print(self.unique_id)

        if self.fase == config.FASES['digiturno']:
            self.fase = self.model.triage_agent.cambiar_fase_paciente(self)
