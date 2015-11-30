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

.PHONY: all so
all: ${TARGET_LIB}

so: all

${TARGET_LIB}: ${OBJS}
	$(CC) ${LDFLAGS} -o $@ $^

.PHONY: clean
clean:
	-${RM} ${TARGET_LIB} ${OBJS}
