f = open('data_file.txt')
file_stuff = f.read()
args = [p.strip() for p in file_stuff.splitlines()]
f.close()

PID = []
arrival_time = []
priority = []
C_burst = []
I_burst = []



for i in range(0, len(args)):
    print(args[i])
