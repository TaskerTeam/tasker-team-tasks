import grpc
from concurrent import futures
import tasks_pb2
import tasks_pb2_grpc
from tasksORM.operations import TasksOperator
from utils.date import DateTimeUtils

class TasksServicer(tasks_pb2_grpc.TasksServicer):
    def __init__(self):
        self.tasks_operator = TasksOperator()


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
                date=date_string
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
                    date=date_string)
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
            'date': DateTimeUtils.convert_to_datetime(request.task.date)
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
            context.set_details(f'ID (task_id) da tarefa não fornecido.')
            return tasks_pb2.UpdateTaskResponse()
        

        update_data = {}
        if request.task.title:
            update_data["title"] = request.task.title
        if request.task.description:
            update_data["description"] = request.task.description
        if request.task.date:
            update_data["date"] = DateTimeUtils.convert_to_datetime(request.task.date)

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


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tasks_pb2_grpc.add_TasksServicer_to_server(TasksServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print(f'Starting server in: localhost:50051')
    serve()