# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mypy_protobuf/extensions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1emypy_protobuf/extensions.proto\x12\rmypy_protobuf\x1a google/protobuf/descriptor.proto\"D\n\x0c\x46ieldOptions\x12\x10\n\x08\x63\x61sttype\x18\x01 \x01(\t\x12\x0f\n\x07keytype\x18\x02 \x01(\t\x12\x11\n\tvaluetype\x18\x03 \x01(\t:M\n\x07options\x12\x1d.google.protobuf.FieldOptions\x18\xe4\xd4\x03 \x01(\x0b\x32\x1b.mypy_protobuf.FieldOptions:5\n\x08\x63\x61sttype\x12\x1d.google.protobuf.FieldOptions\x18\xe0\xd4\x03 \x01(\tB\x02\x18\x01:4\n\x07keytype\x12\x1d.google.protobuf.FieldOptions\x18\xe2\xd4\x03 \x01(\tB\x02\x18\x01:6\n\tvaluetype\x12\x1d.google.protobuf.FieldOptions\x18\xe3\xd4\x03 \x01(\tB\x02\x18\x01\x62\x06proto3')


OPTIONS_FIELD_NUMBER = 60004
options = DESCRIPTOR.extensions_by_name['options']
CASTTYPE_FIELD_NUMBER = 60000
casttype = DESCRIPTOR.extensions_by_name['casttype']
KEYTYPE_FIELD_NUMBER = 60002
keytype = DESCRIPTOR.extensions_by_name['keytype']
VALUETYPE_FIELD_NUMBER = 60003
valuetype = DESCRIPTOR.extensions_by_name['valuetype']

_FIELDOPTIONS = DESCRIPTOR.message_types_by_name['FieldOptions']
FieldOptions = _reflection.GeneratedProtocolMessageType('FieldOptions', (_message.Message,), {
  'DESCRIPTOR' : _FIELDOPTIONS,
  '__module__' : 'mypy_protobuf.extensions_pb2'
  # @@protoc_insertion_point(class_scope:mypy_protobuf.FieldOptions)
  })
_sym_db.RegisterMessage(FieldOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(options)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(casttype)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(keytype)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(valuetype)

  DESCRIPTOR._options = None
  casttype._options = None
  casttype._serialized_options = b'\030\001'
  keytype._options = None
  keytype._serialized_options = b'\030\001'
  valuetype._options = None
  valuetype._serialized_options = b'\030\001'
  _FIELDOPTIONS._serialized_start=83
  _FIELDOPTIONS._serialized_end=151
# @@protoc_insertion_point(module_scope)