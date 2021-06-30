#!/usr/bin/env bash
# read-menu: a menu driven system information program
clear
cat << EOF
Please Select:
    1. Basecrack
    2. Rotcrack
    3. Unknown Cipher
    4. Unknown Cipher 2
    0. Quit
EOF
echo -n 'Enter selection [0-4]: '
read -r sel

case $sel in
	0) echo "Program terminated.";;
	1) python3 basecrack.py;;
	2) python3 rotcrack.py;;
	3) python3 ciphey.py;;
        4) python3 dcode.py;;
	*)
		echo "Invalid entry." >&2
		exit 1
esac
