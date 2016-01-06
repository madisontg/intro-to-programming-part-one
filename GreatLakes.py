#Madison Thorburn-Gundlach
#August 31, 2015

#How deep would the water contained in the Great Lakes be
#if it were spread evenly aross the 48 contiguous U.S. states?

#Establish variables
water_volume_km_float = 22810
area_of_48_contiguous_US_states_km_float = 8080464.3

#Solve known volume equation for depth
depth_km_float = water_volume_km_float/area_of_48_contiguous_US_states_km_float

#Convert depth to meters "so it doesn't look gross"
depth_m_float = depth_km_float * 1000

#Convert depth to feet because we are in America
depth_f_float = depth_m_float * 3.28084

print ("The depth in meters is ", depth_m_float,\
       "and the depth in feet (because we are in America) is ", depth_f_float)
