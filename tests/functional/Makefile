#
# Copyright(c) 2019 Intel Corporation
# SPDX-License-Identifier: BSD-3-Clause-Clear
#

PWD=$(shell pwd)
OCFDIR=$(PWD)/../../
ADAPTERDIR=$(PWD)/pyocf
SRCDIR=$(ADAPTERDIR)/ocf/src
INCDIR=$(ADAPTERDIR)/ocf/include
WRAPDIR=$(ADAPTERDIR)/wrappers

CC=gcc
CFLAGS=-g -Wall -I$(INCDIR) -I$(SRCDIR)/ocf/env
LDFLAGS=-pthread -lz

SRC=$(shell find $(SRCDIR) $(WRAPDIR) -name \*.c)
OBJS=$(patsubst %.c, %.o, $(SRC))
OCFLIB=$(ADAPTERDIR)/libocf.so

all: | sync
	$(MAKE) $(OCFLIB)

$(OCFLIB): $(OBJS)
	@echo "Building $@"
	@$(CC) -shared -o $@ $(CFLAGS) $^ -fPIC $(LDFLAGS)

%.o: %.c
	@echo "Compiling $@"
	@$(CC) -c $(CFLAGS) -o $@ -fPIC $^ $(LDFLAGS)

sync:
	@echo "Syncing OCF sources"
	@mkdir -p $(ADAPTERDIR)/ocf
	@$(MAKE) -C $(OCFDIR) inc O=$(ADAPTERDIR)/ocf
	@$(MAKE) -C $(OCFDIR) src O=$(ADAPTERDIR)/ocf
	@$(MAKE) -C $(OCFDIR) env O=$(ADAPTERDIR)/ocf ENV=posix

clean:
	@rm -rf $(OCFLIB) $(OBJS)
	@echo "  CLEAN "

distclean: clean
	@rm -rf $(OCFLIB) $(OBJS)
	@rm -rf $(SRCDIR)/ocf
	@rm -rf $(INCDIR)/ocf
	@echo "  DISTCLEAN "

.PHONY: all clean sync distclean
