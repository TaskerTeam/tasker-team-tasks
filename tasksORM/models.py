from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

# Criar uma instância da base declarativa
Base = declarative_base()

class TaskStatus(Base):
    __tablename__ = "task_status"

    status_id = Column(Integer, primary_key=True, name='status_id')
    status_name = Column(String, nullable=False, name='status_name')

    tasks = relationship("Tasks", back_populates="status")

    def __repr__(self):
        """Retorna uma representação legível do objeto StatusTarefa."""
        return f"StatusTarefa(status_id={self.status_id}, status_name={self.status_name})"


class Tasks(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, name='task_id')
    title = Column(String, nullable=False, name='title')
    description = Column(String, nullable=False, name='description')
    date = Column(DateTime, nullable=False, name='date')
    status_id = Column(Integer, ForeignKey('task_status.status_id'), nullable=False)
    
    status = relationship("TaskStatus", back_populates="tasks")

    def __repr__(self):
        """Retorna uma representação legível do objeto Task."""
        return f"Task(task_id={self.task_id}, description={self.description}, date={self.date})"