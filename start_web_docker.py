import subprocess
import os


def build_and_run_docker_image(image_name, container_name,port,api_url):
    try:

        result = subprocess.run(['docker', 'build',  '-t', f'{image_name}', '.'],
                                check=True)
        print(f"web容器构建成功")

        result = subprocess.run(
            ['docker', 'run', '-d','--name', f'{container_name}', '-p',f'{port}:{port}', '-e',f'CONSOLE_API_URL=http://{api_url}:{port}', '-e',f'APP_API_URL=http://{api_url}:{port}',f'{image_name}' ], check=True)
        print(f"api容器运行成功：端口{port}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_name = "dify_web"
    container_name = "dify_web_container"  # 容器的名称
    port = 5001
    api_url = '38.12.33.185'
    build_and_run_docker_image(image_name, container_name,port,api_url)
