# В этом модуле функция будет считать процент успешных действий игрока

import math

#функции нужны два параметра: общее количество выполненого действия и количество из них успешных.
# all_attempts  - это все попытки совершения действия в игре
# well_done_attempts  -  это успешные попытки совершения действия в игре
def attempts_accuracy(all_attempts,well_done_attempts):
    return 100/(all_attempts/well_done_attempts)



