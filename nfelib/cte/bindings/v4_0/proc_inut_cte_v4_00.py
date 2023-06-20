from dataclasses import dataclass
from nfelib.cte.bindings.v4_0.inut_cte_tipos_basico_v4_00 import TprocInutCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class ProcInutCte(TprocInutCte):
    """
    Pedido de inutilzação de numeração de CT-e processado.
    """
    class Meta:
        name = "procInutCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"