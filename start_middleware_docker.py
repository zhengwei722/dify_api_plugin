import subprocess

def run_docker_compose(compose_file_path):
    command = f"docker compose -f {compose_file_path} up -d"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"已成功启动middleware中定义的服务")
    except subprocess.CalledProcessError as e:
        print(f"启动服务时出错: {e}")

if __name__ == "__main__":
    compose_file_path = "./docker-compose.middleware.yaml"  # 替换为你的 docker-compose.yml 路径
    run_docker_compose(compose_file_path)