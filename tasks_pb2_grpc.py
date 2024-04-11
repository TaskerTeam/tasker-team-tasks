# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tasks_pb2 as tasks__pb2


class TasksStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTasks = channel.unary_unary(
                '/tasks.Tasks/GetTasks',
                request_serializer=tasks__pb2.GetTasksRequest.SerializeToString,
                response_deserializer=tasks__pb2.GetTasksResponse.FromString,
                )
        self.GetTaskById = channel.unary_unary(
                '/tasks.Tasks/GetTaskById',
                request_serializer=tasks__pb2.GetTaskByIdRequest.SerializeToString,
                response_deserializer=tasks__pb2.GetTaskByIdResponse.FromString,
                )
        self.CreateTask = channel.unary_unary(
                '/tasks.Tasks/CreateTask',
                request_serializer=tasks__pb2.CreateTaskRequest.SerializeToString,
                response_deserializer=tasks__pb2.CreateTaskResponse.FromString,
                )
        self.UpdateTask = channel.unary_unary(
                '/tasks.Tasks/UpdateTask',
                request_serializer=tasks__pb2.UpdateTaskRequest.SerializeToString,
                response_deserializer=tasks__pb2.UpdateTaskResponse.FromString,
                )
        self.DeleteTask = channel.unary_unary(
                '/tasks.Tasks/DeleteTask',
                request_serializer=tasks__pb2.DeleteTaskRequest.SerializeToString,
                response_deserializer=tasks__pb2.DeleteTaskResponse.FromString,
                )


class TasksServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TasksServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTasks,
                    request_deserializer=tasks__pb2.GetTasksRequest.FromString,
                    response_serializer=tasks__pb2.GetTasksResponse.SerializeToString,
            ),
            'GetTaskById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskById,
                    request_deserializer=tasks__pb2.GetTaskByIdRequest.FromString,
                    response_serializer=tasks__pb2.GetTaskByIdResponse.SerializeToString,
            ),
            'CreateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTask,
                    request_deserializer=tasks__pb2.CreateTaskRequest.FromString,
                    response_serializer=tasks__pb2.CreateTaskResponse.SerializeToString,
            ),
            'UpdateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTask,
                    request_deserializer=tasks__pb2.UpdateTaskRequest.FromString,
                    response_serializer=tasks__pb2.UpdateTaskResponse.SerializeToString,
            ),
            'DeleteTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTask,
                    request_deserializer=tasks__pb2.DeleteTaskRequest.FromString,
                    response_serializer=tasks__pb2.DeleteTaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tasks.Tasks', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Tasks(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasks.Tasks/GetTasks',
            tasks__pb2.GetTasksRequest.SerializeToString,
            tasks__pb2.GetTasksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasks.Tasks/GetTaskById',
            tasks__pb2.GetTaskByIdRequest.SerializeToString,
            tasks__pb2.GetTaskByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasks.Tasks/CreateTask',
            tasks__pb2.CreateTaskRequest.SerializeToString,
            tasks__pb2.CreateTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasks.Tasks/UpdateTask',
            tasks__pb2.UpdateTaskRequest.SerializeToString,
            tasks__pb2.UpdateTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tasks.Tasks/DeleteTask',
            tasks__pb2.DeleteTaskRequest.SerializeToString,
            tasks__pb2.DeleteTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
