from app.models import Goods
from app.models import Services
from app.models import BotUser
from app.models import State


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


def get_user_by_id(tg_id: int) -> BotUser:
    return BotUser.objects.get(telegram_id=tg_id)


def get_state_by_user(user: BotUser) -> State:
    return State.objects.get(bot_user=user)


def get_state_by_id(tg_id: int) -> State:
    user = get_user_by_id(tg_id)
    return get_state_by_user(user)

# user = get_user_by_id(831322980)
#
# print(get_state_by_user(user).goods)
