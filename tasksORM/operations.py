from .models import Tasks, TaskStatus
from .connection import DatabaseEngine
from sqlalchemy import desc
from sqlalchemy.orm import join

class StatusTaskOperator:
    def select_all(self):
        with DatabaseEngine() as db:
            try:
                data = db.session.query(TaskStatus).all()
                
                return data
            
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_by_id(self, status_id):
        with DatabaseEngine() as db:
            try:
                status = db.session\
                    .query(TaskStatus).filter(TaskStatus.status_id == status_id)\
                    .first()
                
                return status
            
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_by_name(self, status_name):
        with DatabaseEngine() as db:
            try:
                status = db.session.query(TaskStatus)\
                .filter(TaskStatus.status_name == status_name).first()
                
                if status:
                    return status
                else:
                    return None
            
            except Exception as exception:
                db.session.rollback()
                raise exception

    
    def insert(self, status_name):
        with DatabaseEngine() as db:
            try:

                existing_status_id = self.select_by_name(status_name)                
                if existing_status_id:
                    return existing_status_id


                data_insert = TaskStatus(status_name=status_name)

                db.session.add(data_insert)
                db.session.commit()
                
                return data_insert.status_id
            
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def update(self, status_id, status_name):
        with DatabaseEngine() as db:
            try:
                
                db.session.query(TaskStatus)\
                    .filter(TaskStatus.status_id == status_id)\
                    .update({"status_name": status_name})
                
                db.session.commit()
            
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, status_id):
        with DatabaseEngine() as db:
            try:
                db.session.query(TaskStatus)\
                    .filter(TaskStatus.status_id == status_id)\
                    .delete()
                
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

class TasksOperator:
    def select_all(self):
        with DatabaseEngine() as db:
            try:
                data = db.session.query(Tasks).order_by(desc(Tasks.task_id)).all()
                
                return data
            
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_by_id(self, task_id):
        with DatabaseEngine() as db:
            try:
                task = db.session\
                    .query(Tasks).filter(Tasks.task_id == task_id).first()
                
                return task
            
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def insert(self, title, description, date, status_id):
        with DatabaseEngine() as db:
            try:
                data_insert = Tasks(title=title,
                                    description=description,
                                    date=date,
                                    status_id=status_id)

                db.session.add(data_insert)
                db.session.commit()
                
                return data_insert.task_id
            
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def update(self, task_id, title=None, description=None, date=None, status_id=None):
        with DatabaseEngine() as db:
            try:
                update_data = {}
                if title is not None:
                    update_data["title"] = title
                if description is not None:
                    update_data["description"] = description
                if date is not None:
                    update_data["date"] = date
                if status_id is not None:
                    update_data["status_id"] = status_id
                    
                db.session.query(Tasks)\
                    .filter(Tasks.task_id == task_id).update(update_data)
                
                db.session.commit()
            
            except Exception as exception:
                db.session.rollback()
                raise exception



    def delete(self, task_id):
        with DatabaseEngine() as db:
            try:
                db.session.query(Tasks)\
                    .filter(Tasks.task_id == task_id).delete()
                
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_all_by_id_desc(self, status_id):
        with DatabaseEngine() as db:
            try:
                data = db.session.query(Tasks)\
                    .join(TaskStatus)\
                    .filter(TaskStatus.status_id == status_id)\
                    .order_by(desc(Tasks.task_id))\
                    .all()

                return data
            
            except Exception as exception:
                db.session.rollback()
                raise exception