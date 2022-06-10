@REM require : git , vs2019, cmake
echo off
if not exist opencv git clone https://github.com/opencv/opencv
if not exist opencv\build md opencv\build
cd opencv\build
cmake ..\ -DBUILD_SHARED_LIBS OFF -G "Visual Studio 16 2019" -A x64 
cmake --build . --config Release
cd ..\..\ 

if not exist .\lib md .\lib
copy .\opencv\build\lib\Release\*.lib .\lib
if not exist .\bin md .\bin
copy .\opencv\build\bin\Release\*.dll .\bin
if not exist .\include\opencv2 md .\include\opencv2
copy .\opencv\include\opencv2\opencv.hpp .\include\opencv2