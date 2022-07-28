import os

#Agents
from agents.patient import PatientAgent
from agents.triage import TriageAgent

# Models
from models.emergency import EmergencyModel

if __name__=='__main__':
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    triage_agent = TriageAgent()
    emergency_model = EmergencyModel(
        n=10, 
        triage_agent=triage_agent
    )

    # Test con un solo paso
    emergency_model.step()
    for p in emergency_model.schedule.agents:
        print(p.fase)

    # # Test con un múltiples pasos
    for s in range(8):
         emergency_model.step()

