-- Tabela Aeroportos
CREATE TABLE Aeroportos (
    AeroportoID SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Localizacao VARCHAR(255) NOT NULL
);

-- Tabela Aeronaves
CREATE TABLE Aeronaves (
    AeronaveID SERIAL PRIMARY KEY,
    Modelo VARCHAR(255) NOT NULL,
    Capacidade INT NOT NULL
);

-- Tabela EstadosVoo
CREATE TABLE EstadosVoo (
    EstadoID SERIAL PRIMARY KEY,
    Descricao VARCHAR(255) NOT NULL
);

-- Tabela Voos
CREATE TABLE Voos (
    VooID SERIAL PRIMARY KEY,
    Origem VARCHAR(255) NOT NULL,
    Destino VARCHAR(255) NOT NULL,
    DataHoraPartida TIMESTAMP NOT NULL,
    DataHoraChegada TIMESTAMP NOT NULL
);

-- Tabela Manutencao
CREATE TABLE Manutencao (
    ManutencaoID SERIAL PRIMARY KEY,
    AeronaveID INT REFERENCES Aeronaves(AeronaveID),
    TipoManutencao VARCHAR(255) NOT NULL,
    DataHoraAgendamento TIMESTAMP NOT NULL,
    EquipeResponsavel VARCHAR(255) NOT NULL,
    EstadoID INT REFERENCES EstadosVoo(EstadoID)
);

-- Tabela TarefasManutencao
CREATE TABLE TarefasManutencao (
    TarefaID SERIAL PRIMARY KEY,
    ManutencaoID INT REFERENCES Manutencao(ManutencaoID),
    Descricao VARCHAR(255) NOT NULL,
    EstadoTarefa VARCHAR(255) NOT NULL,
    DataHoraInicio TIMESTAMP NOT NULL,
    DataHoraConclusao TIMESTAMP
);

-- Tabela Inventario
CREATE TABLE Inventario (
    ItemID SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    QuantidadeDisponivel INT NOT NULL,
    QuantidadeMinima INT NOT NULL,
    DataUltimaAtualizacao TIMESTAMP NOT NULL
);

-- Tabela UsoPeças
CREATE TABLE UsoPeças (
    UsoID SERIAL PRIMARY KEY,
    TarefaID INT REFERENCES TarefasManutencao(TarefaID),
    ItemID INT REFERENCES Inventario(ItemID),
    QuantidadeUtilizada INT NOT NULL
);

-- Tabela EquipasManutencao
CREATE TABLE EquipasManutencao (
    EquipaID SERIAL PRIMARY KEY,
    NomeEquipa VARCHAR(255) NOT NULL,
    Membros INT NOT NULL,
    Especialidade VARCHAR(255) NOT NULL
);

-- Tabela PeçasSubstituídas
CREATE TABLE PeçasSubstituídas (
    SubstituicaoID SERIAL PRIMARY KEY,
    TarefaID INT REFERENCES TarefasManutencao(TarefaID),
    ItemID INT REFERENCES Inventario(ItemID),
    QuantidadeSubstituida INT NOT NULL,
    RazaoSubstituicao VARCHAR(255) NOT NULL
);

-- Tabela Encomendas
CREATE TABLE Encomendas (
    EncomendaID SERIAL PRIMARY KEY,
    Fornecedor VARCHAR(255) NOT NULL,
    DataPedido TIMESTAMP NOT NULL,
    DataEntregaPrevista TIMESTAMP NOT NULL,
    EstadoEncomenda VARCHAR(255) NOT NULL
);

-- Tabela RelatóriosManutencao
CREATE TABLE RelatóriosManutencao (
    RelatorioID SERIAL PRIMARY KEY,
    ManutencaoID INT REFERENCES Manutencao(ManutencaoID),
    DetalhesProblema TEXT,
    AçõesCorretivas TEXT,
    Observacoes TEXT
);

-- Tabela Auditoria
CREATE TABLE Auditoria (
    AuditoriaID SERIAL PRIMARY KEY,
    UsuarioID INT REFERENCES Usuarios(UsuarioID),
    Operacao VARCHAR(255) NOT NULL,
    DataHoraOperacao TIMESTAMP NOT NULL,
    DetalhesOperacao TEXT
);

-- Tabela Usuarios
CREATE TABLE Usuarios (
    UsuarioID SERIAL PRIMARY KEY,
    NomeUsuario VARCHAR(255) NOT NULL,
    Senha VARCHAR(255) NOT NULL,
    NivelAcesso INT NOT NULL
);

-- Tabela RegrasAcesso
CREATE TABLE RegrasAcesso (
    RegraID SERIAL PRIMARY KEY,
    NivelAcesso INT NOT NULL,
    Permissoes TEXT
);
