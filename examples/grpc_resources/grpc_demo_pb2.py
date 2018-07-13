# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_resources/grpc_demo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_resources/grpc_demo.proto',
  package='bramble',
  syntax='proto3',
  serialized_pb=_b('\n\x1egrpc_resources/grpc_demo.proto\x12\x07\x62ramble\"u\n\x0b\x44\x65moMessage\x12\x35\n\tb3_values\x18\x04 \x03(\x0b\x32\".bramble.DemoMessage.B3ValuesEntry\x1a/\n\rB3ValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x46\n\x0b\x44\x65moService\x12\x37\n\x07\x44\x65moRPC\x12\x14.bramble.DemoMessage\x1a\x14.bramble.DemoMessage\"\x00\x62\x06proto3')
)




_DEMOMESSAGE_B3VALUESENTRY = _descriptor.Descriptor(
  name='B3ValuesEntry',
  full_name='bramble.DemoMessage.B3ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bramble.DemoMessage.B3ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='bramble.DemoMessage.B3ValuesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=160,
)

_DEMOMESSAGE = _descriptor.Descriptor(
  name='DemoMessage',
  full_name='bramble.DemoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='b3_values', full_name='bramble.DemoMessage.b3_values', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEMOMESSAGE_B3VALUESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=160,
)

_DEMOMESSAGE_B3VALUESENTRY.containing_type = _DEMOMESSAGE
_DEMOMESSAGE.fields_by_name['b3_values'].message_type = _DEMOMESSAGE_B3VALUESENTRY
DESCRIPTOR.message_types_by_name['DemoMessage'] = _DEMOMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DemoMessage = _reflection.GeneratedProtocolMessageType('DemoMessage', (_message.Message,), dict(

  B3ValuesEntry = _reflection.GeneratedProtocolMessageType('B3ValuesEntry', (_message.Message,), dict(
    DESCRIPTOR = _DEMOMESSAGE_B3VALUESENTRY,
    __module__ = 'grpc_resources.grpc_demo_pb2'
    # @@protoc_insertion_point(class_scope:bramble.DemoMessage.B3ValuesEntry)
    ))
  ,
  DESCRIPTOR = _DEMOMESSAGE,
  __module__ = 'grpc_resources.grpc_demo_pb2'
  # @@protoc_insertion_point(class_scope:bramble.DemoMessage)
  ))
_sym_db.RegisterMessage(DemoMessage)
_sym_db.RegisterMessage(DemoMessage.B3ValuesEntry)


_DEMOMESSAGE_B3VALUESENTRY.has_options = True
_DEMOMESSAGE_B3VALUESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_DEMOSERVICE = _descriptor.ServiceDescriptor(
  name='DemoService',
  full_name='bramble.DemoService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=162,
  serialized_end=232,
  methods=[
  _descriptor.MethodDescriptor(
    name='DemoRPC',
    full_name='bramble.DemoService.DemoRPC',
    index=0,
    containing_service=None,
    input_type=_DEMOMESSAGE,
    output_type=_DEMOMESSAGE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEMOSERVICE)

DESCRIPTOR.services_by_name['DemoService'] = _DEMOSERVICE

# @@protoc_insertion_point(module_scope)