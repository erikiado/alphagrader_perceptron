# https://www.alphagrader.com/courses/6/assignments/17
import fileinput
import numpy as np

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
            data_set.append(np.array([float(x) for x in line.split(',')], dtype=float))
        if step >= 4+m:
            test_set.append(np.array([float(x) for x in line.split(',')], dtype=float))
        step += 1
    return data_set, test_set

def split_data(data):
    ds = []
    ls = []
    for d in data:
        ds.append(np.append(d[:-1],1)) # BIAS CONSTANT
        ls.append(d[-1])
    return ds, ls

def step_activation(output):
    if output >= 0.0:
        return 1.0
    return 0.0

def main():
    data, test = read_input()
    data, labels = split_data(data)
    W = np.array([initial_w] * len(data[0]),dtype=float)
    n_iterations = 10
    for iteration in range(n_iterations):
        for row, label in zip(data, labels):
            output = np.dot(W,row)
            activation = step_activation(output)
            update = learning_rate * (label - activation) * row
            W += update
    for row in test:
        x = np.dot(W,np.append(row,1))
        print(step_activation(x))

if __name__ == '__main__':
    main()
