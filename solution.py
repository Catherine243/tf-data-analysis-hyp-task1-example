import pandas as pd
import numpy as np

from scipy.stats import beta
from calc_prob import calc_prob_between

chat_id = 557932710 # Ваш chat ID, не меняйте название переменной

def solution(convs_ctrl: int, 
             imps_ctrl: int, 
             convs_test: int, 
             imps_ctrl: int) -> bool:
    a_C, b_C = convs_ctrl+1, imps_ctrl-convs_ctrl+1
    beta_C = beta(a_C, b_C)
    a_T, b_T = convs_test+1, imps_test-convs_test+1
    beta_T = beta(a_T, b_T)

    lift=(beta_T.mean()-beta_C.mean())/beta_C.mean()

    prob=calc_prob_between(beta_T, beta_C)
    if (prob < 0.01):
      return False
    else:
      return True
