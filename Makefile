SOURCE = magic/sqrt.c
OUT    = magic/sqrt.dylib
CC     = gcc
FLAGS  = -Wall -Werror -O2 -shared -fno-builtin-sqrt

all:
	gcc $(FLAGS) $(SOURCE) -o $(OUT)

plot:
	python3 plot.py

run:
	python3 find.py --start $(start)

clean:
	rm -f $(OUT)
