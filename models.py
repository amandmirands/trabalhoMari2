from db import Base
from sqlalchemy import Column, Integer, DateTime, Float, Integer, Text

#Implementa a classe DadoCLP a partir da Base do sqlalchemy
class DadoCLP(Base):
    """
    Modelo dos dados do CLP
    """
    #como não temos construtor, usa o da base
    __tablename__ = 'dadoclp' #nome da tabela
    id = Column(Integer, primary_key=True) #id principal
    timestamp = Column(DateTime) #coluna timestamp
    torque = Column(Float) #coluna temperatura, etc...
    carga = Column(Float)
    freq_rot = Column(Float)
    vel_est = Column(Float)
    freq = Column(Float)
    current = Column(Float)
    P = Column(Integer)
    Q = Column(Integer)
    S = Column(Integer)
    startType = Column(Text)
    activeMotor = Column(Text)
    inversorFreq = Column(Float)
    temp_R = Column(Float)
    temp_S = Column(Float)
    temp_T = Column(Float)
    temp_C = Column(Float)
    corr_R = Column(Float)
    corr_S = Column(Float)
    corr_T = Column(Float)
    corr_N = Column(Float)
    ddp_RS = Column(Float)
    ddp_ST = Column(Float)
    ddp_TR = Column(Float)
    sel_pid = Column(Float)
    mv_escreve = Column(Float)

    def get_attr_list(self): #método auxiliar p/ ajudar a printar os dados na tela
        return self.timestamp