<?php

require dirname(__FILE__).'/vendor/autoload.php';

@include_once dirname(__FILE__).'/Validator/ValidatorClient.php';
@include_once dirname(__FILE__).'/Validator/PINRequest.php';
@include_once dirname(__FILE__).'/Validator/PINResponse.php';
@include_once dirname(__FILE__).'/GPBMetadata/Validator.php';


function validate($pin)
{
    $server_url = (getenv('GRPC_SERVER_HOST') ?: '[::]').':'.getenv('GRPC_SERVER_PORT') ?: '50051';

    $client = new Validator\ValidatorClient($server_url, [
        'credentials' => Grpc\ChannelCredentials::createInsecure(),
    ]);

    $request = new Validator\PINRequest();
    $request->setPin($pin);
    list($reply, $status) = $client->ValidatePIN($request)->wait();

    return $reply;
}

echo "PIN: ";
$reply = validate(trim(fgets(STDIN)));

echo "Validator response: ".var_export($reply->getValid(), true).", Err: ".$reply->getErr()."\n";
