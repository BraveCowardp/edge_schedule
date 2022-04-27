import constant
import math
class utils:

    @classmethod
    def get_trans_delay(cls,x1,y1,x2,y2):
        distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
        return distance*constant.CO_DISTANCE_TO_DELAY