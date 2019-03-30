#!/bin/sh
if [$# -eq 2] then
  echo "installation des bibliotheques"
  if [$3 = "3"] then
    exec "pip3 install pip CherryPy --upgrade"
  else
    exec "pip install pip CherryPy --upgrade"
  fi
else
  return true
fi
