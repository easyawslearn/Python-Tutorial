import subprocess

logile="subprocess.log"
def subprocess_cmd(command):
    print (command)
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    with open(logile,'w') as f:
        f.writelines(proc_stdout.split('  '))
    return logile

subprocess_cmd("uname")
