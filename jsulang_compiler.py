import sys

class JSULangInterpreter:
    def __init__(self, code):
        self.memory = [0] * 59049
        self.ptr = 0
        self.code = code
        self.charset = "jsu !?&$@;_"
        self.output = []

    def execute(self):
        i = 0
        while i < len(self.code):
            char = self.code[i]
            if char == 'j':
                self.memory[self.ptr] = (self.memory[self.ptr] + 1) % 256
            elif char == 's':
                self.memory[self.ptr] = (self.memory[self.ptr] - 1) % 256
            elif char == 'u':
                self.ptr = (self.ptr + 1) % len(self.memory)
            elif char == 'l':
                self.ptr = (self.ptr - 1) % len(self.memory)
            elif char == '!':
                self.output.append(chr(self.memory[self.ptr]))
            elif char == '?':
                self.memory[self.ptr] = ord(input("Input a character: ")[0])
            elif char == '&':
                self.memory[self.ptr] ^= 255
            elif char == '$':
                self.memory[self.ptr] = (self.memory[self.ptr] * 2) % 256
            elif char == '@':
                self.memory = self.memory[1:] + [self.memory[0]]
            elif char == ';':
                self.memory[self.ptr] = int(self.memory[self.ptr] / 2)
            elif char == '_':
                self.code = (
                    self.code[:i]
                    + self.charset[self.memory[self.ptr] % len(self.charset)]
                    + self.code[i + 1:]
                )
            i += 1
        print("".join(self.output))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python jsulang_compiler.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, "r") as file:
        code = file.read()

    interpreter = JSULangInterpreter(code)
    interpreter.execute()