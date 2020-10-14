




# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authenticate/token.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='authenticate/token.proto',
  package='authenticate',
  syntax='proto3',
  serialized_options=b'Z2github.com/iamport/interface/build/go/authenticate',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x61uthenticate/token.proto\x12\x0c\x61uthenticate\">\n\x05Token\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x0b\n\x03now\x18\x02 \x01(\x05\x12\x12\n\nexpired_at\x18\x03 \x01(\x05\"3\n\x0cTokenRequest\x12\x0f\n\x07imp_key\x18\x01 \x01(\t\x12\x12\n\nimp_secret\x18\x02 \x01(\t\"U\n\rTokenResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12%\n\x08response\x18\x03 \x01(\x0b\x32\x13.authenticate.TokenB4Z2github.com/iamport/interface/build/go/authenticateb\x06proto3'
)




_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='authenticate.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='authenticate.Token.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='now', full_name='authenticate.Token.now', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expired_at', full_name='authenticate.Token.expired_at', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=42,
  serialized_end=104,
)


_TOKENREQUEST = _descriptor.Descriptor(
  name='TokenRequest',
  full_name='authenticate.TokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imp_key', full_name='authenticate.TokenRequest.imp_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imp_secret', full_name='authenticate.TokenRequest.imp_secret', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=106,
  serialized_end=157,
)


_TOKENRESPONSE = _descriptor.Descriptor(
  name='TokenResponse',
  full_name='authenticate.TokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='authenticate.TokenResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='authenticate.TokenResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='authenticate.TokenResponse.response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=159,
  serialized_end=244,
)

_TOKENRESPONSE.fields_by_name['response'].message_type = _TOKEN
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['TokenRequest'] = _TOKENREQUEST
DESCRIPTOR.message_types_by_name['TokenResponse'] = _TOKENRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'authenticate.token_pb2'
  # @@protoc_insertion_point(class_scope:authenticate.Token)
  })
_sym_db.RegisterMessage(Token)

TokenRequest = _reflection.GeneratedProtocolMessageType('TokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOKENREQUEST,
  '__module__' : 'authenticate.token_pb2'
  # @@protoc_insertion_point(class_scope:authenticate.TokenRequest)
  })
_sym_db.RegisterMessage(TokenRequest)

TokenResponse = _reflection.GeneratedProtocolMessageType('TokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOKENRESPONSE,
  '__module__' : 'authenticate.token_pb2'
  # @@protoc_insertion_point(class_scope:authenticate.TokenResponse)
  })
_sym_db.RegisterMessage(TokenResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)





