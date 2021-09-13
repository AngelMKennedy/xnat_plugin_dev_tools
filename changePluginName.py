#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
from subprocess import call

def renameDirs(folder_path,oldOrg="Template",newOrg="Aisperth",oldDataType="Sample",newDataType="Spect"):
  for path, subdirs, files in os.walk(folder_path):
    for name in subdirs:
      name2=name
      if(oldOrg in name):
        name2=name.replace(oldOrg,newOrg)
        file_path = os.path.join(path,name)
        new_name = os.path.join(path,name2)
        print("os.rename("+file_path+", "+new_name+")")
        os.rename(file_path,new_name)
      if(oldDataType in name):
        file_path = os.path.join(path,name2)
        new_name = os.path.join(path,name2.replace(oldDataType,newDataType))
        print("os.rename("+file_path+", "+new_name+")")
        os.rename(file_path,new_name)

def runUpdate(plugin="aisperth",datatype="spect",dir="src",oldPlug="template",oldDT="sample"):
  updateFiles(dir,oldPlug.capitalize(),plugin.capitalize(),oldDT.capitalize(),datatype.capitalize())
  updateFiles(dir,oldPlug,plugin,oldDT,datatype)
  updateFiles(dir,"Jdbc"+plugin.capitalize(),"Jdbc"+oldPlug.capitalize(),"doBuild"+plugin.capitalize(),"doBuild"+oldPlug.capitalize()) 
  renameDirs(dir,oldPlug.capitalize(),plugin.capitalize(),oldDT.capitalize(),datatype.capitalize())
  renameDirs(dir,oldPlug,plugin,oldDT,datatype)
  renameDirs(dir,plugin+"s",oldPlug+"s","nonsense","nonsense")


def updateFiles(folder_path,oldOrg="Template",newOrg="Aisperth",oldDataType="Sample",newDataType="Spect"):
  for path, subdirs, files in os.walk(folder_path):
    for name in files:
      file_path = os.path.join(path,name)
      print("file: "+name)
      replaceStrings(file_path,oldOrg,newOrg)
      replaceStrings(file_path,oldDataType,newDataType)
      name2=name
      if(oldOrg in name):
        name2 = name.replace(oldOrg,newOrg)
        new_name = os.path.join(path,name2)
        os.rename(file_path, new_name)
        file_path = new_name
      if(oldDataType in name):
        new_name =  os.path.join(path,name2.replace(oldDataType,newDataType))
        os.rename(file_path, new_name)

def replaceStrings(fileName,old,new):
  argStr="-i s/"+old+"/"+new+"/g "+fileName
  runCmd("sed "+argStr)

def runCmd(sCmd,stdOutFile=None):
  print(" ")
  print(sCmd)
  print(" ")
  lcmd=sCmd.split()
  if stdOutFile==None:
    call(lcmd)
  else:
    with open(stdOutFile, 'w') as fp:
      call(lcmd,stdout=fp, stderr=fp)
  
