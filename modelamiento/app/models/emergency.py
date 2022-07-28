import mesa
from mesa import Model
from agents.patient import PatientAgent

class EmergencyModel(Model):

    def __init__(
        self,
        n,
        triage_agent):

        # Creación de agentes pacientes
        self.num_agents = n
        self.schedule = mesa.time.BaseScheduler(self)
        for i in range(self.num_agents):
            a = PatientAgent(
                unique_id=i,
                model=self,
                edad=30,
                convenio='SURA'
                )
            self.schedule.add(a)

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
