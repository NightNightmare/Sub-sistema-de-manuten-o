from tortoise import fields
from tortoise.models import Model

class Note(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    filename = fields.CharField(max_length=256)
    title = fields.CharField(max_length=1000)
    content = fields.TextField(default="")

class Aeronave(Model):
    id = fields.IntField(pk=True)
    Nome = fields.CharField(max_length=256)
    descricao = fields.CharField(max_length=1000)
    
class TarefaManutencao(Model):
    id = fields.IntField(pk=True)
    aeronave = fields.ForeignKeyField('models.Aeronave', related_name='tarefas_manutencao')
    tipo_tarefa = fields.CharField(max_length=50)
    equipe_responsavel = fields.CharField(max_length=100)
    data_agendada = fields.DatetimeField()
    data_conclusao = fields.DatetimeField(null=True)
    progresso = fields.IntField()
    observacoes = fields.TextField()