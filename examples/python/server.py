import logging
import os
import sys
import time
from concurrent import futures

import grpc

import validator_pb2
import validator_pb2_grpc

from lib import checkValidRC

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Validator(validator_pb2_grpc.ValidatorServicer):

    def ValidatePIN(self, request, context):
        logging.getLogger().debug('Recived PIN "{}" for validation'.format(request.pin))

        valid, message = checkValidRC(request.pin)

        return validator_pb2.PINResponse(valid=valid, err=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    validator_pb2_grpc.add_ValidatorServicer_to_server(Validator(), server)

    server_url = '{}:{}'.format(
            os.getenv('GRPC_SERVER_HOST', '[::]'),
            os.getenv('GRPC_SERVER_PORT', '50051')
    )

    server.add_insecure_port(server_url)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(message)s")
    serve()
