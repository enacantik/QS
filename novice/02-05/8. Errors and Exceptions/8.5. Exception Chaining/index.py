raise RuntimeError from exc
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    print(raise RuntimeError('Failed to open database') from exc)

try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

