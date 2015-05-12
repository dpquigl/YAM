# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shard.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='shard.proto',
  package='',
  serialized_pb='\n\x0bshard.proto\"\xc9\x02\n\x0cShardRequest\x12,\n\x04type\x18\x01 \x02(\x0e\x32\x1e.ShardRequest.ShardMessageType\x12-\n\x0frestart_request\x18\x02 \x01(\x0b\x32\x14.RestartShardRequest\x12\'\n\x0cstop_request\x18\x03 \x01(\x0b\x32\x11.StopShardRequest\x12+\n\x0estatus_request\x18\x04 \x01(\x0b\x32\x13.ShardStatusRequest\x12-\n\x12shard_list_request\x18\x05 \x01(\x0b\x32\x11.ShardListRequest\"W\n\x10ShardMessageType\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07RESTART\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\n\n\x06STATUS\x10\x03\x12\x08\n\x04LIST\x10\x04\x12\x0c\n\x08SHUTDOWN\x10\x05\"\xb5\x02\n\nShardReply\x12*\n\x04type\x18\x01 \x02(\x0e\x32\x1c.ShardReply.ShardMessageType\x12)\n\rrestart_reply\x18\x02 \x01(\x0b\x32\x12.RestartShardReply\x12#\n\nstop_reply\x18\x03 \x01(\x0b\x32\x0f.StopShardReply\x12\'\n\x0cstatus_reply\x18\x04 \x01(\x0b\x32\x11.ShardStatusReply\x12)\n\x10shard_list_reply\x18\x05 \x01(\x0b\x32\x0f.ShardListReply\"W\n\x10ShardMessageType\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07RESTART\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\n\n\x06STATUS\x10\x03\x12\x08\n\x04LIST\x10\x04\x12\x0c\n\x08SHUTDOWN\x10\x05\"\'\n\x13RestartShardRequest\x12\x10\n\x08shard_id\x18\x01 \x02(\x05\"#\n\x11RestartShardReply\x12\x0e\n\x06status\x18\x01 \x02(\x05\"3\n\x10StopShardRequest\x12\x10\n\x08shard_id\x18\x01 \x02(\x05\x12\r\n\x05\x66lags\x18\x02 \x02(\x05\" \n\x0eStopShardReply\x12\x0e\n\x06status\x18\x01 \x02(\x05\"&\n\x12ShardStatusRequest\x12\x10\n\x08shard_id\x18\x01 \x02(\x05\"\"\n\x10ShardStatusReply\x12\x0e\n\x06status\x18\x01 \x02(\x05\"\x12\n\x10ShardListRequest\"\x86\x01\n\x0eShardListReply\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12-\n\nshard_data\x18\x02 \x03(\x0b\x32\x19.ShardListReply.ShardData\x1a\x35\n\tShardData\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0e\n\x06status\x18\x02 \x02(\t\x12\n\n\x02id\x18\x03 \x02(\x05')



_SHARDREQUEST_SHARDMESSAGETYPE = _descriptor.EnumDescriptor(
  name='ShardMessageType',
  full_name='ShardRequest.ShardMessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESTART', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=258,
  serialized_end=345,
)

_SHARDREPLY_SHARDMESSAGETYPE = _descriptor.EnumDescriptor(
  name='ShardMessageType',
  full_name='ShardReply.ShardMessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESTART', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=258,
  serialized_end=345,
)


_SHARDREQUEST = _descriptor.Descriptor(
  name='ShardRequest',
  full_name='ShardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ShardRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='restart_request', full_name='ShardRequest.restart_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_request', full_name='ShardRequest.stop_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_request', full_name='ShardRequest.status_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shard_list_request', full_name='ShardRequest.shard_list_request', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SHARDREQUEST_SHARDMESSAGETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=16,
  serialized_end=345,
)


_SHARDREPLY = _descriptor.Descriptor(
  name='ShardReply',
  full_name='ShardReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ShardReply.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='restart_reply', full_name='ShardReply.restart_reply', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_reply', full_name='ShardReply.stop_reply', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_reply', full_name='ShardReply.status_reply', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shard_list_reply', full_name='ShardReply.shard_list_reply', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SHARDREPLY_SHARDMESSAGETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=348,
  serialized_end=657,
)


_RESTARTSHARDREQUEST = _descriptor.Descriptor(
  name='RestartShardRequest',
  full_name='RestartShardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shard_id', full_name='RestartShardRequest.shard_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=659,
  serialized_end=698,
)


_RESTARTSHARDREPLY = _descriptor.Descriptor(
  name='RestartShardReply',
  full_name='RestartShardReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='RestartShardReply.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=700,
  serialized_end=735,
)


_STOPSHARDREQUEST = _descriptor.Descriptor(
  name='StopShardRequest',
  full_name='StopShardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shard_id', full_name='StopShardRequest.shard_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='StopShardRequest.flags', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=737,
  serialized_end=788,
)


_STOPSHARDREPLY = _descriptor.Descriptor(
  name='StopShardReply',
  full_name='StopShardReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='StopShardReply.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=790,
  serialized_end=822,
)


