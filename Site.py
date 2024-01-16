'''
Site Connectivity Checker
-------------------------------------------------------------
Enter websites as http(s)://www.yourwebsite.com
'''

import urllib.request
import tkinter as tk

def test_connectivity():
    window = tk.Tk()
    window.geometry('600x400')
    head = tk.Label(window, text='Website Connectivity Checker',
                  font=('Calibri 15'))