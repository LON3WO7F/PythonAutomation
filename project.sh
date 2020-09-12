#!/bin/bash


function create(){

       cd 
       new.py $1
       cd /media/gourav/DarkStar1/VisualStudio/Python/automation
       mkdir $1 
       cd $1 
       git init
       git remote add origin git+ssh://git@github.com:LON3WO7F/$1.git
       touch README.md
       git add .
       git commit -m "Initial Commmit"
       git push -u origin master


}
