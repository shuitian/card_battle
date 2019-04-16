# -*- coding:utf-8 -*-

import inspect

def _add_component(klass, component, funcs):
	for name, attr in component.__dict__.iteritems():
		if name.startswith("__") and name.endswith("__") and name != '__init__':
			continue
		if inspect.isroutine(attr):
			methods = funcs.setdefault(name, [])
			methods.append(attr)
		else:
			setattr(klass, name, attr)
			
def gen_sequence_function(funcs):
	def _wrapper(*args, **kwds):
		value = None
		for f in funcs:
			value = f(*args, **kwds)
		return value

	return _wrapper

def assemble_function(klass, funcs):
	for name, funs in funcs.iteritems():
		if len(funs) == 1:
			func = funs[0]
		else:
			func = gen_sequence_function(funs)
		setattr(klass, name, func)

def components(*import_components):
	def _components(klass):

		funcs = {}
		_add_component(klass, klass, funcs)
		for component in import_components:
			_add_component(klass, component, funcs)
		
		assemble_function(klass, funcs)

		return klass

	return _components