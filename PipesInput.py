from base64 import b16encode
import subprocess
import sys
#proc = subprocess.Popen(["python", "ExampleScript.py "])

# while proc.returncode is None:
#     proc.poll()

proc = subprocess.Popen(["python", "ExampleScript.py "], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# proc.stdin.write("Alex\n".encode("utf-8"))
# proc.stdin.write("Jhon\n".encode("utf-8"))
byte = proc.communicate("hello".encode("utf-8"))

# byte = proc.stdout.read()
print(byte[0].decode("utf-8"))


print ("I am back from the child program this:\n{0}".format(byte[0].decode("utf-8")))