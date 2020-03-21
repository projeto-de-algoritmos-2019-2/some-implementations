from collections import defaultdict

peso = {1:4, 2:2, 3:1, 4:3}
valor = {1:500, 2:400, 3:300, 4:450}
cap = 5 # capacidade máxima da mochila
objs = 4 # qnt de objetos

table = defaultdict(lambda:defaultdict(lambda:0))

# cm: capacidade da mochila
for cm in range(1, cap+1):

	# para cada objeto
	for obj in range(1, objs+1):

		# vso: valor sem o objeto
		best_value = vso = table[obj-1][cm]

		p_obj = peso[obj]

		# print('obj',obj, 'p_obj', p_obj)

		if p_obj <= cm:

			# vco: valor com o objeto
			vco = valor[obj] + table[obj-1][ cm-p_obj ]

			if vco > vso:
				best_value = vco


		table[obj][cm] = best_value

		print(table[obj][cm], end=' ')
	print()

	print('best', table[objs][cap])
