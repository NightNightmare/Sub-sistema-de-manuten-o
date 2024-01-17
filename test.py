from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime
from database import init_db
from models import Note
from models import Aeronave
from models import TarefaManutencao

app = FastAPI(title="fastapi-gcp")
init_db(app)

@app.get("/", response_class=HTMLResponse)
def healthcheck():
    return "<h1>All good!</h2>"

class CreateNotePayload(BaseModel):
    filename: str
    title: str
    content: str
class CreatAeronavePayload(BaseModel):
    Nome: str
    descricao: str
class CreatTarefaManutencaoPayload(BaseModel):
    aeronave: int  
    tipo_tarefa: str
    equipe_responsavel: str
    progresso: int
    observacoes: str
    data_agendada: datetime

@app.post("/notes")
async def create_note(payload: CreateNotePayload):
    note = await Note.create(**payload.dict())
    return {"message": f"Note created successfully with id {note.id}"}

@app.post("/manutencao")
async def create_manutencao(payload: CreatTarefaManutencaoPayload):
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

    return note
@app.get("/notes/{title}")
async def get_note_by_title(title: str):
    if not (note := await TarefaManutencao.get_or_none(title=title)):
        raise HTTPException(status_code=404, detail="Note not found")

    return note

@app.post("/aeronave")
async def create_aeronave(payload: CreatAeronavePayload):
    aeronave = await Aeronave.create(**payload.dict())
    return {"message": f"Aeronave created successfully with id {aeronave.id}"}

@app.get("/aeronave/{Nome}")
async def get_aeronave_by_nome(Nome: str):
    if not (aeronave := await Aeronave.get_or_none(Nome=Nome)):
        raise HTTPException(status_code=404, detail="Aeronave not found")

    return aeronave