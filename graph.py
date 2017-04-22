[18:10, 21/4/2017] Erik Ibarra: # https://www.alphagrader.com/courses/6/assignments/17
import fileinput

initial_w = 0.1
learning_rate = 0.03

def read_input():
    lines = []
    step = 1
    data_set = []
    test_set = []
    m = 0
    for line in fileinput.input():
        lines.append(line.strip())
    for line in lines:
        if step == 2:
            m = int(line)
        if step >= 4 and step < 4+m:
            data_set.append([float(x) for x in line.split(',')])
        if step >= 4+m:
            test_set.append([float(x) for x in line.split(',')])
        step += 1
    return data_set, test_set

def split_data(data):
    ds = []
    ls = []
    for d in data:
        ds.append(d[:-1] + [1]) # BIAS CONSTANT
        ls.append(d[-1])
    return ds, ls

def step_activation(output):
    if output >= 0.0:
        return 1.0
    return 0.0

def dot(u,v):
    return sum([x[0] * x[1] for x in zip(u,v)])

def main():
    data, test = read_input()
    data, labels = split_data(data)
    W = [initial_w] * len(data[0])
    n_iterations = 5
    for iteration in range(n_iterations):
        for row, label in zip(data, labels):
            output = dot(W,row)
            activation = step_activation(output)
            err = learning_rate * (label - activation)
            update = [err * r for r in row]
            W = [ w+update[i] for i,w in enumerate(W)]
    for row in test:
        x = dot(W,row + [1])
        print(step_activation(x))

if _name_ == '_main_':
    main()
[19:00, 21/4/2017] Erik Ibarra: # https://www.alphagrader.com/courses/6/assignments/17
import fileinput
import matplotlib.pyplot as plt
import numpy as np
initial_w = 0.1
learning_rate = 0.03
line = plt.figure()

def read_input():
    lines = []
    step = 1
    data_set = []
    test_set = []
    m = 0
    for line in fileinput.input():
        lines.append(line.strip())
    for line in lines:
        if step == 2:
            m = int(line)
        if step >= 4 and step < 4+m:
            data_set.append([float(x) for x in line.split(',')])
        if step >= 4+m:
            test_set.append([float(x) for x in line.split(',')])
        step += 1
    return data_set, test_set

def split_data(data):
    ds = []
    ls = []
    for d in data:
        ds.append(d[:-1] + [1]) # BIAS CONSTANT
        ls.append(d[-1])
    return ds, ls

def step_activation(output):
    if output >= 0.0:
        return 1.0
    return 0.0

def dot(u,v):
    return sum([x[0] * x[1] for x in zip(u,v)])

def main():
    data, test = read_input()
    data, labels = split_data(data)
    W = [initial_w] * len(data[0])
    n_iterations = 5
    xs = []
    xs1 = []
    ys = []
    ys1 = []
    for i,d in enumerate(data):
        if labels[i] == 0:
            xs1.append(d[0])
            ys1.append(d[1])
        else:
            xs.append(d[0])
            ys.append(d[1])
    plt.scatter(xs, ys, alpha=.8, s=20)
    plt.scatter(xs1, ys1, alpha=.5, s=30)
    plt.show()
    for iteration in range(n_iterations):
        for row, label in zip(data, labels):
            output = dot(W,row)
            activation = step_activation(output)
            err = learning_rate * (label - activation)
            update = [err * r for r in row]
            W = [ w+update[i] for i,w in enumerate(W)]
    if len(test) > 0:
        for row in test:
            x = dot(W,row + [1])
            print(int(step_activation(x)))
    else:
        print('no solution found')
if __name__ == '__main__':
    main()
