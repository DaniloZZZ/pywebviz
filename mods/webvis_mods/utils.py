import subprocess
import os

def copy(src, dest):
    print("copy", src, dest)
    if src.is_dir():
        src = str(src) + str(os.sep)
    run_cmd(['rsync','-r', src, dest])

def write_to(s, dest):
    with open(dest, 'w+') as f:
        f.write(s)

def run_cmd(cmds):
    try:
        subprocess.check_output(' '.join([str(x) for x in cmds]),
                   shell=True,
                  )
    except subprocess.CalledProcessError as e:
        output, stderr = e.output, e.stderr
        if output:
            output = output.decode()
        if stderr:
            stderr = stderr.decode()
        raise Exception(f"Failed to execute.\n!!Command: {e.cmd}.\n!!Output: {output}.\n!!Error: {stderr}")
