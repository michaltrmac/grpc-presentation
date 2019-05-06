# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: validator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='validator.proto',
  package='validator',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fvalidator.proto\x12\tvalidator\"\x19\n\nPINRequest\x12\x0b\n\x03pin\x18\x01 \x01(\t\")\n\x0bPINResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x0b\n\x03\x65rr\x18\x02 \x01(\t2K\n\tValidator\x12>\n\x0bValidatePIN\x12\x15.validator.PINRequest\x1a\x16.validator.PINResponse\"\x00\x62\x06proto3')
)




_PINREQUEST = _descriptor.Descriptor(
  name='PINRequest',
  full_name='validator.PINRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pin', full_name='validator.PINRequest.pin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=55,
)


_PINRESPONSE = _descriptor.Descriptor(
  name='PINResponse',
  full_name='validator.PINResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid', full_name='validator.PINResponse.valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err', full_name='validator.PINResponse.err', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['PINRequest'] = _PINREQUEST
DESCRIPTOR.message_types_by_name['PINResponse'] = _PINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PINRequest = _reflection.GeneratedProtocolMessageType('PINRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINREQUEST,
  __module__ = 'validator_pb2'
  # @@protoc_insertion_point(class_scope:validator.PINRequest)
  ))
_sym_db.RegisterMessage(PINRequest)

PINResponse = _reflection.GeneratedProtocolMessageType('PINResponse', (_message.Message,), dict(
  DESCRIPTOR = _PINRESPONSE,
  __module__ = 'validator_pb2'
  # @@protoc_insertion_point(class_scope:validator.PINResponse)
  ))
_sym_db.RegisterMessage(PINResponse)



_VALIDATOR = _descriptor.ServiceDescriptor(
  name='Validator',
  full_name='validator.Validator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=100,
  serialized_end=175,
  methods=[
  _descriptor.MethodDescriptor(
    name='ValidatePIN',
    full_name='validator.Validator.ValidatePIN',
    index=0,
    containing_service=None,
    input_type=_PINREQUEST,
    output_type=_PINRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VALIDATOR)

DESCRIPTOR.services_by_name['Validator'] = _VALIDATOR

# @@protoc_insertion_point(module_scope)
