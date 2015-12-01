DESTDIR ?=

TARGET = perlcrc32
CC = gcc
CFLAGS = -fPIC -Wall -Wextra -O3
LDFLAGS = -shared
RM = rm -f
TARGET_LIB = lib$(TARGET).so

SRCS = perl_crc32.c
OBJS = $(SRCS:.c=.o)

HEADERS = perl_crc32.h

.PHONY: all so
all: ${TARGET_LIB}

so: all

install_headers:
	-mkdir -p $(DESTDIR)
	$(foreach f,$(HEADERS),cp $(f) $(DESTDIR)/$(f);)

${TARGET_LIB}: ${OBJS}
	$(CC) ${LDFLAGS} -o $@ $^

.PHONY: clean
clean:
	-${RM} ${TARGET_LIB} ${OBJS}
