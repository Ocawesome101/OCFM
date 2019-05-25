#!/usr/bin/env python3.5
#  _____     _____   _______  __    __
# /OOOOO\   /CCCCC\  |FFFFFF||MM\  /MM|
#/O/   \O\ /C/   \C\ |F|___  |M\M\/M/M|
#|O|   |O| |C|       |FFFFF| |M|\MM/|M|
#|O|   |O| |C|       |F|     |M| \/ |M|
#\O\___/O/ \C\___/C/ |F|     |M|    |M|
# \OOOOO/   \CCCCC/  |F|     |M|    |M|
#
#OC File Manager
#
#Sorry for the bad ASCII art.
#
#OCFM attempt 2 - the "command line" way. Made with Python 3.5 to interface
#with Bash. This is strictly command-line and somewhat Vi-like.
#Hopefully this goes better than my first attempt, which was a MESS.
#
#This program will require VLC Media Player and the Mousepad text editor to work
#to its full extent.

from os import system
CurrentDir = '/'
system('ls ' + CurrentDir)
print('OCFM 2.0. Type \':\' before commands.')
while 1:
    command = input('')
    if command == ':q' or command == ':quit' or command == ':exit':
        exit()
    elif command == ':/':
        CurrentDir = '/'
    elif command == ':h' or command == ':help':
        print('OCFM Help\nCommands:\n:q or :quit or :exit - exit OCFM\n:/ - Return to the root directory\n <Directory Name> - Move to that directory\n:delete <file> - delete a file. Will ask for confirmation.')
    elif command[0:7] == ':delete':
        command = command[8:len(command)]
        delete = input('Are you sure you want to delete file ' + command + '? (y/n)')
        if delete == 'y':
            system('rm -r ' + command)
        elif delete == 'n':
            print('Aborting')
        elif delete != 'y' and delete != 'n':
            print('Aborting - you did not type Y or N.')
    elif command[0:6] == ':mkdir':
        command = command[7:len(command)]
        system('mkdir ' + command)
    elif command[0] != ':':
        CurrentDir += command + '/'
    elif command[0] == ':':
        print('UNRECOGNIZED COMMAND - RETURNING TO ROOT DIRECTORY')
        CurrentDir = '/'
    system('ls ' + CurrentDir)
