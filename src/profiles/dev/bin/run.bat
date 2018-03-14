@echo off
echo "================================== start ========================="
set _CLASS_PATH= %1
set _MAIN_CLASS= %2
set _EXECJAVA="java"
set _EXECJAVA=%_EXECJAVA% -classpath "%_CLASS_PATH%" %_MAIN_CLASS%  
echo %_EXECJAVA%
%_EXECJAVA%
echo "================================== end ========================="