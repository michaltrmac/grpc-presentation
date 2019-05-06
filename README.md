Presentation available on https://michaltrmac.github.io/grpc-presentation/

## Examples

Located in `examples` directory.

This directory contains basics examples of gRPC python server, python client and PHP client.

There is one service called "Validator" with method "ValidatePIN". This method is exposed through python gRPC server. Python and PHP clients have same code - wait for input, send it to server and print response.

**TODO:** bidirectional streaming example

## How to run examples

1. Generete stubs from proto files
```
docker-compose -f docker-compose-proto-gen.yml up
```

2. Run gRPC server
```
docker-compose up -d grpc-server
```

3. Install PHP packages
```
docker-compose run php-client /usr/local/bin/composer install
```

4. Run gRPC clients
```
docker-compose run python-client
docker-compose run php-client
```