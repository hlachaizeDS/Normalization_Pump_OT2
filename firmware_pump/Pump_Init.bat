SetLocal EnableDelayedExpansion
set content=
for /F "delims=" %%i in (robotIP.txt) do set ip=!content!%%i

ssh -i ot2_ssh_key root@%ip% "python /data/DispenseUnit_1161.py 0"