# Code from Chapter 11 of Machine Learning: An Algorithmic Perspective (2nd Edition)
# by Stephen Marsland (http://stephenmonika.net)

# You are free to use, change, or redistribute the code in any way you wish for
# non-commercial purposes, but please maintain the name of the original author.
# This code comes with no warranty of any kind.

# Stephen Marsland, 2008, 2014

# The basic SARSA algorithm with the Cliff example

import numpy as np


def SARSA_cliff():
    R = -np.ones((4, 7, 4))
    R[0, :, 0] = -np.inf
    R[0, 6, 0] = 0
    R[:, 0, 3] = -np.inf
    R[3, :, 2] = -np.inf
    R[:, 6, 1] = -np.inf
    R[1, 1:6, 0] = -100
    R[0, 0, 1] = -100
    R[0, 6, 3] = -100

    t = np.zeros((4, 7, 4, 2))
    for i in range(4):
        for j in range(7):
            for k in range(4):
                if k == 2:
                    if i < 3:
                        t[i, j, k, 0] = i + 1
                        t[i, j, k, 1] = j
                    else:
                        t[i, j, k, 0] = i
                        t[i, j, k, 1] = j
                elif k == 1:
                    if j < 6:
                        t[i, j, k, 0] = i
                        t[i, j, k, 1] = j + 1
                    else:
                        t[i, j, k, 0] = i
                        t[i, j, k, 1] = j
                    if i == 0 and j == 0:
                        t[i, j, k, 0] = 0
                        t[i, j, k, 1] = 0
                elif k == 0:
                    if i == 0 and j == 6:
                        # Finished
                        t[i, j, k, 0] = 0
                        t[i, j, k, 1] = 0
                    if i > 0:
                        t[i, j, k, 0] = i - 1
                        t[i, j, k, 1] = j
                    else:
                        t[i, j, k, 0] = i
                        t[i, j, k, 1] = j

                    if i == 1 and 1 <= j <= 5:
                        t[i, j, k, 0] = 0
                        t[i, j, k, 1] = 0
                else:
                    if j > 0:
                        t[i, j, k, 0] = i
                        t[i, j, k, 1] = j - 1
                    else:
                        t[i, j, k, 0] = i
                        t[i, j, k, 1] = j
                    if i == 0 and j == 6:
                        t[i, j, k, 0] = 0
                        t[i, j, k, 1] = 0

    # print t[:,:,3,0] ,t[:,:,3,1]

    Q = np.random.random_sample(np.shape(R)) * 0.1 - 0.05
    mu = 0.7
    gamma = 0.4
    epsilon = 0.05
    nits = 0

    while nits < 1000:
        # Pick initial state
        s = np.array([0, 0])  # np.array([np.random.randint(4),np.random.randint(7)])

        r = -np.inf
        while r == -np.inf:
            # epsilon-greedy
            if (np.random.rand() < epsilon):
                a = np.random.randint(4)
            else:
                a = np.argmax(Q[s[0], s[1], :])
            r = R[s[0], s[1], a]

        # print s, np.shape(s)
        # print np.shape(Q), np.shape(Q[s[0],s[1],:])
        inEpisode = 1
        # Stop when the accepting state is reached
        while inEpisode:
            r = R[s[0], s[1], a]
            # print "r = ", r
            sprime = t[s[0], s[1], a, :]
            # print "sprime",sprime

            rprime = -np.inf
            while rprime == -np.inf:
                # epsilon-greedy
                if (np.random.rand() < epsilon):
                    aprime = np.random.randint(4)
                else:
                    aprime = np.argmax(Q[sprime[0], sprime[1], :])
                rprime = R[sprime[0], sprime[1], aprime]

            # print aprime
            # print "here", Q[sprime[0],sprime[1],aprime], Q[s[0],s[1],a], s, a

            Q[s[0], s[1], a] += mu * (r + gamma * Q[sprime[0], sprime[1], aprime] - Q[s[0], s[1], a])
            # print "there"
            s = sprime
            a = aprime
            r = rprime
            if s[0] == 0 and s[1] == 6 and a == 0:
                # Have reached endpoint
                inEpisode = 0
        nits = nits + 1
        print(nits)
    print(Q)
    return Q, R, t


def SARSAgo(Q, R, t):
    s = np.array([0, 0])
    rtotal = 0
    finished = 0
    epsilon = 0.05
    while not (finished):
        r = -np.inf
        while r == -np.inf:
            # epsilon-greedy
            if (np.random.rand() < epsilon):
                a = np.random.randint(4)
            else:
                a = np.argmax(Q[s[0], s[1], :])
            r = R[s[0], s[1], a]
        s = t[s[0], s[1], a, :]
        # print s
        rtotal += r
        if s[0] == 0 and s[1] == 6 and a == 0:
            finished = 1
    print("Total cost = ", rtotal)
    return rtotal


Q, R, t = SARSA_cliff()
cost = SARSAgo(Q, R, t)
cost = SARSAgo(Q, R, t)
cost = SARSAgo(Q, R, t)
cost = SARSAgo(Q, R, t)
cost = SARSAgo(Q, R, t)
