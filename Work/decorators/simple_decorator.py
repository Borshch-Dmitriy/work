#Json format + functools.wraps(doc and name)
import json
import functools

def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        json_data = json.dumps(func(*args, **kwargs))
        print(json_data)
        return json_data
    return wrapper


@jsonify
def make_str(s1, s2):
    return (s1 + s2) * 5


print(make_str('bee', 'geek'))


@jsonify
def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}


print(make_user(4, False, None))

# TEST_7:
@jsonify
def make_tuple():
    """JSON-Tuple object"""
    return (1, '2', 3.0, None, False, {'1': True})


print(make_tuple())
print(make_tuple.__name__)
print(make_tuple.__doc__)