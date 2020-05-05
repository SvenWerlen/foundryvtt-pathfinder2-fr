#!/usr/bin/python3
# -*- coding: utf-8 -*-

BABELE="../babele/fr/"

TRANSL={
  'pf2e.actionspf2e': { 'label': "Actions", 'path': "../data/actions/" }
}

import json
import os             

for key in TRANSL: 
  path = TRANSL[key]['path']
  all_files = os.listdir(path)

  data = { 
    'label': TRANSL[key]['label'],
    'entries': []
  }


  # read all files in folder
  for fpath in all_files:
    
    # read all lines in f
    with open(path + fpath, 'r') as f:
      content = f.readlines()
    
    nameEN = ""
    nameFR = ""
    descr = ""
    status = ""
    isDesc = False  
    
    for line in content:
      if isDesc:
        descr += line
      elif line.startswith("Name:"):
        nameEN = line[5:].strip()
      elif line.startswith("Nom:"):
        nameFR = line[4:].strip()
      elif line.startswith("État:"):
        status = line[5:].strip()
      elif line.startswith("------ Description (fr) ------"):
        isDesc = True
    
    if len(nameEN) == 0 or (len(nameFR) == 0 and len(descr.replace('\n','').strip()) == 0):
      continue
    
    entry = { 'id': nameEN }
    if len(nameFR) > 0:
      entry['name'] = nameFR
    if len(descr.replace('\n','').strip()) > 0:
      entry['description'] = descr
    data['entries'].append(entry)
        

  with open(BABELE + key + ".json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
