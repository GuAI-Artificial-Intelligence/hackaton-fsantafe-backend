import mesa
from mesa import Model
from agents.patient import PatientAgent

class EmergencyModel(Model):

    def __init__(
        self,
        patients_by_step,
        edad_pacientes,
        convenios_pacientes,
        triage_agent):

        # Creación de agentes pacientes
        self.patients_by_step = patients_by_step
        self.pacientes_ingresados = 0
        self.num_patient_agents = sum(self.patients_by_step)
        self.schedule = mesa.time.BaseScheduler(self)
        for i in range(self.num_patient_agents):
            a = PatientAgent(
                unique_id=i,
                model=self,
                edad=edad_pacientes[i],
                convenio=convenios_pacientes[i]
                )
            self.schedule.add(a)

        # Creación de agentes que cambian el estado del paciente
        self.triage_agent = triage_agent
        self.datacollector = mesa.DataCollector(
            model_reporters={"Pacientes totales": "num_patient_agents",
                             "Pacientes ingresados": "pacientes_ingresados"},
            agent_reporters={"Fase": "fase", "Edad": "edad",
                             "Imagenes": "imagenes", "Examenes":"examenes",
                             "Interconsulta":"interconsulta",
                             "Convenio":"convenio","Diagnostico":"diagnostico"}
        )
        self.datacollector.collect(self)

    def step(self):
        self.pacientes_ingresados += self.patients_by_step[self.schedule.steps]
        self.schedule.step()
        self.datacollector.collect(self)
