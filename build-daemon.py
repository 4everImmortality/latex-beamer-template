#!/usr/bin/env python3
import os
import sys
import time
import subprocess

def build():
    print("Building slides...")
    result = subprocess.run(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print("Build succeeded.")
    else:
        print("Build failed:\n", result.stderr.decode())

def watch(paths, interval=1):
    mtimes = {}
    for path in paths:
        if os.path.exists(path):
            mtimes[path] = os.path.getmtime(path)
    while True:
        changed = False
        for path in paths:
            if os.path.exists(path):
                mtime = os.path.getmtime(path)
                if mtimes.get(path, 0) != mtime:
                    mtimes[path] = mtime
                    changed = True
        if changed:
            build()
        time.sleep(interval)

if __name__ == "__main__":
    watch_files = ["slides.tex", "Makefile", "style/beamercolorthememit.sty"]
    print("Watching for changes in:", ", ".join(watch_files))
    build()
    watch(watch_files)