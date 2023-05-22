#!/bin/bash

CURRENT_PATH=$(pwd)
SRC_PATH="$CURRENT_PATH/src"
GLOBAL_PATH="$SRC_PATH:\$PATH"
FILE_PATH="$SRC_PATH/urban.py"
EXEC_PATH="$HOME/.local/bin/urban"
LOG_FILE="$CURRENT_PATH/logs/traceback.log"
RC_FILE="$HOME/.bashrc"

reload_rc_file() {
	echo "Reloading file information..."
    source $RC_FILE
}

is_first_time_install() {
	echo "Checking first time installation"
	if [[ ":$PATH:" == *":$CURRENT_PATH:"* ]]; then
		return 1
	else
		return 0
	fi
}

exec_file_is_created() {
	echo "Checking validity of executable at $EXEC_PATH"
}

create_exec_symlink() {
    echo "Making a locally executable alias"
    ln -s $FILE_PATH $EXEC_PATH 2>> $LOG_FILE
}

fail_and_exit() {
    echo "Error: Failed to modify $RC_FILE. Please update it manually."
    cat $LOG_FILE
    rm $LOG_FILE
    exit 1
}

if ! is_first_time_install; then
	echo "Warning: Installation cannot be done twice"
	exit 0
fi

echo export "PATH=$GLOBAL_PATH" >> $RC_FILE 2> $LOG_FILE

if [[ $? -eq 0 ]]; then
	echo "Changing local file permissions for $FILE_PATH"
	chmod +x $FILE_PATH
else
	fail_and_exit
fi

create_exec_symlink

if [[ $? -eq 0 ]]; then
	echo "Installation complete! 🎉"
	source $RC_FILE # Final reload of file
	exit 0
else
	echo "Invalid permissions to $EXEC_PATH: try running installer w/ sudo"
	fail_and_exit
fi

