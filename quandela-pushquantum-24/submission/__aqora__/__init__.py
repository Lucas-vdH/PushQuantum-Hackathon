import importlib.util
import sys
from pathlib import Path

dir_path = Path(__file__).resolve().parent


spec_onxwy5lunfxw4 = importlib.util.spec_from_file_location(
    'submission.solution',
    dir_path / 'generated' / 'onxwy5lunfxw4.py')
module_onxwy5lunfxw4 = importlib.util.module_from_spec(spec_onxwy5lunfxw4)
sys.modules['submission.solution'] = module_onxwy5lunfxw4
spec_onxwy5lunfxw4.loader.exec_module(module_onxwy5lunfxw4)

async def generated_onxwy5lunfxw4(*__aqora__args, **__aqora__kwargs):
    return await module_onxwy5lunfxw4.__aqora__(*__aqora__args, **__aqora__kwargs)
