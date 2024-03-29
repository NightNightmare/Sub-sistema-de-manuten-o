from tortoise import fields
from tortoise.models import Model

class Aeronave(Model):
    id = fields.IntField(pk=True)
    nome = fields.CharField(max_length=255)
    modelo = fields.CharField(max_length=255)
    # Adicionando opções de escolha para o campo disponibilidade
    DISPONIBILIDADE_CHOICES = [("Disponível", "Disponível"), ("Não Disponível", "Não Disponível")]
    disponibilidade = fields.CharField(max_length=15, choices=DISPONIBILIDADE_CHOICES, default="Disponível")
    
    descricao = fields.CharField(max_length=1000)

class Manutencao(Model):
    id = fields.IntField(pk=True)
    id_aeronave = fields.ForeignKeyField("models.Aeronave", related_name="id_aeronav", on_delete="CASCADE")
    tipo_manutencao = fields.CharField(max_length=255)
    data = fields.DateField()
    
    # Adicionando opções de escolha para o campo observacao
    OPCOES_OBSERVACAO = [("fase_inicial", "Fase Inicial"), ("em_progresso", "Em Progresso"), ("concluida", "Concluída")]
    observacao = fields.CharField(max_length=255, choices=OPCOES_OBSERVACAO)
    
    # forma de atualizar a escolha
    # manutencao = await Manutencao.create(id_aeronave=aeronave_instance, tipo_manutencao="Reparo", data=now, observacao="em_progresso")

class EquipeManutencao(Model):
    id = fields.IntField(pk=True)
    nome = fields.CharField(max_length=255)

class TarefaManutencao(Model):
    id = fields.IntField(pk=True)
    id_manutencao = fields.ForeignKeyField('models.Manutencao', related_name='id_de_Manutencao')
    equipa = fields.ForeignKeyField('models.EquipeManutencao', related_name='id_equipa')
    # ka atxal precisso pmd no ta txomal na tabela manutenção la na tipo_manutenção, nhos da opinião
    # tipo_tarefa = fields.CharField(max_length=255)
    data_inicio = fields.DatetimeField()
    data_conclusao = fields.DatetimeField(null=True)
    progresso = fields.IntField()

class Peca(Model):
    id = fields.IntField(pk=True)
    nome = fields.CharField(max_length=255)
    quantidade_disponivel = fields.IntField()

class UsoPeca(Model):
    id = fields.IntField(pk=True)
    id_tarefa = fields.ForeignKeyField('models.TarefaManutencao', related_name='id_tarefa')
    id_peca = fields.ForeignKeyField('models.Peca', related_name='id_peca')
    quantidade_necessaria = fields.IntField()

class RelatorioManutencao(Model):
    id = fields.IntField(pk=True)
    id_tarefa = fields.ForeignKeyField('models.TarefaManutencao', related_name='id_de_tarefa')
    data_criacao = fields.DatetimeField(null=True)
