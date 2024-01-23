from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime
from database import init_db
from models import Aeronave, Manutencao, EquipeManutencao, TarefaManutencao, Peca, UsoPeca, RelatorioManutencao

app = FastAPI(title="fastapi-gcp")
init_db(app)

@app.get("/", response_class=HTMLResponse)
def healthcheck():
    return "<h1>All good!</h2>"

class CreateAeronavePayload(BaseModel):
    Nome: str
    descricao: str

class CreateTarefaManutencaoPayload(BaseModel):
    aeronave: int  
    tipo_tarefa: str
    equipe_responsavel: str
    progresso: int
    observacoes: str
    data_agendada: datetime

class CreatePecaPayload(BaseModel):
    nome: str
    quantidade_disponivel: int

class CreateUsoPecaPayload(BaseModel):
    id_tarefa: int
    id_peca: int
    quantidade_necessaria: int

class CreateRelatorioManutencaoPayload(BaseModel):
    id_aeronave: int
    descricao: str
    data_criacao: datetime

@app.post("/aeronave")
async def create_aeronave(payload: CreateAeronavePayload):
    aeronave = await Aeronave.create(**payload.dict())
    return {"message": f"Aeronave created successfully with id {aeronave.id}"}

@app.get("/aeronave/{Nome}")
async def get_aeronave_by_nome(Nome: str):
    if not (aeronave := await Aeronave.get_or_none(Nome=Nome)):
        raise HTTPException(status_code=404, detail="Aeronave not found")

    return aeronave

@app.post("/manutencao")
async def create_manutencao(payload: CreateTarefaManutencaoPayload):
    aeronave_instance = await Aeronave.get_or_none(id=payload.aeronave)
    if not aeronave_instance:
        raise HTTPException(status_code=404, detail="Aeronave not found")

    payload_dict = payload.dict(exclude={"aeronave"})
    manutencao = await TarefaManutencao.create(aeronave=aeronave_instance, **payload_dict)
    return {"message": f"TarefaManutencao created successfully with id {manutencao.id}"}

@app.get("/manutencao/{id}")
async def get_manutencao_by_id(id: int):
    if not (manutencao := await TarefaManutencao.get_or_none(id=id)):
        raise HTTPException(status_code=404, detail="TarefaManutencao not found")

    return manutencao

@app.post("/peca")
async def create_peca(payload: CreatePecaPayload):
    peca = await Peca.create(**payload.dict())
    return {"message": f"Peca created successfully with id {peca.id}"}

@app.post("/usopeca")
async def create_uso_peca(payload: CreateUsoPecaPayload):
    tarefa_instance = await TarefaManutencao.get_or_none(id=payload.id_tarefa)
    peca_instance = await Peca.get_or_none(id=payload.id_peca)

    if not tarefa_instance or not peca_instance:
        raise HTTPException(status_code=404, detail="TarefaManutencao or Peca not found")

    uso_peca = await UsoPeca.create(id_tarefa=tarefa_instance, id_peca=peca_instance, quantidade_necessaria=payload.quantidade_necessaria)
    return {"message": f"UsoPeca created successfully with id {uso_peca.id}"}

@app.post("/relatoriomanutencao")
async def create_relatorio_manutencao(payload: CreateRelatorioManutencaoPayload):
    aeronave_instance = await Aeronave.get_or_none(id=payload.id_aeronave)
    if not aeronave_instance:
        raise HTTPException(status_code=404, detail="Aeronave not found")

    relatorio_manutencao = await RelatorioManutencao.create(aeronave=aeronave_instance, **payload.dict())
    return {"message": f"RelatorioManutencao created successfully with id {relatorio_manutencao.id}"}

@app.get("/relatoriomanutencao/{id}")
async def get_relatorio_manutencao_by_id(id: int):
    if not (relatorio_manutencao := await RelatorioManutencao.get_or_none(id=id)):
        raise HTTPException(status_code=404, detail="RelatorioManutencao not found")

    return relatorio_manutencao
