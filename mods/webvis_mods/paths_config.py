import webvis_mods, libvis
from pathlib import Path

# Sources
manager_path = Path(webvis_mods.__file__).parent
web_src = manager_path / 'web'
web_user_mods = web_src /'src'/ 'modules' / 'presenters' / 'installed'

# Target
vis_dir = Path(libvis.__file__).parent
build_dir = vis_dir / 'front_build'
python_user_mods = vis_dir / 'modules' / 'installed'

# Project templates
templates_path = manager_path / 'project-templates'
files_template = templates_path / 'source-files'
dirs_template = templates_path / 'source-dirs'
