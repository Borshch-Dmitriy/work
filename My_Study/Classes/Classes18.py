class AnyClass:

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)

  def __str__(self):
    items = [f'{key}={value!r}' for key, value in self.__dict__.items()]
    res = ', '.join(items)
    return f'AnyClass: {res}' if res else 'AnyClass:'

  def __repr__(self):
    items = [f'{key}={value!r}' for key, value in self.__dict__.items()]
    res = ', '.join(items)
    return f'AnyClass({res})'
