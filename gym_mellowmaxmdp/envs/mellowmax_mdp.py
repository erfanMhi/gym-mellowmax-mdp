import gym
import numpy as np

from gym import error, spaces, utils
from gym.utils import seeding
from gym.envs.toy_text import discrete


A = 0
B = 1


class MellowmaxMdp(discrete.DiscreteEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        
        # Defining the number of actions
        nA = 2
        nS = 1

        # Defining the reward system and dynamics of RiverSwim environment
        P, isd = self.__init_dynamics(nS, nA)
        
        super(MellowmaxMdp, self).__init__(nS, nA, P, isd)

    def __init_dynamics(self, nS, nA):
        
        # P[s][a] == [(probability, nextstate, reward, done), ...]
        P = {}
        for s in range(nS):
            P[s] = {a: [] for a in range(nA)}

        # Rewarded Transitions
        P[0][A] = [(0.66, 0, 0.122, 0), (.34, 1, 0.122, 1)]
        P[0][B] = [(0.99, 0, 0.033, 0), (.01, 1, 0.033, 1)]
        
        isd = np.zeros(nS)
        isd[0] = 1.
        
        return P, isd

    def render(self, mode='human'):
        pass

    def close(self):
        pass