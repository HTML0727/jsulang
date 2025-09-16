# JSULang

JSULang is an esoteric programming language inspired by Malbolge. It uses the following character set:
- `j, s, u, l, !, ?, &, $, @, ;, _`

## Files
- `header.jsuh`: Metadata for the program.
- `hello_world.jsul`: A "Hello, World!" program written in JSULang.

## Instructions
JSULang code is interpreted by a Malbolge-like self-modifying compiler. To run the example program:
```bash
python jsulang_compiler.py hello_world.jsul```