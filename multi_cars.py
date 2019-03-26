import cars
import road_env_good
road_this = road_env_good.road()
#car[0] start_point ;car[1] end_point ;car[2] current_position ; car[3] speed ; car[4] past_position ;
        # car[5] letf distance ;car[6] plan time ; car[7] car_id
        # 返回car的状态是其行为的状态
        # 如果car_id为-1的话，就说明其无法继续行动
# 如果在路口，即left distance 为0的话，则可以进行下一步的动作，否则就不行
class multi_cars_set():
    def set_cars(self):
        car_list,_ = cars.car_set().init_car()

    def distribute(self,actions,g,cars):
        reward_all = 0
        for i in range(len(cars)):
            #对其中的第i+1辆车进行操作
            car = cars[i+1]
            action = actions[1][int([0].index(i+1))]
            # choose an action in actions ,这是一个二维数组，分别存储id和action
            # 如果action设定为-1，则不对其进行修改，移除出cars之中？
            car,reward,done,current_position,road_id = road_this.travel(action,g=g,car= car)
            if done:
                car[7] = -1
            next_position = car[2]
            cars[i+1] = car
            reward_all = reward_all+reward
        return cars,reward_all,done,next_position
