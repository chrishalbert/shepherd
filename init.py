from tmuxp.workspace.builder import WorkspaceBuilder
from pathlib import Path
from tmuxp.config_reader import ConfigReader

herd_config = ConfigReader.from_file(Path('herd.yaml'))

def lamb(commands):
    shell_command = [{"cmd": cmd} for cmd in commands]
    herd_config.content['windows'][0]['panes'].append({'shell_command': shell_command})

def herd():
    builder = WorkspaceBuilder(herd_config.content, server)
    builder.build(session, True)
    exit()