def which_is_smaller(time_pair):

	def equal_time_range(first_time, second_time):

		if first_time.startswith('12'):
			first_time = first_time.replace('12', '00')
		if second_time.startswith('12'):
			second_time = second_time.replace('12', '00')

		# if 'AM' in first_time:
		# 	if first_time.startswith('12'):
		# 		if not second_time.startswith('12'):
		# 			return 'First'
		# 		elif second_time.startswith('12'):
		# 			mins_first_time = int(first_time[3:5])
		# 			mins_sec_time = int(second_time[3:5])
		# 			if mins_first_time < mins_sec_time:
		# 				return 'First'
		# 			else:
		# 				return 'Second'
		# 	else:
		# 		if second_time.startswith('12'):
		# 			if not first_time.startswith('12'):
		# 				return 'Second'
		# 		elif first_time.startswith('12'):
		# 			mins_first_time = int(first_time[3:5])
		# 			mins_sec_time = int(second_time[3:5])
		# 			if mins_first_time < mins_sec_time:
		# 				return 'First'
		# 			else:
		# 				return 'Second'

		if len(first_time) < 7:
			first_time = '0' + first_time
		if len(second_time) < 7:
			second_time = '0' + second_time

		time_one = int(first_time[:5].replace(':', ''))
		time_two = int(second_time[:5].replace(':', ''))
		if time_one > time_two:
			return 'Second'
		else:
			return 'First'

	first_time, second_time = time_pair
	# print('first time: ', first_time[5:7])
	# print('second time: ', second_time[5:7])
	if 'AM' in first_time:
		if 'PM' in second_time:
			return 'First'
		elif 'AM' in second_time:
			return equal_time_range(first_time, second_time)
	elif 'PM' in first_time:
		if 'AM' in second_time:
			return 'Second'
		elif 'PM' in second_time:
			return equal_time_range(first_time, second_time)

if __name__ == '__main__':
	num_of_queries = int(input())
	time_list = [raw_input().split(' ') for i in range(num_of_queries)]
	# print(time_list)
	for pair in time_list:
		print(which_is_smaller(pair))


