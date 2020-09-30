import datetime
import json
from django.template.response import TemplateResponse
from .models import RequestLog
from ipware.ip import get_client_ip


class RequestLogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = ""
        request_log = RequestLog()
        path = request.path.split("/")

        if path[1] != "admin":
            request_log = RequestLogMiddleware.save_request(self, request, request_log)
            response = RequestLogMiddleware.save_response(self, request, request_log)
        else:
            response = self.get_response(request)

        return response

    def save_response(self, request, request_log):

        response = self.get_response(request)
        try:
            if isinstance(response, TemplateResponse):
                response_body = {"message":str(response.content)}
            elif response.status_code != 500:
                response_body = {"message":str(response.data)}
            else:
                response_body = {"message":str(response.content)}
        except Exception as e:
            response_body = {"message":str(e)}

        request_log.response_body = response_body
        request_log.status_code = response.status_code
        request_log.response_time = (datetime.datetime.now() - request_log.time).microseconds / 1000
        request_log.save()

        return response


    def save_request(self,request,request_log):

        request_log.method = request.method
        request_log.endpoint = request.path
        client_ip, is_routable = get_client_ip(request)
        request_log.ip = client_ip

        try:
            body = json.loads(request.body.decode('utf-8'))
            if 'password' in body:
                body['password'] = 'xxxxxxxx'
            request_body = body
        except Exception as e:
            request_body = {}

        if request.GET:
            request_log.query_params = dict(request.GET)
        if request.body:
            request_log.request_body = request_body
        request_log.time = datetime.datetime.now()

        try:
            if request.user:
                request_log.user = request.user
        except:
            pass

        request_log.save()

        return request_log