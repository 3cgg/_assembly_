import sys
import os
from os import path
import platform
import string
import copy

print(platform.system())

currentWorkPath = os.getcwd()  # 获得当前工作目录

print(currentWorkPath)

classPath = ""
mainClass = ""


class Run:

    def run(self):
        raise NotImplemented


class Env(Run):

    def __init__(self):
        self.__cps = []
        self.__main_class = ""

    def java_home(self):
        raise NotImplemented

    def java(self):
        # return self.java_home()+"/bin/java "
        return "java "

    def join_str(self):
        raise NotImplemented

    def append_cp(self, *cp):
        self.__cps.extend(list(cp))

    def main_class(self, mainClass):
        self.__main_class = mainClass

    def __cp(self):
        libPath = path.dirname(currentWorkPath) + "/lib"
        libJars = []
        try:
            for file in os.listdir(libPath):
                libJars.append(libPath + "/" + file)
        except Exception:
            raise Exception
        return libJars

    def cp(self):
        cps = copy.deepcopy(self.__cps);
        cps.extend(self.__cp())
        return self.join_str().join(cps)

    def run(self):
        action = self.java() + " " + " -cp " + self.cp() + " " + self.__main_class
        print(action)
        print("-" * 80 + "-ready , running sh/bat -" + "-" * 80)
        os.system(currentWorkPath + "/run \"" + self.cp() + "\" " + self.__main_class)


class Windows(Env):

    def java_home(self):
        return "%JAVA_HOME%"

    def join_str(self):
        return ";"

    def run(self):
        return super().run()


class Linux(Env):

    def java_home(self):
        return "$JAVA_HOME"

    def join_str(self):
        return ":"

    def run(self):
        return super().run()


def main():
    system_ = platform.system()
    env = None
    if system_ == "Windows":
        env = Windows()
        env.append_cp("c:/work/a.jar")
        env.main_class("me.libme._assembly_.App")
        print(env.cp())
        env.run()
    elif system_ == "Linux":
        env = Linux()
    else:
        print("Other System tasks")


if __name__ == '__main__':
    main()
