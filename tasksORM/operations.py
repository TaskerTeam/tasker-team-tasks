from .models import Tasks
from .connection import DatabaseEngine
from sqlalchemy import desc

class TasksOperator:
    def select_all(self):
        with DatabaseEngine() as db:
            try:
                data = db.session\
                    .query(Tasks)\
                    .order_by(desc(Tasks.task_id))\
                    .all()
                
                return data
            
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_by_id(self, task_id):
        with DatabaseEngine() as db:
            try:
                task = db.session\
                    .query(Tasks)\
                    .filter(Tasks.task_id == task_id)\
                    .first()
                
                return task
            
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def insert(self, title, description, date):
        with DatabaseEngine() as db:
            try:
                data_insert = Tasks(title=title,
                                    description=description,
                                    date=date)

                db.session.add(data_insert)
                db.session.commit()
                
                return data_insert.task_id
            
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def update(self, task_id, title=None, description=None, date=None):
        with DatabaseEngine() as db:
            try:
                update_data = {}
                if title is not None:
                    update_data["title"] = title
                if description is not None:
                    update_data["description"] = description
                if date is not None:
                    update_data["date"] = date
                
                db.session.query(Tasks)\
                    .filter(Tasks.task_id == task_id)\
                    .update(update_data)
                
                db.session.commit()
            
            except Exception as exception:
                db.session.rollback()
                raise exception


    def delete(self, task_id):
        with DatabaseEngine() as db:
            try:
                db.session.query(Tasks)\
                    .filter(Tasks.task_id == task_id)\
                    .delete()
                
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception