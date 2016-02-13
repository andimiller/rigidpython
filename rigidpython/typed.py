import inspect, warnings


class TypeWarning(Warning):
    pass


def _typed(f: callable, level: int = 2) -> callable:
    if not __debug__:
        return f
    s = inspect.signature(f)  # type: inspect.Signature

    def inner(*args, **kwargs):
        # bind arguments and insert defaults
        bound = s.bind(*args, **kwargs)  # type: inspect.BoundArguments
        bound.apply_defaults()
        # extract the parameter types
        sigtypes = list(map(lambda x:x.annotation, s.parameters.values()))
        # check all parameter types
        for pair in zip(bound.arguments.values(), sigtypes):
            if isinstance(pair[1], type):
                if not type(pair[0]) == pair[1]:
                    warnings.warn("expected argument of type {}, got {}".format(pair[1], type(pair[0])), TypeWarning, level)
            elif callable(pair[1]):
                if not pair[1](pair[0]):
                    warnings.warn("expected argument of type {}, got {}".format(callable, type(pair[0])), TypeWarning, level)
        result = f(*bound.args, **bound.kwargs)
        # return type checking
        if isinstance(s.return_annotation, type):
            if type(result) != s.return_annotation:
                warnings.warn("expected return of type {}, got {}".format(s.return_annotation, type(result)), TypeWarning, level)
        elif callable(s.return_annotation):
            if not s.return_annotation(result):
                warnings.warn("expected argument of type {}, got {}".format(callable, type(result)), TypeWarning, level)
        return result
    return inner


@_typed
def typed(f: callable, level: int = 2) -> callable:
    return _typed(f, level)

@_typed
def typed3(f: callable) -> callable:
    return _typed(f, 3)