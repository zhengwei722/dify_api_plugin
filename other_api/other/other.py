from flask_restful import Resource, reqparse

from controllers.console.setup import setup_required
from controllers.other_api import api
from controllers.service_api.wraps import DatasetApiResource
import requests


class XiaohongshuApi(DatasetApiResource):
    @setup_required
    def post(self, tenant_id):
        parser = reqparse.RequestParser()
        parser.add_argument("url", required=True, nullable=False, location="json")
        args = parser.parse_args()

        response = requests.get(args["url"])
        if response.status_code == 200:
            # 获取页面的HTML内容
            html_content = response.text

            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # 查找<meta>标签并获取content属性的值
            meta_tag = soup.find('meta', {'name': 'description'})
            if meta_tag:
                description_content = meta_tag['content']
                return {"result": "success", "data": {"content": description_content}}
            else:
                return {"result": "fail", "data": "未找到<meta>标签或content属性"}
        else:
            return {"result": "fail", "data": f"请求失败，状态码：{response.status_code}"}


api.add_resource(XiaohongshuApi, "/other/xiaohongshu")
