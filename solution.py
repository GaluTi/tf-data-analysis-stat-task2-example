import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 640884635 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    sum_x = sum(x)
    z_1_g = gamma.ppf(alpha/2, a=len(x), loc=sum_x - len(x)/2, scale=1)
    z_2_g = gamma.ppf(1-alpha/2, a=len(x), loc=sum_x - len(x)/2, scale=1)
    a_g = z_1_g * 2 / (len(x) * 5**2)
    b_g = z_2_g * 2 / (len(x) * 5**2)
    return a_g, b_g
