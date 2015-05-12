YAMPROTODIR = ../yamproto
YAMPKGDIR = pyyamproto/protocol/

PROTO_SRC := yambody.proto yam.proto shard.proto user.proto 
PROTO_PY := $(addprefix $(YAMPKGDIR),$(patsubst %.proto,%_pb2.py,$(PROTO_SRC)))
DISTFILES := pyyamproto.protocol.egg-info build dist	

$(YAMPKGDIR)%_pb2.py: $(YAMPROTODIR)/%.proto
	protoc --proto_path=$(YAMPROTODIR) --python_out=pyyamproto/protocol $<

proto: $(PROTO_PY)

sdist: $(PROTO_PY)
	python setup.py sdist

dist: $(PROTO_PY)
	python setup.py bdist
dist-egg: $(PROTO_PY)
	python setup.py bdist_egg
dist-rpm: $(PROTO_PY)
	python setup.py bdist_rpm
all: proto

clean-py:
	rm -rf $(PROTO_PY)
dist-clean:
	rm -rf $(DISTFILES)
clean: clean-py
