#!/usr/bin/env python3
import socket
import numpy as np
import json
import time
import random

import csv

HOST = '172.20.10.4'  # Standard loopback interface address
PORT = 2000  # Port to listen on (use ports > 1023)

t = 0


fieldnames = ["time", "acc_x", "acc_y", "acc_z"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:

            with open('data.csv', 'a') as csv_file:

                data = conn.recv(1024).decode('utf-8')
                # print('Received from socket server : ', data)

                ix,iy,iz, end = data.find("x"),data.find("y"),data.find("z"), data.find("_e")

                ax = int(data[ix+1: iy])
                ay = int(data[iy+1: iz])
                az = int(data[iz+1: end])

                print(ax, ay, az)

                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                info = {
                    "time": t,
                    "acc_x": ax,
                    "acc_y": ay,
                    "acc_z": az
                }

                csv_writer.writerow(info)

                t += 1

            # time.sleep(1)

                

            