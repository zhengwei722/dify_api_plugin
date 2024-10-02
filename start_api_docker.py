import subprocess
import os


def build_and_run_docker_image(dockerfile_path, image_name, tag, container_name,port):
    try:

        result = subprocess.run(['docker', 'build', '-f', f'{dockerfile_path}', '-t', f'{image_name}:{tag}', '.'],
                                check=True)
        print(f"api容器构建成功")

        result = subprocess.run(
            ['docker', 'run', '-d', '--name', f'{container_name}', '-p', f'{port}:{port}', f'{image_name}'], check=True)
        print(f"api容器运行成功：端口{port}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

        # docker run -d --name my-running-app -p 3000:3000 difyweb


if __name__ == "__main__":
    dockerfile_path = 'Dockerfile'
    image_name = "dify_api"
    tag = "latest"
    container_name = "dify_api_container"  # 容器的名称
    port = 5001
    build_and_run_docker_image(dockerfile_path, image_name, tag, container_name,port)
