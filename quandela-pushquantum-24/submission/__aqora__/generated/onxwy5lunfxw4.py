import ast
from pathlib import Path

__aqora__path = Path(__file__).parent / 'onxwy5lunfxw4.converted.py'
with open(__aqora__path) as f:
    __aqora__script = compile(f.read(), __aqora__path, 'exec', flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)

async def __aqora__(*__aqora__args, **__aqora__kwargs):
    globals().update(locals())
    coroutine = eval(__aqora__script, globals())
    if coroutine is not None:
        await coroutine
    if 'output' in globals():
        return globals()['output']
    else:
        raise NameError("No 'output' variable found in the notebook")
