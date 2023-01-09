from pathlib import Path
from src.core.constants import PROJECT_ROOT_PATH


def join_domain_port(domain: str, port: str | int) -> str:
    """
    将 传入的domain 和 port 拼接成 domain:port 形式的
    :param domain: 域名
    :param port: 端口号
    :return: domain:port
    """
    return domain + ':' + str(port)


def parse_user_input_path(p: str | Path) -> Path:
    """
    将 类似与'~/xxx/ooo' 的路径改为绝对路径
    :param p: 原路径
    :return: 改为绝对路径的Path对象
    """
    if p.startswith('~'):
        return Path(p.replace('~', str(Path.home())))
    if p.startswith('/'):
        return Path(p)
    if p.startswith('.'):
        return Path(p).absolute()
    if Path(p).is_file():
        return Path(p)
    return PROJECT_ROOT_PATH.joinpath(p)



