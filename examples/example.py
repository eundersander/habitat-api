#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import habitat


def example():
    # Note: Use with for the example testing, doesn't need to be like this on the README

    with habitat.Env(
        config=habitat.get_config("configs/tasks/pointnav.yaml")
    ) as env:
        print("Environment creation successful")

        count_episodes = 0
        while count_episodes < 8:
            observations = env.reset()

            print("Agent stepping around inside environment.")
            count_steps = 0
            while not env.episode_over:
                while True:
                    action = env.action_space.sample()
                    if count_steps >= 1000 or action['action'] != 'STOP':
                        break
                # print("action: {}".format(action))
                observations = env.step(action)
                count_steps += 1
            print("Episode finished after {} steps.".format(count_steps))
            count_episodes += 1

    env.close()


if __name__ == "__main__":
    example()
