# coding: utf-8
from pathlib import Path
pathname = "pet-clinic"
path = Path(pathname)
path
path.resolve()
list(path.iterdir())
get_ipython().run_line_magic('ls', 'pet-clinic')
path.is_dir()
path.is_file()
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p)
        
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p.as_posix())
        
        
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p.as_posix())
        
        
handle_directory(path)
pathname = "/home/ec2-user/code/AWS-AUTOMATION-WITH-PYTHON/01-webotron/pet-clinic/"
path = Path(pathname)
path.expanduser()
handle_directory(path.expanduser())
path
root = pathname
path.relative_to(root)
path = Path('/home/ec2-user/code/AWS-AUTOMATION-WITH-PYTHON/01-webotron/pet-clinic/images/slide-1.jpg')
path.relative_to(root)
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print("Path: {}\n Key: {}".format(p, p.relative_to(root)))
        
       
        
handle_directory(Path(root))
get_ipython().run_line_magic('history', '')
