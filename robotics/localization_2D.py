from pprint import pprint

def sense(p, Z, sensor_right):
	q = [[0 for x in range(0,len(p[0]))] for y in range(0,len(p))]
	for i in range(len(p)):
		for j in range(len(p[0])):
			hit = (Z == colors[i][j])
			q[i][j] = p[i][j]*(hit*sensor_right+(1-hit)*(1-sensor_right))
	s = sum(sum(x) for x in q)
	for i in range(len(p)):
		for j in range(len(p[0])):
			q[i][j] = q[i][j]/s
	return q
	
def move(p, U, p_move):
	q = [[0 for x in range(0,len(p[0]))] for y in range(0,len(p))]
	for i in range(len(p)):
		for j in range(len(p[0])):
			s = p[i][j]*(1-p_move)
			s += p[(i-U[0])%len(p)][(j-U[1])%len(p[0])]*p_move
			q[i][j] = s
	return q
	
def localize(colors,measurements,motions,sensor_right,p_move):
	# initializes p to a uniform distribution over a grid of the same dimensions as colors
	pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
	p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
	
	for i in range(0, len(motions)):
		p = move(p,motions[i],p_move)
		p = sense(p,measurements[i],sensor_right)
	return p
	
colors = [['G', 'G', 'G'],
          ['G', 'R', 'G'],
          ['G', 'G', 'G'],
		  ['G', 'G', 'G']]
measurements = ['R','G']
motions = [[1,0],[1,0]]
sensor_right = 0.99
p_move = 0.99
p = localize(colors,measurements,motions,sensor_right,p_move)
pprint(p)
