import subprocess
import inspect
from inspect import Parameter
import shutil

def only_required_kwargs_call(f, *args, **kwargs):
    sig = inspect.signature(f)
    of_type = lambda type: [name for name, param in sig.parameters.items()
                if param.kind == type
               ]
    pos = of_type(Parameter.kind.POSITIONAL_OR_KEYWORD)
    #_args = of_type( Parameter.kind.VAR_KEYWORD)
    keyw = of_type(Parameter.kind.KEYWORD_ONLY)
    _kwargs = of_type(Parameter.kind.VAR_KEYWORD)
    if len(_kwargs):
        return f(*args, **kwargs)
    else:
        names = pos + keyw
        conf = {name:value for 
                name, value in kwargs if name in names
               }
        return f(*args, **conf)


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
        subprocess.run(' '.join([str(x) for x in cmds]),
                   shell=True, check=True
                  )
    except subprocess.CalledProcessError as e:
        output, stderr = e.output, e.stderr
        if output:
            output = output.decode()
        if stderr:
            stderr = stderr.decode()
        raise Exception(f"Failed to execute `{cmds[0]}`.\n\
 Command: {e.cmd}.\n\
 Output: {output}")
