# import random
# from datetime import datetime, timedelta

# # Base values for simulation
# team_id = "2024-CANSAT-ASI-023"
# start_time = datetime.strptime("00:00:00", "%H:%M:%S")
# start_gnss_time = datetime.strptime("15:00:00", "%H:%M:%S")
# packet_count = 0
# flight_state = 0
# altitude = 0
# gnss_alt = 0
# lines = []

# for i in range(200):
#     # Time stamping and GNSS time (increment by one second per packet)
#     current_time = (start_time + timedelta(seconds=i)).strftime("%H:%M:%S")
#     current_gnss_time = (start_gnss_time + timedelta(seconds=i)).strftime("%H:%M:%S")
    
#     # Incrementing packet count
#     current_packet = packet_count + i

#     # Static or near-static values with slight random variations

#     if i in range(10,99):
#         altitude = altitude + random.randint(0,10)
#     elif i in range(99,200):
#         altitude = altitude + random.randint(-5,0)

#     pressure = f"{99554 + random.randint(-50,50)}"
#     temp = f"{22.9 + random.uniform(-5,10):.1f}"
#     voltage = f"{7.42 + random.uniform(-0.05,0.05):.2f}"
#     gnss_lat = f"{28.6122 + random.uniform(-0.001, 0.001):.4f}"
#     gnss_long = f"{77.0365 + random.uniform(-0.001, 0.001):.4f}"

    
#     if i in range(11,100):
#         gnss_alt = gnss_alt + random.randint(0,10)
#     elif i in range(100,200):
#         gnss_alt = gnss_alt + random.randint(-5,0)


#     if i in range(0,7):
#         gnss_sats = "9"
#     elif i in range(7,100):
#         gnss_sats = f"{7 + random.randint(-2,7)}"
#     else:
#         gnss_sats = f"{7 + random.randint(-5,0)}"

    
#     acc_r = f"{16.17 + random.uniform(-0.1, 0.1):.2f}"
#     acc_p = f"{-10.81 + random.uniform(-0.1, 0.1):.2f}"
#     acc_y = f"{0.25 + random.uniform(-0.05, 0.05):.2f}"
    
#     gyro_r = f"{-0.05 + random.uniform(-0.02, 0.02):.2f}"
#     gyro_p = f"{-0.01 + random.uniform(-0.02, 0.02):.2f}"
#     gyro_y = f"{0.10 + random.uniform(-0.02, 0.02):.2f}"
    
#     if i in range(0,2):
#         flight_state = "0"
#     elif i in range(2,6):
#         flight_state = "1"
#     elif i in range(6,9):
#         flight_state = "2"
#     elif i in range(9,99):
#         flight_state = "3"
#     elif i in range(99,105):
#         flight_state = "4"
#     else:
#         flight_state = "5"

#     tvoc = f"{random.randint(0,20)}"
#     eco2 = f"{413 + random.randint(-50,50)}"
    
#     # Construct the packet string
#     packet = (
#         f"<{team_id},{current_time},{current_packet},{altitude},"
#         f"{pressure},{temp},{voltage},{current_gnss_time},"
#         f"{gnss_lat},{gnss_long},{gnss_alt},{gnss_sats},"
#         f"{acc_r},{acc_p},{acc_y},{gyro_r},{gyro_p},{gyro_y},"
#         f"{flight_state},{tvoc},{eco2}>"
#     )
#     lines.append(packet)

# # Write the packets to a file
# with open("data_packets.txt", "w") as f:
#     for line in lines:
#         f.write(line + "\n")


with open("data_packets.txt",'r') as file:
    content = file.read()

print(content)
