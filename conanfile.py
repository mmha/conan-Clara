#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os

class ClaraConan(ConanFile):
    name = "Clara"
    version = "20171211"
    url = "https://github.com/mmha/conan-Clara"
    description = "A simple to use, composable, command line parser for C++ 11 and beyond"
    license = "BSD 2-Clause"
    commit = "1efb6152b3c84e76d4e33d5312cd681e398f9eb5"

    def source(self):
        source_url = "https://github.com/catchorg/Clara"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.commit))
        extracted_dir = self.name + "-" + self.commit
        os.rename(extracted_dir, "sources")
        #Rename to "sources" is a convention to simplify later steps

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="sources")
        self.copy(pattern="clara.hpp", dst="include", src=os.path.join("sources","single_include"))

    def package_id(self):
        self.info.header_only()