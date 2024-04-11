from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

# Criar uma instância da base declarativa
Base = declarative_base()

class Tasks(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, name='task_id')
    title = Column(String, nullable=False, name='title')
    description = Column(String, nullable=False, name='description')
    date = Column(DateTime, nullable=False, name='date')


    def __repr__(self):
        """Retorna uma representação legível do objeto Task."""
        return f"Task(task_id={self.task_id}, description={self.description}, date={self.date})"