_SHARDSTATUSREQUEST = _descriptor.Descriptor(
  name='ShardStatusRequest',
  full_name='ShardStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shard_id', full_name='ShardStatusRequest.shard_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=824,
  serialized_end=862,
)


_SHARDSTATUSREPLY = _descriptor.Descriptor(
  name='ShardStatusReply',
  full_name='ShardStatusReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ShardStatusReply.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=864,
  serialized_end=898,
)


_SHARDLISTREQUEST = _descriptor.Descriptor(
  name='ShardListRequest',
  full_name='ShardListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=900,
  serialized_end=918,
)


_SHARDLISTREPLY_SHARDDATA = _descriptor.Descriptor(
  name='ShardData',
  full_name='ShardListReply.ShardData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ShardListReply.ShardData.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='ShardListReply.ShardData.status', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='ShardListReply.ShardData.id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=1002,
  serialized_end=1055,
)

_SHARDLISTREPLY = _descriptor.Descriptor(
  name='ShardListReply',
  full_name='ShardListReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ShardListReply.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shard_data', full_name='ShardListReply.shard_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SHARDLISTREPLY_SHARDDATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=921,
  serialized_end=1055,
)

_SHARDREQUEST.fields_by_name['type'].enum_type = _SHARDREQUEST_SHARDMESSAGETYPE
_SHARDREQUEST.fields_by_name['restart_request'].message_type = _RESTARTSHARDREQUEST
_SHARDREQUEST.fields_by_name['stop_request'].message_type = _STOPSHARDREQUEST
_SHARDREQUEST.fields_by_name['status_request'].message_type = _SHARDSTATUSREQUEST
_SHARDREQUEST.fields_by_name['shard_list_request'].message_type = _SHARDLISTREQUEST
_SHARDREQUEST_SHARDMESSAGETYPE.containing_type = _SHARDREQUEST;
_SHARDREPLY.fields_by_name['type'].enum_type = _SHARDREPLY_SHARDMESSAGETYPE
_SHARDREPLY.fields_by_name['restart_reply'].message_type = _RESTARTSHARDREPLY
_SHARDREPLY.fields_by_name['stop_reply'].message_type = _STOPSHARDREPLY
_SHARDREPLY.fields_by_name['status_reply'].message_type = _SHARDSTATUSREPLY
_SHARDREPLY.fields_by_name['shard_list_reply'].message_type = _SHARDLISTREPLY
_SHARDREPLY_SHARDMESSAGETYPE.containing_type = _SHARDREPLY;
_SHARDLISTREPLY_SHARDDATA.containing_type = _SHARDLISTREPLY;
_SHARDLISTREPLY.fields_by_name['shard_data'].message_type = _SHARDLISTREPLY_SHARDDATA
DESCRIPTOR.message_types_by_name['ShardRequest'] = _SHARDREQUEST
DESCRIPTOR.message_types_by_name['ShardReply'] = _SHARDREPLY
DESCRIPTOR.message_types_by_name['RestartShardRequest'] = _RESTARTSHARDREQUEST
DESCRIPTOR.message_types_by_name['RestartShardReply'] = _RESTARTSHARDREPLY
DESCRIPTOR.message_types_by_name['StopShardRequest'] = _STOPSHARDREQUEST
DESCRIPTOR.message_types_by_name['StopShardReply'] = _STOPSHARDREPLY
DESCRIPTOR.message_types_by_name['ShardStatusRequest'] = _SHARDSTATUSREQUEST
DESCRIPTOR.message_types_by_name['ShardStatusReply'] = _SHARDSTATUSREPLY
DESCRIPTOR.message_types_by_name['ShardListRequest'] = _SHARDLISTREQUEST
DESCRIPTOR.message_types_by_name['ShardListReply'] = _SHARDLISTREPLY

class ShardRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHARDREQUEST

  # @@protoc_insertion_point(class_scope:ShardRequest)

class ShardReply(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHARDREPLY

  # @@protoc_insertion_point(class_scope:ShardReply)

class RestartShardRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESTARTSHARDREQUEST

  # @@protoc_insertion_point(class_scope:RestartShardRequest)

class RestartShardReply(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESTARTSHARDREPLY

  # @@protoc_insertion_point(class_scope:RestartShardReply)

class StopShardRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STOPSHARDREQUEST

  # @@protoc_insertion_point(class_scope:StopShardRequest)

class StopShardReply(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STOPSHARDREPLY

  # @@protoc_insertion_point(class_scope:StopShardReply)

class ShardStatusRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHARDSTATUSREQUEST

  # @@protoc_insertion_point(class_scope:ShardStatusRequest)

class ShardStatusReply(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHARDSTATUSREPLY

  # @@protoc_insertion_point(class_scope:ShardStatusReply)

class ShardListRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHARDLISTREQUEST

  # @@protoc_insertion_point(class_scope:ShardListRequest)

class ShardListReply(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class ShardData(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SHARDLISTREPLY_SHARDDATA

    # @@protoc_insertion_point(class_scope:ShardListReply.ShardData)
  DESCRIPTOR = _SHARDLISTREPLY

  # @@protoc_insertion_point(class_scope:ShardListReply)


# @@protoc_insertion_point(module_scope)
