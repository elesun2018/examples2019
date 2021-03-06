#coding=utf-8
"""
logging模块
Author: elesun
logging模块是Python内置的标准模块，主要用于输出运行日志，可以设置输出日志的等级、日志保存路径、日志文件回滚等；
相比print，具备如下优点：
    可以通过设置不同的日志等级，在release版本中只输出重要信息，而不必显示大量的调试信息；
    print将所有信息都输出到标准输出中，严重影响开发者从标准输出中查看其它数据；logging则可以由开发者决定将信息输出到什么地方，以及怎么输出
"""
import logging
import subModule

logger = logging.getLogger("mainModule")
logger.setLevel(level = logging.INFO)

handlerfile = logging.FileHandler("log.txt")
#handlerfile.setLevel(logging.INFO)
formatter1 = logging.Formatter('%(asctime)s - %(name)25s - %(levelname)s - %(message)s')
handlerfile.setFormatter(formatter1)
logger.addHandler(handlerfile)

screen = logging.StreamHandler()
#screen.setLevel(logging.INFO)
formatter2 = logging.Formatter('%(asctime)s - %(name)25s - %(levelname)s - %(message)s')
screen.setFormatter(formatter2)
logger.addHandler(screen)


logger.info("creating an instance of subModule.subModuleClass")
a = subModule.SubModuleClass()
logger.info("calling subModule.subModuleClass.doSomething")
a.doSomething()
logger.info("done with  subModule.subModuleClass.doSomething")
logger.info("calling subModule.some_function")
subModule.som_function()
logger.info("done with subModule.some_function")