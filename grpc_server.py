import grpc
from concurrent import futures

import tasks_pb2
import tasks_pb2_grpc
import status_pb2
import status_pb2_grpc

from tasksORM.operations import TasksOperator, StatusTaskOperator
from utils.date import DateTimeUtils

import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# .env
dotenv_path = os.path.dirname(__file__) + '/dotenv_files/.env'
load_dotenv(dotenv_path)
PORT = int(os.environ.get("PORT", 50051))


class StatusTaskService(status_pb2_grpc.TasksServicer):
    def __init__(self):
        self.status_operator = StatusTaskOperator()
    
    def GetStatusById(self, request, context):
        """
        Lista um status especificado pelo id

        Returns:
            Uma resposta gRPC contendo um status específico
        """
        status = self.status_operator.select_by_id(request.status_id)
        if status:
            return status_pb2.GetStatusByIdResponse(
                status = status_pb2.TaskStatus(
                        status_id=status.status_id,
                        status_name=status.status_name
                    )
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f'Status não encontrado no banco de dados')
            return status_pb2.GetStatusByIdResponse()

    def GetStatusByName(self, request, context):
        """
        Retorna o status pelo nome.

        Returns:
            Retorna o status correspondente ao nome fornecido.
        """

        if not request.status_name:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("O campo 'status_name' é obrigatório.")
            return status_pb2.GetStatusByNameResponse()

        try:
            status = self.status_operator.select_by_name(request.status_name.strip())

            # Se o status não for encontrado, retorne um erro
            if not status:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("O status não foi encontrado.")
                return status_pb2.GetStatusByNameResponse()

            # Se o status for encontrado, retorne na resposta
            return status_pb2.GetStatusByNameResponse(status={"status_id": status.status_id, "status_name": status.status_name})

        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return tasks_pb2.GetStatusByNameResponse()

    def GetStatus(self, request, context):
        """
        Obtém todos os status.

        Retorna:
            Uma resposta gRPC contendo uma lista de status.
        """
        status_all = self.status_operator.select_all()
        status_messages = []

        for status in status_all:
            status_message = status_pb2.TaskStatus(
                status_id=status.status_id,
                status_name=status.status_name
            )
            status_messages.append(status_message)

        return status_pb2.GetStatusResponse(status=status_messages)

    def CreatStatus(self, request, context):
        """
        Cria um novo status.

        Retorna:
            Retorna o ID do status criado se bem-sucedido, caso contrário, retorna um erro.
        """
        try:
            status_id = self.status_operator.insert(request.status.status_name)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return status_pb2.CreateStatusResponse()

        return status_pb2.CreateStatusResponse(status_id=status_id)

    def UpdatStatus(self, request, context):
        """
        Atualiza um status existente.

        Retorna:
            Retorna uma resposta vazia se a atualização for bem-sucedida, caso contrário, retorna um erro.
        """
        if not request.status.status_id:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("ID (status_id) do status não fornecido.")
            return status_pb2.UpdateStatusResponse()

        try:
            self.status_operator.update(request.status.status_id, request.status.status_name)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return status_pb2.UpdateStatusResponse()

        return status_pb2.UpdateStatusResponse()

    def DeletStatus(self, request, context):
        """
        Exclui um status existente.

        Retorna:
            Retorna uma resposta vazia se a exclusão for bem-sucedida, caso contrário, retorna um erro.
        """
        if not request.status_id:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("ID (status_id) do status não fornecido.")
            return status_pb2.DeleteStatusResponse()

        try:
            self.status_operator.delete(request.status_id)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return status_pb2.DeleteStatusResponse()

        return status_pb2.DeleteStatusResponse()

