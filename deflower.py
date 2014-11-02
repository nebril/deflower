import sys
import subprocess

switches_filename = 'switches.txt'

if len(sys.argv) > 1:
    switches_filename = sys.argv[1]



with open(switches_filename) as f:
    switches = [x.strip('\n') for x in f.readlines()] 

for switch in switches:
    output = subprocess.check_output(['dpctl', 'dump-flows', switch])
    flows = output.split('\n')[1:-1]
    print flows
