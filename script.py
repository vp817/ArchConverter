import sys
import os
import lief

def turn(src: str, dst: str = None):
    binary = lief.parse(src)
    binary.header.machine_type = lief.ELF.ARCH.x86_64
    binary.write(dst if (dst is None) or (isinstance(dst, str) and len(str) < 4) else os.path.splitext(dst, str)[1] + "_x86_64")

if len(sys.argv) < 2:
    print("Usage: " + ("python3" if "linux" in sys.platform else "python") + " <file_to_turn_path> <destination_of_turned_file: Optional>")
    exit()

turn(sys.argv[1], sys.argv[2] if len(sys.argv) >= 3 else None)
