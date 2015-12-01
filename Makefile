DESTDIR ?=
DESTPATH = ${DESTDIR}/usr/local/lib

TARGET = perlcrc32
CC = gcc
CFLAGS = -fPIC -Wall -Wextra -O3
LDFLAGS = -shared
RM = rm -f
TARGET_LIB = lib$(TARGET).so

SRCS = crc32.c
OBJS = $(SRCS:.c=.o)

HEADERS = crc32.h
COMMA = ,

.PHONY: all so
all: ${TARGET_LIB}

so: all

install_headers:
	#-cp {$(subst $(COMMA),:,$(HEADERS))} $(DESTDIR)
	-mkdir -p $(DESTDIR)
	-cp $(HEADERS) $(DESTDIR)

${TARGET_LIB}: ${OBJS}
	$(CC) ${LDFLAGS} -o $@ $^

.PHONY: clean
clean:
	-${RM} ${TARGET_LIB} ${OBJS}
