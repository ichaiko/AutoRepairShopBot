from app.models import Goods
from app.models import Services


def get_goods_list():
    goods = Goods.objects.all()

    if len(goods) == 0:
        return None

    return goods


def get_services_list():
    services = Services.objects.all()

    if len(services) == 0:
        return None

    return services
