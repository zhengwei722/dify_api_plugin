import subprocess
import os
import shutil
import stat
import re

def clone_github_repo(repo_url):
    """
    克隆指定仓库
    :param repo_url:
    :return:
    """
    subprocess.run(["git", "clone", "--depth", "1", repo_url], check=True)
    # 获取仓库名称
    repo_name = repo_url.split("/")[-1].replace(".git", "")

def move_folder_to_directory(source_folder, target_dir):
    """
    移动a目录到b目录
    :param repo_url:
    :return:
    """
    target_folder_path = os.path.join(target_dir, os.path.basename(source_folder))
    shutil.move(source_folder, target_folder_path)
def move_file_to_folder(src, dst):
    """
    移动a文件到b目录
    :param repo_url:
    :return:
    """
    shutil.move(src, dst)

def delete_folder_content_and_folder(folder_path):
    """
    删除指定目录
    :param repo_url:
    :return:
    """
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            try:
                os.remove(filename)
            except PermissionError:
                os.chmod(filename, stat.S_IWRITE)
                os.remove(filename)
        for name in dirs:
            dirname = os.path.join(root, name)
            shutil.rmtree(dirname)
    # 删除空的文件夹
    if not os.listdir(folder_path):  # 检查文件夹是否为空
        os.rmdir(folder_path)


# 第一步下载difu原始文件
repo_url = "https://github.com/langgenius/dify.git"
clone_github_repo(repo_url)
move_folder_to_directory('./dify/api', '.')
move_folder_to_directory('./dify/web', '.')
move_folder_to_directory('./dify/docker', '.')
delete_folder_content_and_folder('dify')
# 第二步下载插件
move_file_to_folder('./dify_api_plugin/.env', './api')
move_file_to_folder('./dify_api_plugin/.env.local', './web')
move_file_to_folder('./dify_api_plugin/middleware.env', './docker')
move_file_to_folder('./dify_api_plugin/start_api_docker.py', './api')
move_file_to_folder('./dify_api_plugin/start_middleware_docker.py', './docker')
move_file_to_folder('./dify_api_plugin/start_web_docker.py', './web')
delete_folder_content_and_folder('dify_api_plugin')