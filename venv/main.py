import os, time

from pprint import pprint
from copy import  deepcopy
from time import sleep
# clear = lambda :print('\n'*80)
E = '[ ]'
P = '[◾]'
D ='[◎]'
S = '[◾]'
A = '[●]'
A_P = '[▣]'
A_D = '[◉]'
X,Y = 0,1
OH = 1
NOH = 0
EAST, WEST, NORTH, SOUTH, PICKUP, DROPOFF = 0,1,2,3,4,5

class PDWORLD:

    def __init__(self, grid, state,  start_position, pickup_locations, pickup_limits, dropoff_locations, dropoff_limits):
        self.grid = grid
        self.state = state
        self.start_postion = start_position
        self.pickup_limits = pickup_limits
        self.pickup_locations = pickup_locations
        self.dropff_limits = dropoff_limits
        self.dropoff_locations = dropoff_locations
    def get_possible_actions(self,state):
        agent_pos = state.agent_location
        block = state.block
        actions = [EAST,WEST,NORTH,SOUTH]

        # pick up and drop offs are only applicable in certain circumstances
        if (state.block is OH) and (state.agent_location in world.dropoff_locations):
            indx = world.dropoff_locations.index(state.agent_location)
            if dropoff_limits[indx] < 5:
                actions.append(DROPOFF)
                return actions
        if (state.block is NOH) and (state.agent_location in world.pickup_locations) :
            indx = world.pickup_locations.index(state.agent_location)
            if pickup_limits[indx] > 0:
                actions.append(PICKUP)
                return actions
        return actions


        # if block == NOH and agent_pos in pickup_locations:
        #     if world.pickup_limits[pickup_locations.index(agent_pos)] > 0:
        #         return [EAST, WEST, NORTH, SOUTH, PICKUP]
        #     else:
        #         pass
        # elif block == OH and agent_pos in dropoff_locations:
        #     if world.dropff_limits[dropoff_locations.index(agent_pos)] < 5:
        #         return [EAST, WEST, NORTH, SOUTH, DROPOFF]
        #     else:
        #         pass
        # else:




        return [EAST,WEST,NORTH,SOUTH, PICKUP,DROPOFF]
    def __str__(self):
        s = ''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if [i,j] == self.state.agent_location:
                    s += A
                else:
                    s+=grid[i][j]
            s+='\n'
        return s
class State:
    def __init__(self, agent_position, block):
        self.agent_location = agent_position
        self.block = block
    def __str__(self):
        return f"AL: {self.agent_location} B: {self.block}"
    def __eq__(self, other):
        return self.agent_location == other.agent_location and self.block == other.block and isinstance(other, State)
    def __hash__(self):
        return hash(str(self.agent_location)+str(self.block))


# Given a state and action, returns the
# takes state and action, return new_state, reward, done
def act(state, action):
    done = False
    reward = 0
    al = deepcopy(state.agent_location)
    block = deepcopy(state.block)
    grid_v_max = len(world.grid) - 1
    grid_h_max = len(world.grid[0]) - 1

    if action == EAST:
        al[1] = min(grid_h_max,al[1]+1)
        reward = -1
    elif action == WEST:
        al[1] = max(0,al[1]-1)
        reward = -1
    if action == NORTH:
        al[0] = max(0,al[0]-1)
        reward = -1
    elif action == SOUTH:
        al[0] = min(grid_v_max,al[0]+1)
        reward = -1
    elif action == PICKUP:
        # print(al)
        block = 1
        reward = 13
        if al == [0,0]:
            world.pickup_limits[0] -= 1
        elif al == [2,2]:
            world.pickup_limits[1] -= 1
        elif al == [4,4]:
            world.pickup_limits[2] -= 1

    elif action == DROPOFF:
        block = 0
        reward = 13
        if al == [4,0]:
            world.dropff_limits[0] += 1
        elif al == [4,2]:
            world.dropff_limits[1] += 1
        elif al == [1,4]:
            world.dropff_limits[2] += 1

    if world.pickup_limits == [0,0,0] and world.dropff_limits == [5,5,5]:
        done = True
    newstate = State(al, block)
    return newstate, reward, done

actions = [EAST,WEST,NORTH,SOUTH,PICKUP,DROPOFF]
actions_string = ['EAST','WEST','NORTH','SOUTH','PICKUP','DROPOFF']
grid = [[P,E,E,E,E],[E,E,E,E,D],[E,E,P,E,E],[E,E,E,E,E],[D,E,D,E,P]]
start_location = [0,4]
start_block = NOH
agent_location = start_location
pickup_locations = [[0,0],[2,2],[4,4]]
pickup_limits = [5,5,5]
dropoff_locations = [[4,0],[4,2],[1,4]]
dropoff_limits = [0,0,0]
start_state = State(agent_location,NOH)
world = PDWORLD(grid,start_state, start_location, pickup_locations,pickup_limits, dropoff_locations, dropoff_limits)
st = start_state

