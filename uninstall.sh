#!/bin/bash

CURRENT_PATH=$(pwd)
SRC_PATH="$CURRENT_PATH/src"
GLOBAL_PATH="$SRC_PATH:\$PATH"
FILE_PATH="$SRC_PATH/urban.py"
EXEC_PATH="$HOME/.local/bin/urban"
LOG_FILE="$CURRENT_PATH/logs/traceback.log"
RC_FILE="$HOME/.bashrc"

remove_alias() {
	echo "removing bash alias"
	sed -i '$ d' $RC_FILE
}

remove_logs() {
	echo "removing previous log files"
	rm "$CURRENT_PATH/logs/traceback.log"
}

remove_exec_file() {
	echo "Removing executable from local bin"
	rm $EXEC_PATH
}

remove_logs
remove_exec_file
remove_alias
