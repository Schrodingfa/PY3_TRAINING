goods_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}


def shopping(goods_info):
    print_goods(goods_info)
    item = int(input("1键购买，2键结算。"))
    if item == 1:
        order_list = choice_goods(goods_info)
    if item == 2:
        pay_bill(order_list, goods_info)


def choice_goods(goods_info):
    """
    选购商品
    :param goods_info: 商品清单
    :return:
    """
    order_list = []
    goods_id = int(input("请输入商品编号："))
    if goods_exist(goods_id, goods_info):
        count = int(input("请输入购买数量："))
        order_list.append((goods_id, count))
        print("添加到购物车。")
    else:
        print("该商品不存在")
    return order_list


def goods_exist(goods_id, goods_info):
    """
    判断输入的商品编号是否存在
    :param goods_id: 待判断商品编号
    :param goods_info: 商品清单
    :return: 返回bool值
    """
    if goods_id in goods_info:
        return True
    return False


def print_goods(goods_info):
    """
    打印商品信息
    :param goods_info: 商品清单
    :return:
    """
    for key, value in goods_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


def pay_bill(order_list, goods_info):
    total_price = 0
    for item in order_list:
        total_price += print_bill(item, goods_info)
    return pay(total_price)


def print_bill(item, goods_info):
    goods = goods_info[item[0]]
    print("商品：%s，单价：%d,数量:%d." % (goods["name"], goods["price"], item[1]))
    price = goods["price"] * item[1]
    return price


def pay(total_price):
    money = float(input("总价%d元，请输入金额：" % total_price))
    if money >= total_price:
        print("购买成功，找回：%d元。" % (money - total_price))
        # order_list.clear()
        return True
    else:
        print("金额不足.")
        return False


shopping(goods_info)
