import random,time
import numpy as np
import copy
EAST, WEST, NORTH, SOUTH, PICKUP, DROPOFF = 0, 1, 2, 3, 4, 5
PRANDOM, PGREEDY, PEXPLOIT = 1, 2, 3
ENABLE_GUI = False
class PDWORLD:
    def __init__(self, state, pickup_point, dropoff_points, pickup_items_count, dropoff_items_count):
        self.state = state
        self.pickup_items_count = pickup_items_count
        self.dropoff_items_count = dropoff_items_count

        self.pickup_points = pickup_point
        self.dropoff_points = dropoff_points



    # can agent pickup/dropoff from a given state
        # has to be at the pickup/dropoff point
        # for pickup should not already be carrying an itme and should be carrying an item for dropoff
        # pickup location should have at least one package and dropoff location should not be maxed out
        # IF ALL CONDITIONS SATISFIED -> PICKUP/DROPOFF
    def can_pickup(self, state):
        y,x,z = state
        if [y,x] in self.pickup_points and z == 0:    # if agent is at a pickup point and doesn't already have a package
            index_location = self.pickup_points.index([y,x])  # index of the pickup item location >= 0 means we have an item
            if self.pickup_items_count[index_location] > 0:    # does the location still have packages left for pickup
                return True
        return False
    def can_dropoff(self, state):
        y,x, z = state
        if [y,x] in self.dropoff_points and z == 1:    # if agent is at a pickup point and doesn't already have a package
            index_location = self.dropoff_points.index([y,x])  # index of the pickup item location >= 0 means we have an item
            if self.dropoff_items_count[index_location] < 5:    # does the location still have packages left for pickup
                return True
        return False

    # applicable action from a give state
    #
    def applicable_actions(self,state):
        y,x, z = state
        actions = []
        if not out_of_boundary(state, EAST):
            actions.append(EAST)
        if not out_of_boundary(state,WEST):
            actions.append(WEST)
        if not out_of_boundary(state,NORTH):
            actions.append(NORTH)
        if not out_of_boundary(state,SOUTH):
            actions.append(SOUTH)
        if z == 1 and self.can_dropoff(state):
            actions.append(DROPOFF)
        elif z == 0 and self.can_pickup(state):
            actions.append(PICKUP)
        # print("applicable action in state ", state, actions)
        return actions
def get_state_index(state):
    y,x,z = state
    return 5*y+x+(z*25)

class QTable:
    def __init__(self, num_states, num_actions):
        np.random.seed(42)
        self.qtable = np.zeros([num_states, num_actions])

    def __str__(self):
        return np.array_str(self.qtable, precision=6)

    def value(self, state, action):
        return self.qtable[state][action]

    # given a state and a set of applicable actions: retuns an action with maximum qvalue
    def argmax(self, state,mask=None):
        if mask == None:
            return np.argmax(q.qtable[state])
        else:
            idx = np.array(mask)
            newq = np.ones_like(self.qtable)
            newq[:,idx] = 0
            maskedQ = np.ma.masked_array(self.qtable,newq)
            return np.argmax(maskedQ[state], 0)


num_states = 50
num_actions = 6
q = QTable(num_states, num_actions)
def out_of_boundary(state,action):
    y,x,z = state
    # print("State inside aa ", state)
    if x < 4 and action == EAST:
        return False
    elif x > 0 and action == WEST:
        return False
    elif y > 0 and action == NORTH:
        return False
    elif y < 4 and action == SOUTH:
        return False
    else:
        return True
def isTerminal(world, state):
    if world.pickup_items_count == [0,0,0] and world.dropoff_items_count == [5,5,5]:
        return True
    return False

def apply(world, state, action):
    done = False
    y,x, z = state
    reward = 0
    # print(action == EAST)
    if action == NORTH:
        reward = -1
        y -= 1
    elif action == SOUTH:
        reward = -1
        y += 1
    elif action == EAST:
        reward = -1
        x += 1
    elif action == WEST:
        reward = -1
        x -= 1
    elif action == PICKUP:
        if world.can_pickup(state):
            reward = 13
            z = 1
            world.pickup_items_count[world.pickup_points.index([state[0],state[1]])] -= 1
    elif action == DROPOFF:
        if world.can_dropoff(state):
            reward = 13
            z = 0
            world.dropoff_items_count[world.dropoff_points.index([state[0],state[1]])] += 1
    else:
        print("Nothing found")
    if isTerminal(world,state):
        done = True

    return [y,x,z], reward, done




