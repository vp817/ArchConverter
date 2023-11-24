import sys
import os
import lief

def turn(src: str, dst: str = None):
    binary = lief.parse(src)
    binary.header.machine_type = lief.ELF.ARCH.x86_64
    if dst is None or (isinstance(dst, str) and len(dst) < 4):
        srcPts = os.path.splitext(src)
        dst = srcPts[0] + "_x86_64" + srcPts[1]
    else:
        dstPts = os.path.splitext(dst)
        dst = dstPts[0] + "_x86_64" + dstPts[1]
    binary.write(dst)

if len(sys.argv) < 2:
    print("Usage: " + ("python3" if "linux" in sys.platform else "python") + " <file_to_turn_path> <destination_of_turned_file: Optional>")
    exit()

turn(sys.argv[1], sys.argv[2] if len(sys.argv) >= 3 else None)
