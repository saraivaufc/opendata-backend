from data.models.task import Task
from .auxilio_emergencial import AuxilioEmergencialService
from .cotas_parlamentares import CotasParlamentaresService
from .cotacoes_historicas_b3 import CotacoesHistoricasB3Service

get_service = {
    Task.AUXILIO_EMERGENCIAL: AuxilioEmergencialService(),
    Task.COTAS_PARLAMENTARES: CotasParlamentaresService(),
    Task.COTACOES_HISTORICAS_B3: CotacoesHistoricasB3Service()
}
