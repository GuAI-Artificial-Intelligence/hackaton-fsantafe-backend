import random
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
        self.triage: int = None
        self.unique_id = unique_id
        self.step_digiturno = None
        self.step_triage = None

        # test grafica
        self.masked = True

    def step(self):
        if self.fase != config.FASES['sin_ingresar']:
            self.move()

        

        if self.fase == config.FASES['triage']:
            ruido = random.choice([0, 1, 2, 3, 4, -1,-2,-3,-4])
            limit = (5 + ruido)
            if (self.model.schedule.steps - self.step_triage >= limit):
                self.fase = config.FASES['consulta']
            

        if self.fase == config.FASES['digiturno']:
            self.fase, self.triage, self.step_triage = self.model.triage_agent.atencion(self)
            if not (self.triage in [3, 4]):
                self.fase = config.FASES['fuera_de_estudio']

        if (self.unique_id < self.model.pacientes_ingresados) and (self.fase == config.FASES['sin_ingresar']):
            self.fase = config.FASES['digiturno']
            self.step_digiturno = self.model.schedule.steps

    def move(self):
        x,y = self.pos
        self.model.grid.move_agent(self, (x+1, y))

