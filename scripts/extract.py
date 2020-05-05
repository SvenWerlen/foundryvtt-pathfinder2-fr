#!/usr/bin/python3
# -*- coding: utf-8 -*-

ROOT="../"
FILE=ROOT + "packs/actions.db"

import json

# read file
with open(FILE, 'r') as f:
  content = f.readlines()


for line in content:
  obj = json.loads(line)
  
  with open(ROOT + 'data/actions/' + obj['_id'] + ".htm", 'w') as df:
    df.write('Name: ' + obj['name'] + '\n')
    df.write('Nom: ' + '\n')
    df.write('État: aucune\n\n')
    df.write('------ Description (en) ------' + '\n')
    df.write(obj['data']['description']['value'] + '\n')
    df.write('------ Description (fr) ------' + '\n')