class TasksServicer(tasks_pb2_grpc.TasksServicer):
    def __init__(self):
        self.tasks_operator = TasksOperator()
        self.status_operator = StatusTaskOperator()

    def GetTasks(self, request, context):
        """
        Listar tasks cadastradas em ordem decrecente

        Returns:
            Uma resposta gRPC contendo uma lista de tarefas.
        """
        tasks = self.tasks_operator.select_all()
        task_messages = []
        
        for task in tasks:
            date_string = DateTimeUtils.convert_to_string(task.date)

            # Convertendo as tarefas para mensagens GPRC
            task_message = tasks_pb2.Task(
                task_id=task.task_id,
                title=task.title,
                description=task.description,
                date=date_string,
                status_id=task.status_id
            )
            task_messages.append(task_message)
        
        return tasks_pb2.GetTasksResponse(tasks=task_messages)

    def GetTaskById(self, request, context):
        """
        Lista uma task especificada pelo id

        Returns:
            Uma resposta gRPC contendo uma task especifica
        """
        task = self.tasks_operator.select_by_id(request.task_id)
        if task:
            date_string = DateTimeUtils.convert_to_string(task.date)
            return tasks_pb2.GetTaskByIdResponse(
                task = tasks_pb2.Task(
                    task_id=task.task_id,
                    title=task.title,
                    description=task.description,
                    date=date_string,
                    status_id=task.status_id)
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f'Tarefa não encontrada no banco de dados')
            return tasks_pb2.GetTaskByIdResponse()
        
    def CreateTask(self, request, context):
        """
        Cria uma nova task.

        Returns:
            Retorna o id da task criada se bem-sucedido, caso contrário, retorna um erro.
        """

        new_task_data = {
            'title': request.task.title,
            'description': request.task.description,
            'date': DateTimeUtils.convert_to_datetime(request.task.date),
            'status_id': request.task.status_id
        }

        try:
            task_id = self.tasks_operator.insert(**new_task_data)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return tasks_pb2.CreateTaskResponse()

        return tasks_pb2.CreateTaskResponse(task_id=task_id)

    def UpdateTask(self, request, context):
        """
        Atualiza uma task existente.

        Returns:
            Retorna uma resposta vazia se a atualização for bem-sucedida, caso contrário, retorna um erro.
        """

        if not request.task.task_id:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("O campo 'task_id' é obrigatório.")
            return tasks_pb2.UpdateTaskResponse()

        update_data = {}
        if request.task.title:
            update_data["title"] = request.task.title
        if request.task.description:
            update_data["description"] = request.task.description
        if request.task.date:
            update_data["date"] = DateTimeUtils.convert_to_datetime(request.task.date)
        if request.task.status_id:
            update_data["status_id"] = request.task.status_id

        try:
            task_id = request.task.task_id
            self.tasks_operator.update(task_id, **update_data)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return tasks_pb2.UpdateTaskResponse()

        return tasks_pb2.UpdateTaskResponse()

    def DeleteTask(self, request, context):
        """
        Exclui uma task existente.

        Returns:
            Retorna uma resposta vazia se a exclusão for bem-sucedida, caso contrário, retorna um erro.
        """
        
        if not request.task_id:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("ID (task_id) da tarefa não fornecido.")
            return tasks_pb2.DeleteTaskResponse()

        try:
            task_id = request.task_id
            self.tasks_operator.delete(task_id)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return tasks_pb2.DeleteTaskResponse()

        return tasks_pb2.DeleteTaskResponse()

    def GetTasksByStatus(self, request, context):
        """
        Retorna todas as tarefas associadas a um determinado status.

        Returns:
            Retorna as tarefas associadas ao status especificado na solicitação.
        """
        try:
            if not request.status_name:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("O campo 'status_name' é obrigatório.")
                return tasks_pb2.GetTasksResponse()

            # Obtenha o status usando o nome fornecido
            status = self.status_operator.select_by_name(request.status_name)
            print(status)
            if not status:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Status não encontrado.")
                return tasks_pb2.GetTasksResponse()

            # Obtendo todas as tarefas associadas ao status obtido
            tasks = self.tasks_operator.select_all_by_id_desc(status.status_id)

            # Converta para gRPC
            task_messages = []
            for task in tasks:
                date_string = DateTimeUtils.convert_to_string(task.date)
                task_message = tasks_pb2.Task(
                    task_id=task.task_id,
                    title=task.title,
                    description=task.description,
                    date=date_string,
                    status_id=task.status_id
                )
                task_messages.append(task_message)

            return tasks_pb2.GetTasksResponse(tasks=task_messages)

        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return tasks_pb2.GetTasksResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tasks_pb2_grpc.add_TasksServicer_to_server(TasksServicer(), server)
    status_pb2_grpc.add_TasksServicer_to_server(StatusTaskService(), server)
    server.add_insecure_port(f'[::]:{PORT}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print(f'Starting server in: localhost:{PORT}')
    serve()