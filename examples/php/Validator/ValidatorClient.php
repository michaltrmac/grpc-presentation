<?php
// GENERATED CODE -- DO NOT EDIT!

namespace Validator;

/**
 * The validator service definition.
 */
class ValidatorClient extends \Grpc\BaseStub {

    /**
     * @param string $hostname hostname
     * @param array $opts channel options
     * @param \Grpc\Channel $channel (optional) re-use channel object
     */
    public function __construct($hostname, $opts, $channel = null) {
        parent::__construct($hostname, $opts, $channel);
    }

    /**
     * validate personal identification number
     * @param \Validator\PINRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     */
    public function ValidatePIN(\Validator\PINRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/validator.Validator/ValidatePIN',
        $argument,
        ['\Validator\PINResponse', 'decode'],
        $metadata, $options);
    }

}
