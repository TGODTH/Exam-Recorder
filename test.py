import datetime
import msvcrt

print(ord("A"))
print(ord("B"))
print(ord("C"))
print(ord("D"))
print(ord("E"))
print(ord("1"))
print(ord("2"))
print(ord("3"))
print(ord("4"))
print(ord("5"))
print(ord("a"))
print(ord("b"))
print(ord("c"))
print(ord("d"))
print(ord("e"))

delta = datetime.timedelta(seconds=100, microseconds=431259)
delta_str = str(delta)

print(delta_str.split(".")[0])

# print(f"input: {msvcrt.getch().decode('utf-8')}")