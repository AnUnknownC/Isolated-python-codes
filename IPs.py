def ips_between(start, end):
    start = start.split(".")
    end = end.split(".")
    num = (int(end[0]) - int(start[0]))*256**3 + (int(end[1]) - int(start[1]))*256**2 + (int(end[2]) - int(start[2]))*256 + (int(end[3]) - int(start[3]))
    return num

print(ips_between("20.0.0.10", "20.0.1.0"))