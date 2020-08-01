"""
# -*- coding: UTF-8 -*-
__author__: gcc
__website__: www.gcc.中国
"""
import os
import time
import pandas as pd


class UtilsFunction():
    """It's a assist class."""

    def __init__(self, arg_list):
        self.line = "--"
        self.arg_list = arg_list
        self.checked = input("是否需要打印文件头定义, yes or no? \n")

    def judge_options(self):
        if self.checked in ["no", "n", "NO", "No", "N"]:
            print(self.line * 50)
            for key in self.arg_list[0]:
                if self.arg_list[0].get(key) == "":
                    self.first_options()
                else:
                    self.second_options()
        else:
            print(self.line * 50)
            print(__doc__)
            print(self.line * 50)
            for key in self.arg_list[0]:
                if self.arg_list[0].get(key) == "":
                    self.first_options()
                else:
                    self.second_options()

    def first_options(self):
        self.str_choice = input('请确认您需要执行的配置选项: %s: \n' % (list(self.arg_list[0].keys())))
        self.str_input = ""
        while not self.str_choice:
            print("所输入选项不能为空!")
            self.str_choice = input('请确认您需要执行的配置选项: %s: \n' % (list(self.arg_list[0].keys())))
            print(self.line * 50)
        while self.str_choice not in list(self.arg_list[0].keys()):
            print("必须选择已有选项!")
            self.str_choice = input('请输入您需要执行的配置选项: %s: \n' % (list(self.arg_list[0].keys())))
            print(self.line * 50)
        else:
            self.usage_contents()
            print(self.line * 50)
            self.exec_path()
            print(self.line * 50)

    def second_options(self):
        self.str_choice = input('请确认您需要执行的配置选项: %s: \n' % (list(self.arg_list[0].keys())))
        while not self.str_choice:
            print("所输入选项不能为空!")
            self.str_choice = input('请确认您需要执行的配置选项: %s: \n' % (list(self.arg_list[0].keys())))
            print(self.line * 50)
        while self.str_choice not in list(self.arg_list[0].keys()):
            print("必须选择已有选项!")
            self.str_choice = input('请输入您需要执行的配置选项: %s: \n' % (list(self.arg_list[0].keys())))
            print(self.line * 50)
        else:
            for i, j in enumerate(self.arg_list[0].keys()):
                if self.str_choice == str(j):
                    self.str_input = input('请确认您需要执行的配置选项: %s: \n' % (list(self.arg_list[0].values())[i]).split('/'))
                    while not self.str_input:
                        print("所输入选项不能为空!")
                        self.str_input = input('请确认您需要执行的配置选项: %s: \n' % (list(self.arg_list[0].values())[i]).split('/'))
                        print(self.line * 50)
                    while self.str_input not in (list(self.arg_list[0].values())[i]).split('/'):
                        print("必须选择已有选项!")
                        self.str_input = input('请输入您需要执行的配置选项: %s: \n' % (list(self.arg_list[0].values())[i]).split('/'))
                        print(self.line * 50)
                    else:
                        self.datail_contents()
                        print(self.line * 50)
                        self.exec_path()
                        print(self.line * 50)

    def usage_contents(self):
        self.usage_infos = """###"""

    def datail_contents(self):
        self.detail_infos = """###"""

    def exec_path(self):
        txt_info = input("是否输出到.doc文件? Yes or No? \n")
        if txt_info == "yes" or txt_info == "y" or txt_info == "Y" or txt_info == "YES" or txt_info == "Yes":
            try:
                os.mkdir(os.path.join(os.getcwd(), f"doc_output"))
            except Exception:
                pass
                # raise Exception("已经创建'doc_output'文件夹")
            else:
                pass
            finally:
                if self.str_choice and self.str_input:
                    df = pd.DataFrame(data=[self.detail_infos])
                    df.to_csv(f"doc_output" + f"\\" + self.str_input + f"_{int(time.time())}.doc", index=False,
                              header=False)
                    print("文件输出在当前目录的'doc_output'文件夹中, 以 %s 开头." % f"{self.str_input}")
                else:
                    df = pd.DataFrame(data=[self.usage_infos])
                    df.to_csv(
                        f"doc_output" + f"\\" + self.str_choice + f"_{int(time.time())}.doc",
                        index=False, header=False)
                    print("文件输出在当前目录的'doc_output'文件夹中, 以 %s 开头." % f"{self.str_choice}")
            self.result()
        else:
            self.result()

    def result(self):
        """Help choose to continue or exit at the end of the program."""
        print(self.line * 50)
        self.res = input("exit or continue? \n")
        if self.res == "exit" or self.res == "e" or self.res == "exit" or self.res == "E" or self.res == "EXIT":
            print(self.line * 50)
            print("Thank You, 请使用 'Ctrl+c' 退出!")

        else:
            self.judge_options()
            self.result()


# checked = input("是否需要打印文件头定义, yes or no? \n")
# UtilsFunction("name/age").judge_options()
