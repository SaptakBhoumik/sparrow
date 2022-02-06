import os
from os import path
def system(cmd):
    print(cmd)
    os.system(cmd)
import platform
bin_name="sparrow"
if platform.system()=="Windows":
    bin_name+=".exe"
bf=["sparrow/bf/libbf.cpp"]
quickjs=["sparrow/quickjs/quickjs.cpp"]
quickjs_libc=["sparrow/quickjs_libc/quickjs_libc.cpp"]
regexp=["sparrow/regexp/libregexp.cpp"]
unicode=["sparrow/unicode/libunicode.cpp"]
utils=["sparrow/utils/utils.cpp"]
main=["sparrow/main.cpp"]
files=[
    bf,
    quickjs,
    quickjs_libc,
    regexp,
    unicode,
    utils,
    main
]
cpp_compiler="clang++"#only works with clang at this moment
cargs="-Wc99-designator -w"
libs=[
    'm', 
    'dl',
    'pthread'
]
obj=[]
buildir="buildir"
system(f"mkdir -p {buildir}")
modified=False
for x in files:
    for y in x:
        obj_name=y.replace("/","_").replace(".cpp",".o")
        obj.append(obj_name)
        if path.exists(f"{buildir}/{obj_name}"):
            if path.getmtime(y)>path.getmtime(f"{buildir}/"+obj_name):
                modified=True
                system(f"{cpp_compiler} -c {cargs} {y} -o {buildir}/{obj_name}")
        else:
            modified=True
            system(f"{cpp_compiler} -c {cargs} {y} -o {buildir}/{obj_name}")
if modified==True:
    cmd=f"{cpp_compiler} {cargs}"
    for x in obj:
        cmd+=f" {buildir}/{x}"
    for x in libs:
        cmd+=f" -l{x}"
    cmd+=f" -o {buildir}/{bin_name}"
    system(cmd)
else:
    print("No changes detected, skipping build")
    