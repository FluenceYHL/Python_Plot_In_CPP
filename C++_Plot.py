import matplotlib.pyplot as plt
import numpy as np
import ctypes


def myPlot(x, y):
    plt.scatter(x, y)
    plt.show()


def plotCluster(clusters):
    for one in clusters:

    plt.legend(loc="best")
    plt.title("GMM Clustering By EM Algorithm")
    plt.show()


# x = np.random.rand(30)
# y = np.random.rand(30)
# plt.scatter(x, y)
# plt.show()


#
# include <iostream>
# include <functional>
# include <cstdlib>
# include <vector>
# include <ctime>
# include <sys/unistd.h>
# include "scopeguard.h"
# include "/usr/include/python3.5/Python.h"

# namespace {
# 	void logCall(const char* message) {
# 		std::cout << message << "\n";
# 	}
# }

# int main() {
# 	Py_Initialize();
# 	YHL::ON_SCOPE_EXIT([&]{
# 		Py_Finalize();
# 		logCall("内存回收完毕");
# 	});
# 	if(!Py_IsInitialized()) {
# 		logCall("加载 Python 失败"); exit(-1);
# 	}
# 	srand(unsigned(time(nullptr)));
# 	std::vector<double> x, y;
# 	for(int i = 0;i < 20; ++i) {
# 		x.emplace_back(rand() % 30);
# 		y.emplace_back(rand() % 30);
# 	}
# 	PyRun_SimpleString("import sys\nsys.path.append('./')");
# 	PyObject* pModule = PyImport_ImportModule("C++_Plot.py");
# 	if(!pModule) {
# 		logCall("导入失败");
# 	}
# 	// auto pFunc = PyObject_GetAttrString(pModule, "myPlot");
# 	// pArg = Py_BuildValue("O,O", x, y);
# 	return 0;
# }

# // PyRun_SimpleString(
# // 	"import matplotlib.pyplot as plt\n"
# // 	"import numpy as np\n"
# // 	"x = np.random.rand(30)\n"
# // 	"y = np.random.rand(30)\n"
# // 	"plt.scatter(x, y)\n"
# // 	"plt.show()\n"
# // );

# // https://www.cnblogs.com/lancelod/p/4036922.html
#