#
# state = start_state
# print(world)
# world.state, reward, done = act(state,WEST)
# print(world.state, reward)
# print(world)
#





print(world)
# flush = true in print
# world.dropff_limits[2] = 6
# for i in range(5):
#     for j in range(5):
#         print(f"at agent_location {i,j} possible actions {world.get_possible_actions(([i,j],OH))}")
import numpy as np
import random
random.seed(42)
N_STATE = 50
N_EPISODES = 1000
MAX_EPISODE_STEPS = 4000
alpha = 0.1
gamma = 1
eps = 0.3
q_table = dict()
def q(state, action = None):
    if state not in q_table:
        q_table[state] = np.zeros(len(actions))
    if action is None:
        return q_table[state]
    return q_table[state][action]

def choose_action(state):
    # return random.choice(world.get_possible_actions(state))
    ps = world.get_possible_actions(state)
    # print(state)
    # for p in ps:
    #     print(actions_string[p], end=' ')
    #
    # print()
    # time.sleep(1)
    sta = q(state)
    somev = []

    for a in ps:
        somev.append(a)
    # if PICKUP not in ps:
    #     np.delete(sta, PICKUP)
    #     print("Deleting PICKUP")
    # if DROPOFF not in ps:
    #     np.delete(sta, DROPOFF)
    #     print("Deleting Drop")
    # print(somev)

    if random.uniform(0,1) < eps:
        return random.choice(somev)
    else:
        return np.argmax(somev)
    # if state.agent_location in world.pickup_locations and world.pickup_limits[pickup_locations.index(state.agent_location)] > 0 :
    #     return PICKUP
    # elif state.agent_location in world.dropoff_locations and world.dropff_limits[dropoff_locations.index(state.agent_location)] < 5:
    #     return DROPOFF
    # else:
    #     if random.uniform(0,1) < eps:
    #         return random.choice(world.get_possible_actions(state))
    #     else:
    #         actionc =  np.argmax(q(state))
    #         # print(f"choosing action {actionc} because of argmax")
    #         return  actionc
random.seed(1)
for e in range(N_EPISODES):
    state = start_state
    # print(type(state))
    total_reward = 0
    while(True):
    # for _ in range(MAX_EPISODE_STEPS):
        action = choose_action(state)
        # print("selected action: ", actions_string[action])
        nextstate, reward, done = act(state, action)
        # print("new state:", nextstate,"reward:",reward)
        # print(nextstate)
        world.state = nextstate
        print(actions_string[action])
        print(world)
        total_reward += reward

        if action == PICKUP and (-1 in world.pickup_limits):
            print(state,nextstate, actions_string[action],'R: ',reward)
            exit()

        # print(state,nextstate, actions_string[action],'R: ',reward)
        # time.sleep(.1)
        q(state)[action] = q(state,action) + alpha * (reward + gamma * np.max(q(nextstate))-q(state,action))
        # print(f"at state {state.agent_location} {state.block} choosing action {action} {actions} with reward {reward}")
        # sleep(.1)
        state = nextstate
        if done:
            print(f"Episode {e+1}: total reward -> {total_reward}")
            print("Done %d",e)
            break



r = q(State([0,4],NOH))
print(f"east={r[EAST]}, west={r[WEST]}, north={r[NORTH]}, south={r[SOUTH],},pickup={r[PICKUP]}, dropoff={r[DROPOFF]}")
r = q(State([0,3],NOH))
print(f"east={r[EAST]}, west={r[WEST]}, north={r[NORTH]}, south={r[SOUTH],},pickup={r[PICKUP]}, dropoff={r[DROPOFF]}")
r = q(State([0,2],NOH))
print(f"east={r[EAST]}, west={r[WEST]}, north={r[NORTH]}, south={r[SOUTH],},pickup={r[PICKUP]}, dropoff={r[DROPOFF]}")
r = q(State([1,4],OH))
print(f"east={r[EAST]}, west={r[WEST]}, north={r[NORTH]}, south={r[SOUTH],},pickup={r[PICKUP]}, dropoff={r[DROPOFF]}")
print(world.pickup_limits)
print(world.dropff_limits)

print(f"\t\t\t\t{actions_string}")
for k,v in q_table.items():
    print(k,  end=' | ')
    for e in v:
        print('%.3f'%round(e,2),end='\t')
    print()
# for key, value in q_table.items():
#     print(key, sep=' ')
#     for v in value:
#         print(v,sep=' ')
#     print
print(world)