## cppunit in CodeBlocks
- https://sourceforge.net/projects/cppunit/files/cppunit/1.12.1/
- https://sourceforge.net/projects/cppunit/files/cppunit/1.12.1/cppunit-1.12.1.tar.gz/download
- https://stackoverflow.com/questions/41924136/what-are-beginners-steps-for-cppunit-in-codeblocks

```

download cppunit, unzip to C:\cppunit-1.12.1
download MinGW, copy and rename mingw32-make.exe to make.exe, add PATH


cd C:\cppunit-1.12.1

./configure

make

make install


Open a new console application in Code::Blocks.

Go To project->build option->search Directories->compiler

add C:\cppunit-1.12.1\include

Go To project->build option->search Directories->linker

add C:\cppunit-1.12.1\src\cppunit\Release

Go To project->build option->linker settings

add C:\cppunit-1.12.1\src\cppunit\Release\libcppunit.a

```
