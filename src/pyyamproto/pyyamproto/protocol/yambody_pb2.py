# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yambody.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yambody.proto',
  package='',
  serialized_pb='\n\ryambody.proto\":\n\x0eYamMessageBody\x12(\n\x0cmessage_type\x18\x01 \x02(\x0e\x32\x0c.MessageType:\x04NONE*\x17\n\x0bMessageType\x12\x08\n\x04NONE\x10\x00')

_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=77,
  serialized_end=100,
)

MessageType = enum_type_wrapper.EnumTypeWrapper(_MESSAGETYPE)
NONE = 0



_YAMMESSAGEBODY = _descriptor.Descriptor(
  name='YamMessageBody',
  full_name='YamMessageBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='YamMessageBody.message_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=17,
  serialized_end=75,
)

_YAMMESSAGEBODY.fields_by_name['message_type'].enum_type = _MESSAGETYPE
DESCRIPTOR.message_types_by_name['YamMessageBody'] = _YAMMESSAGEBODY

class YamMessageBody(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _YAMMESSAGEBODY

  # @@protoc_insertion_point(class_scope:YamMessageBody)


# @@protoc_insertion_point(module_scope)