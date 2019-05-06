FROM php:7.3.2-cli-alpine3.9

RUN apk add --update --no-cache \
    curl \
    zip \
    unzip \
    zlib-dev \
    autoconf \
    gcc \
    g++ \
    make \
    git

# install composer
RUN cd /usr/local/bin && curl -sS https://getcomposer.org/installer | php
RUN cd /usr/local/bin && mv composer.phar composer

RUN pecl install grpc
RUN docker-php-ext-enable grpc
RUN docker-php-ext-install bcmath
RUN pecl install protobuf
RUN docker-php-ext-enable protobuf
RUN apk add --update --no-cache \
    gmp-dev
RUN docker-php-ext-install gmp
RUN docker-php-ext-enable gmp