import mesa
from mesa import Model
from agents.patient import PatientAgent

class EmergencyModel(Model):

    num_agents = 0

    def __init__(
        self,
        n,
        triage_agent):

        # Creación de agentes pacientes
        self.schedule = mesa.time.BaseScheduler(self)
        self.ingresar_pacientes_hora(n)

        # Creación de agentes que cambian el estado del paciente
        self.triage_agent = triage_agent
        self.datacollector = mesa.DataCollector(
            model_reporters={"Pacientes": "num_agents"},
            agent_reporters={"Fase": "fase", "Edad": "edad", "Imagenes": "imagenes",
                             "Examenes":"examenes", "Interconsulta":"interconsulta",
                             "Convenio":"convenio","Diagnostico":"diagnostico"}
        )
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

    def ingresar_pacientes_hora(self, n):
        """Metodo que crea una cantidad N de pacientes y los añade al modelo
        les asigna un id teniendo en cuenta los usuarios existentes"""
        prev_agents = self.num_agents
        self.num_agents += n
        for i in range(n):
            a = PatientAgent(
                unique_id=i+prev_agents,
                model=self,
                edad=30,
                convenio='SURA'
                )
            self.schedule.add(a)
