# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: status.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from type import servericon_pb2 as type_dot_servericon__pb2
from type import updatestatus_pb2 as type_dot_updatestatus__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cstatus.proto\x12\rjijidown.core\x1a\x1bgoogle/protobuf/empty.proto\x1a\x15type/servericon.proto\x1a\x17type/updatestatus.proto\"m\n\x0eStatusPingPong\x12\x13\n\x0bserver_name\x18\x01 \x01(\t\x12.\n\x07os_icon\x18\x02 \x01(\x0e\x32\x1d.jijidown.core.ServerIconType\x12\x16\n\x0eos_system_name\x18\x03 \x01(\t\"]\n\x16StatusCheckUpdateReply\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.jijidown.core.UpdateStatusType\x12\x12\n\nchange_log\x18\x02 \x01(\t2\x97\x01\n\x06Status\x12=\n\x04Ping\x12\x16.google.protobuf.Empty\x1a\x1d.jijidown.core.StatusPingPong\x12N\n\x0b\x43heckUpdate\x12\x16.google.protobuf.Empty\x1a%.jijidown.core.StatusCheckUpdateReply0\x01\x42IZ3github.com/JiJiDown/JiJiDownCore-go/common/jijidown\xaa\x02\x11JiJiDown.Core.SDKb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'status_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/JiJiDown/JiJiDownCore-go/common/jijidown\252\002\021JiJiDown.Core.SDK'
  _globals['_STATUSPINGPONG']._serialized_start=108
  _globals['_STATUSPINGPONG']._serialized_end=217
  _globals['_STATUSCHECKUPDATEREPLY']._serialized_start=219
  _globals['_STATUSCHECKUPDATEREPLY']._serialized_end=312
  _globals['_STATUS']._serialized_start=315
  _globals['_STATUS']._serialized_end=466
# @@protoc_insertion_point(module_scope)