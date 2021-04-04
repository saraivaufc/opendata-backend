from data.models.task import Task
from .auxilio_emergencial import AuxilioEmergencialService
from .cotas_parlamentares import CotasParlamentaresService

get_service = {
    Task.AUXILIO_EMERGENCIAL: AuxilioEmergencialService(),
    Task.COTAS_PARLAMENTARES: CotasParlamentaresService()
}
