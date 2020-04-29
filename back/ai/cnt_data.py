#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
base_dir = os.getcwd()
test_dir = os.path.join(base_dir, 'dataset', 'test')
train_dir = os.path.join(base_dir, 'dataset', 'train')


for name in os.walk(test_dir).__next__()[1]:
    now_path = os.path.join(test_dir, name)
    a = os.walk(now_path).__next__()
    print(name, len(a[2]))

print('________________________train______________________')
for name in os.walk(train_dir).__next__()[1]:
    now_path = os.path.join(train_dir, name)
    a = os.walk(now_path).__next__()
    print(name, len(a[2]))

