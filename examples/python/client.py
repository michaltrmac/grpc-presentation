import logging
import os

import grpc

import validator_pb2
import validator_pb2_grpc


def run():
    server_url = '{}:{}'.format(
            os.getenv('GRPC_SERVER_HOST', 'localhost'),
            os.getenv('GRPC_SERVER_PORT', '50051')
    )

    with grpc.insecure_channel(server_url) as channel:
        stub = validator_pb2_grpc.ValidatorStub(channel)
        response = stub.ValidatePIN(validator_pb2.PINRequest(pin=input('PIN: ')))

    print("Validator response: {}, Err: {}".format(response.valid, response.err))


if __name__ == '__main__':
    logging.basicConfig()
    run()
