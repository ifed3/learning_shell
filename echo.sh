#!/bin/sh

# Echo writes its arguments to stdout
# Shell parses the arguments before calling echo (strips out quotes)

# Predict what the echo outputs will be
echo "Hello World"
# Hello World
echo "Hello * World"
# Hello * World
echo Hello * World
# * might be a special character. Would expect to output Hello (sh *) World
echo Hello      World
# Hello World
echo "Hello" World
# Hello World
echo Hello "     " World
# Hello       World
echo "Hello "*" World"
# Hello * World
echo `hello` world
# Is the backtick a special character or also a quote? Output: hello world
echo 'hello' world
# hello world