def select_action(world, state, policy):
    applicable_actions = world.applicable_actions(state)
    # print("applicable action for ",state, applicable_actions)
    global selected
    selected = None
    if policy == PRANDOM:
        if PICKUP in applicable_actions:
            selected = PICKUP
        elif DROPOFF in applicable_actions:
            selected = DROPOFF
        else:
            selected = np.random.choice(applicable_actions)
        # print("selected action: ", selected)
    elif policy == PGREEDY:
        if PICKUP in applicable_actions:
            selected = PICKUP
        elif DROPOFF in applicable_actions:
            selected = DROPOFF
        else:
            selected =  q.argmax(get_state_index(state),applicable_actions)
    elif policy == PEXPLOIT:
        if PICKUP in applicable_actions:
            selected = PICKUP
        elif DROPOFF in applicable_actions:
            selected = DROPOFF
        else:
            rvalue = np.random.uniform(0,1)
            if rvalue < 0.2:
                selected = np.random.choice(applicable_actions)
            else:
                selected = q.argmax(get_state_index(state),applicable_actions)


    return selected
import pygame
clock = pygame.time.Clock()
BLUE = ( 2, 157, 175)
BLUE_BRIGHT = ( 61, 58, 254)
BRIGHT = (186, 99, 69)
YELLOW = ( 255, 228, 135)
ORANGE = (240,124,25)
RED = ( 217, 69, 95)
GREY = (75, 76, 78)
GREEN = ( 86, 201, 123)
D_GREY = (93, 99, 96)
L_GREY = (158, 156, 152)
VL_GREY = (199, 189, 189)

def render(screen,world,state,action):

    al_y, al_x, al_b = state
    window_h, window_v = 800,800
    a_size = 20
    cell_size_x = 100
    cell_size_y = 100
    cell_border = 2
    grid_h = 5
    grid_v = 5
    grid_cx = int(window_h/2)-int((grid_h*cell_size_x)/2)
    grid_cy = int(window_v/2)-int((grid_v*cell_size_y)/2)
    grid_sx, grid_sy = grid_cx,grid_cy
    agent_x = grid_sx+al_x*cell_size_x+int(cell_size_x/2)
    agent_y = grid_sy+al_y*cell_size_y+int(cell_size_y/2)
    screen.fill(GREEN)
    # draw grid

    for y in range (grid_v):
        for x in range(grid_h):
            g_x = grid_sx+x*cell_size_x
            g_y = grid_sy + y * cell_size_y
            gc_x = g_x + int(cell_size_x/2)
            gc_y = g_y + int(cell_size_y/2)
            pygame.draw.rect(screen,BLUE,pygame.Rect(g_x,g_y,cell_size_x,cell_size_y))
            pygame.draw.rect(screen, YELLOW ,pygame.Rect(grid_sx + x * cell_size_x+cell_border, grid_sy + y * cell_size_y+cell_border, cell_size_x-cell_border*2,cell_size_y-cell_border*2))
            for s in range(2):
                newstate = [y,x,s]
                aactions = [0,1,2,3]
                axn = []
                for kx in world.applicable_actions(newstate):
                    if kx in range(4):
                        axn.append(kx)
                newqt = q.qtable[get_state_index(newstate), axn]
                interpolated_q_table = np.interp(newqt, (newqt.min(), newqt.max()), (0, cell_size_x / 2))

                for a in axn:
                    indx = axn.index(a)
                    if a == EAST:
                        pygame.draw.line(screen, RED, (gc_x, gc_y), (gc_x + interpolated_q_table[indx], gc_y))
                    elif a == WEST:
                        pygame.draw.line(screen, RED,(gc_x, gc_y), (gc_x - interpolated_q_table[indx], gc_y))
                    elif a == NORTH:
                        pygame.draw.line(screen,RED, (gc_x, gc_y), (gc_x, gc_y-interpolated_q_table[indx]))
                    elif a == SOUTH:
                        pygame.draw.line(screen, RED, (gc_x, gc_y), (gc_x, gc_y+interpolated_q_table[indx]))

    # draw agent state
    pygame.draw.circle(screen,RED,(agent_x,agent_y),a_size)
    if al_b == 1:
        pygame.draw.circle(screen, YELLOW,(agent_x, agent_y), int(a_size/2))


    # draw nex action
    # pygame.draw.circle(screen, RED, (
    # grid_sx + al_x * cell_size_x + int(cell_size_x / 2), grid_sy + al_y * cell_size_y + int(cell_size_y / 2)), a_size)

    # draw Pickup Points
    # setting fonts
    # for y,x in world.pickup_points:
    #     for c in world.pickup_items_count:
    #         for i in range(c):
    #             px = grid_sx + x * cell_size_x + i* 20
    #             py = grid_sy + y * cell_size_y
    #             pygame.draw.circle(screen,BLUE,(px,py),8)
    package_offset = 15
    for y,x in world.pickup_points:
        itemindex = world.pickup_points.index([y,x])
        for i in range(world.pickup_items_count[itemindex]):
            px = grid_sx + x * cell_size_x + i * package_offset + 20
            py = grid_sy + y * cell_size_y + 20
            pygame.draw.circle(screen, BLUE, (px, py), 8)
    for y,x in world.dropoff_points:
        itemindex = world.dropoff_points.index([y,x])
        for i in range(world.dropoff_items_count[itemindex]):
            px = grid_sx + x * cell_size_x + i * package_offset + 20
            py = grid_sy + y * cell_size_y + 20
            pygame.draw.circle(screen, RED, (px, py), 8)

    # font = pygame.font.SysFont("comicsansms",18)
    # text = font.render(u"→", True, D_GREY)
    # screen.blit(text, (100,100))

    pygame.display.update()


    return

