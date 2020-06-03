from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from blueapps.utils.logger import logger         # 普通日志
from blueapps.utils.logger import logger_celery  # celery日志


def myFunc(request):
    logger.info("这是提示信息")
    logger.debug("这是debug信息")
    logger.warning("这是警告信息")
    logger.error('这是错误信息')
    return render(request, 'mytestapp/index.html', {})
