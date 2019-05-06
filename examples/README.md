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