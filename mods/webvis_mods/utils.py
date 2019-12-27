import subprocess
import shutil
import os

def rm(obj):
    if obj.is_symlink():
        os.unlink(obj)
    elif obj.is_dir():
        shutil.rmtree(obj)
    elif obj.is_file():
        os.remove(obj)


def copy(src, dest):
    print("cp", src, dest)
    if src.is_dir():
        src = str(src) + str(os.sep)
    run_cmd(['rsync','-r', src, dest])

def ln(src, dest):
    print("ln -sf", src, dest)
    if src.is_dir():
        src = str(src) + str(os.sep)
    run_cmd(['ln','-s', src, dest])

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
