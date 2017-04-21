# https://www.alphagrader.com/courses/6/assignments/17
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
