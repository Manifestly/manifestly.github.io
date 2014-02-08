#!/usr/bin/env python

import os
import shutil

def remove_all(root, exceptions):
  to_delete = [name for name in os.listdir(root) if name not in exceptions]
  for name in to_delete:
    path = os.path.normpath(os.path.join(root, name))
    if os.path.isfile(path):
      os.remove(path)
    else:
      shutil.rmtree(path)

def main():
  exceptions = ['.git', 'build', 'update.py', 'CNAME', '.gitignore']
  root = '.'
  remove_all(root, exceptions)

  os.system('mv build/* .')

if __name__ == '__main__':
  main()
