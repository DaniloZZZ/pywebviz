import webvis_mods
import importlib
spec = importlib.util.find_spec('webvis')
from pathlib import Path

# Sources
manager_path = Path(webvis_mods.__file__).parent
web_src = manager_path / 'web'
web_user_mods = web_src /'src'/ 'modules' / 'presenters' / 'installed'

# Target
vis_dir = Path(spec.origin).parent
build_dir = vis_dir / 'front_build'
python_user_mods = vis_dir / 'modules' / 'installed'

# Project templates
templates_path = manager_path / 'project-templates'
files_template = templates_path / 'source-files'
dirs_template = templates_path / 'source-dirs'
