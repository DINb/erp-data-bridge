from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from datetime import datetime

app = FastAPI(title="Oracle ERP Integration Bridge", version="1.0.0")

# --- MODELO FUNCIONAL (Regras de Negócio do ERP) ---
class Invoice(BaseModel):
    vendor_id: int
    invoice_num: str
    invoice_amount: float = Field(..., gt=0) # Valor deve ser > 0
    invoice_date: str
    currency: str = "BRL"
    
    @field_validator('invoice_date')
    def validate_date(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d')
            return v
        except ValueError:
            raise ValueError('A data deve estar no formato AAAA-MM-DD (Padrão ERP)')

# --- ENDPOINTS (A Integração) ---

@app.get("/")
def home():
    return {"status": "Online", "msg": "Pronto para validar dados de integração."}

@app.post("/validate-invoice/")
async def validate_invoice(invoice: Invoice):
    """
    Simula o recebimento de uma Nota de um sistema externo 
    e valida as regras antes de enviar ao Oracle OIC.
    """
    # Simulação de regra funcional: IDs de fornecedores específicos
    if invoice.vendor_id < 100:
        raise HTTPException(status_code=400, detail="Vendor ID inválido no mestre de fornecedores do ERP.")

    # Simulação de Payload formatado para o Oracle Integration Cloud (OIC)
    oic_payload = {
        "Header": {"Source": "Python_Bridge", "Timestamp": str(datetime.now())},
        "Body": {
            "Operation": "CreateInvoice",
            "Data": invoice.model_dump()
        }
    }
    
    return {
        "status": "Success",
        "message": "Dados higienizados e validados. Pronto para carga no Oracle Cloud.",
        "integration_ready_payload": oic_payload
    }
