from .models import Tasks
from .connection import DatabaseEngine
from sqlalchemy import desc

class TasksOperator:
    def select(self):
        with DatabaseEngine() as db:
            try:
                data = db.session.query(Tasks).order_by(desc(Tasks.task_id)).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def insert(self, description, date):
        with DatabaseEngine() as db:
            try:
                data_insert = Tasks(description=description, date=date)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, task_id):
        with DatabaseEngine() as db:
            try:
                db.session.query(Tasks).filter(Tasks.task_id == task_id).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, task_id, description, date):
        with DatabaseEngine() as db:
            try:
                db.session.query(Tasks).filter(Tasks.task_id == task_id).update({"description": description, "date": date})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