def main():
    #
    # if ENABLE_GUI:
    pygame.init()
    size = width,height = (800,800)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PD World")

    starting_state = [0, 4, 0]
    pickup_points = [[0, 0], [2, 2], [4, 4]]
    dropoff_points = [[4,0], [4, 2], [1, 4]]
    pickup_items_count = [5, 5, 5]
    dropoff_items_count = [0, 0, 0]

    world = PDWORLD(starting_state, pickup_points, dropoff_points,pickup_items_count,dropoff_items_count)
    alpha = 0.02
    gamma = 0.98
    EPISODES = 500
    STEPS = 400
    sk = 0
    tiktok =60
    for e in range(EPISODES):
        global s
        global a
        global a_
        global s_
        s = starting_state
        global totalReward
        totalReward = 0
        a = select_action(world, s, PEXPLOIT)
        # while True:
        steps_count = 0
        world.pickup_items_count = [5,5,5]
        world.dropoff_items_count = [0,0,0]
        while True:
        # for step in range(STEPS):
            steps_count += 1
            s_,r,done = apply(world,s,a)

            # if sk==5:
            #     exit()
            if e%100 == 0:
            #     ENABLE_GUI = True
            # if ENABLE_GUI:
                render(screen,world,s,a)
                clock.tick(tiktok)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            sk += 1
            a_ = select_action(world,s_,PEXPLOIT)
            qsa = q.value(get_state_index(s),a)
            old_qsa_tests =copy.deepcopy(q.value(get_state_index(s),a))
            qs_a_= q.value(get_state_index(s_), a_)
            q.qtable[get_state_index(s)][a] = qsa + alpha * (r + gamma*qs_a_-qsa)
            # print("updating ",s,a," to ",  q.qtable[get_state_index(s)][a], " from ", old_qsa_tests )

            # print(world.pickup_items_count,world.dropoff_items_count)
            s = s_
            a = a_

            if done:
                print("Done with ",steps_count, " steps")
                break

        print("Episode: ", e, " done")
    # print(q)
    # action_string = ['EAST','WEST','NORTH','SOUTH','PICKUP','DROPOFF']
    # for i in range(5):
    #     for j in range(5):
    #         for k in range(2):
    #             state = [i,j,k]
    #             # ap = world.applicable_actions(state)
    #             # print(ap)
    #             print(state,end=' ')
    #             for a in range(6):
    #                 print(q.qtable[get_state_index(state)][a],end=' ')
    #             print()
    # while True:
    #     continue
if __name__ == '__main__':
    main()