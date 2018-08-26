# -*- coding: utf-8 -*-
import re


def minify_html(text):
    """
    Минификация HTML

    :param text: Исходный HTML
    :type text: str
    :return: Минифицированный HTML
    :rtype: str
    """
    text = re.sub(r"[\t\n\r]", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\> \<", "><", text)
    text = re.sub(r"\<!wrap!\>", "\n", text)
    return text


def money_format(val):
    """
    Возваращает строку с числом, разделенным на разряды

    :param val: Исходное число
    :type val: int or str
    :return: Форматированная строка
    :rtype: str
    """
    try:
        res = '{0:,}'.format(val).replace(',', '&nbsp;')
    except ValueError:
        return val
    return res
