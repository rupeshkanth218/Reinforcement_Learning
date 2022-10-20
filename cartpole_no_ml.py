import time
import gym
import random

env = gym.make('CartPole-v0')

for episode in range(5):
	env.reset()
	done=False
	for step in range(60):
		env.render()
		
		action = env.action_space.sample()
		s,r,done,_=env.step(action)
		if done:
			print(done)
			time.sleep(1)
			break
	
env.close()
