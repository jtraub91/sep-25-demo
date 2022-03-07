

def make_instance(name, register=""):
    ret = __salt__["random.make_instance"]()
    if register:
        __context__[register] = ret
    return {
        "name": name,
        "changes": {
            "old": "",
            "new": ret
        },
        "comment": "New instance created",
        "result": True
    }

