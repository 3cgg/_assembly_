import sys
import os
import platform
import string
import copy

print(platform.system())



currentWorkPath=os.getcwd() #获得当前工作目录

print(currentWorkPath)

classPath=""
mainClass=""


class Run:

    def run(self):
        raise NotImplemented


class Env:

    def __init__(self):
        self.__cps=[]

    def java_home(self):
        raise NotImplemented

    def join_str(self):
        raise NotImplemented

    def append_cp(self,*cp):
        self.__cps.append(cp)

    def __cp(self):
        libPath=currentWorkPath.+"/../lib"
        libJars=[]
        try:
            for file in os.listdir(libPath):
                libJars.append(libPath+"/"+file)
        except Exception:
            raise Exception
        return libJars

    def cp(self):
        self.join_str().join(copy.deepcopy(self.__cps).append(self.__cp()))

class Windows(Env,Run):

    def java_home(self):
        return "%JAVA_HOME%"

    def join_str(self):
        return ";"

    def run(self):
        return super().run()


class Linux(Env,Run):

    def java_home(self):
        return "$JAVA_HOME"

    def join_str(self):
        return ":"

    def run(self):
        return super().run()




def main():
    system_ = platform.system()
    env=None
    if system_ == "Windows":
        env=Windows()
        env.append_cp("c:/work/a.jar")
        print(env.cp())
    elif system_ == "Linux":
        env = Linux()
    else:
        print("Other System tasks")


if __name__ == '__main__':
    main()