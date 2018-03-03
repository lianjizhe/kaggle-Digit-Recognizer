import pandas as pd
import numpy as np
import logging

def save_csv_data_to_npy():
    data = pd.read_csv('data/train.csv')
    train_data = data.values[0:, 1:]
    train_label = data.values[0:, 0]
    logging.info('train_data.shape:{} train_label.shape:{}'.format(
        train_data.shape, train_label.shape))
    np.save('data/train_data.npy', train_data)
    np.save('data/train_label.npy', train_label)

    data = pd.read_csv('data/test.csv')
    test_data = data.values[0:, 0:]
    logging.info('test_data.shape:{}'.format(test_data.shape))
    np.save('data/test_data.npy', test_data)

def main(args):
    command = args['command']
    eval('{}()'.format(command))
