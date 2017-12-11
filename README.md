[ ![Download](https://api.bintray.com/packages/mmha/conan/Clara%3Ammha/images/download.svg) ](https://bintray.com/mmha/conan/Clara%3Ammha/_latestVersion)
# A simple to use, composable, command line parser for C++ 11 and beyond

[Conan.io](https://conan.io) package for [Clara](https://github.com/catchorg/Clara) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/mmha/conan/Clara).

## For Users: Use this package

### Basic setup

    $ conan install Clara/20171211@mmha/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Clara/20171211@mmha/testing

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## License
[BSD 2-Clause](LICENSE)
