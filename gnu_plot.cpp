#include <iostream>
#include <functional>
#include <cstdlib>
#include <vector>
#include <sys/unistd.h>
#include "scopeguard.h"
#include "/usr/include/python3.5/Python.h"

namespace {
	void logCall(const char* message) {
		std::cout << message << "\n";
	}

	void plot(const std::vector<double>& x, const std::vector<double>& y) {
		Py_Initialize();
		YHL::ON_SCOPE_EXIT([&]{
			Py_Finalize();
			logCall("Python 内存回收完毕");
		});
		if(!Py_IsInitialized()) {
			logCall("加载 Python 失败"); exit(-1);
		}
		const int len = x.size();
		auto tupleX = PyTuple_New(len);
		auto tupleY = PyTuple_New(len);
		for(int i = 0;i < len; ++i) {
			PyTuple_SET_ITEM(tupleX, i, Py_BuildValue("f", x[i]));
			PyTuple_SET_ITEM(tupleY, i, Py_BuildValue("f", y[i]));
		}
		PyRun_SimpleString("import sys");
	    PyRun_SimpleString("sys.path.append('./')");
	    PyObject* pModule = PyImport_ImportModule("C++_Plot");
		auto pFunc = PyObject_GetAttrString(pModule, "myPlot");
		auto pArg = Py_BuildValue("O,O", tupleX, tupleY);
		PyEval_CallObject(pFunc, pArg);
		if(pModule) Py_DECREF(pModule);
	}
}

int main() {
	std::vector<double> x, y;
	srand(unsigned(time(nullptr)));
	for(int i = 0;i < 60; ++i) {
		x.emplace_back(rand() % 30);
		y.emplace_back(rand() % 40);
	}
	plot(x, y);
	return 0;
}