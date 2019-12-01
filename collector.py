from rospy_message_converter import message_converter
import rospy, json, yaml
from std_msgs.msg import String 
from sensor_msgs.msg import Imu
import ipdb, time

sampling_duration = 10 # 10secs

mydata = list() 

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + data.data) 
    mydata.append(data) 

rospy.init_node('get_imu_data')
rospy.Subscriber('imu0', Imu, callback) 
# rospy.spin() 

time.sleep(30)

mydata_json = list() 
for mes in mydata: 
    dict_data = message_converter.convert_ros_message_to_dictionary(
            mes)
    mydata_json.append( dict_data ) 

with open('mydata.json', 'w') as fout: 
    json.dump({'mydata': mydata_json}, fout, indent=4) 
    
    