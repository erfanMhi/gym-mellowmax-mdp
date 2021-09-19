from gym.envs.registration import register

register(
    id='mellowmaxmdp-v0',
    entry_point='gym_mellowmaxmdp.envs:MellowmaxMdp',
)
