def swap_list(inputs):
	if len(inputs) % 2 == 0:
		m = int(len(inputs) / 2) - 1
	else:
		m = int(len(inputs) / 2 )

	last = len(inputs) - 1
	inputs[last], inputs[m] = inputs[m], inputs[last]

	return inputs

