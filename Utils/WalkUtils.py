import os


def walk_dirs(root_path):
    """
    Args:
        root_path:

    Returns:
        dest_real_paths: root_path目录下所有的文件夹绝对路径
    """
    dest_real_paths = []
    for path in os.listdir(root_path):
        if os.path.isdir(os.path.join(root_path, path)):
            dest_real_paths.append(os.path.join(root_path, path))

    return dest_real_paths


def walk_files(root_path):
    """

    Args:
        root_path:

    Returns:
        dest_real_paths: root_path目录下所有的文件绝对路径
    """
    dest_real_paths = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        for file_name in filenames:
            dest_real_paths.append(os.path.join(dirpath, file_name))

    return dest_real_paths
