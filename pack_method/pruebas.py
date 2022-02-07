import os
import pickle
with open("token_gmail_v1.pickle", 'rb') as token:
    cred = pickle.load(token)
    print ([k for k in cred])
