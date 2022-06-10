echo off
@REM require : git , msvc, cmake
@REM build opencv
call thirdparty\build.bat

@REM build project
if not exist .\build md .\build
cd .\build
cmake ..\src -G "Visual Studio 16 2019" -A win32 
cmake --build . --config Release
cd ..\ 