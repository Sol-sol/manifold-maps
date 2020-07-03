


header = ''
lsroom = []
scale = 1

def linkrgt(id0, id1, a, b, c, d, z, y):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	z *= scale
	y *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(+v.px < room%d.w) {\n' % id0
	r[0] += '\t\tView door = View_through_rgt(v, room%d.w, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px -= room%d.w + room%d.w;\n' % (id0, id1)
	r[0] += '\t\tdoor.py -= %ff;\n' % y
	r[0] += '\t\tdoor.pz -= %ff;\n' % z
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.pz >= %ff+d)\n' % a
	r[1] += '\tif(v.pz <= %ff-d)\n' % b
	r[1] += '\tif(v.py >= %ff+d)\n' % c
	r[1] += '\tif(v.py <= %ff-d)\n' % d
	r[1] += '\tif(v.px + x > room%d.w - w) {\n' % id0
	r[1] += '\t\tif(v.px + x > room%d.w) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px -= room%d.w + room%d.w;\n' % (id0, id1)
	r[1] += '\t\t\tv.py -= %ff;\n' % y
	r[1] += '\t\t\tv.pz -= %ff;\n' % z
	r[1] += '\t\t\treturn room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.pz < %ff+d) v.pz = %ff+d, v.vz = 0;\n' % (a, a)
	r[1] += '\t\tif(v.pz > %ff-d) v.pz = %ff-d, v.vz = 0;\n' % (b, b)
	r[1] += '\t\tif(v.py < %ff+d) v.py = %ff+d, v.vy = 0;\n' % (c, c)
	r[1] += '\t\tif(v.py > %ff-d) v.py = %ff-d, v.vy = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'

def linklft(id0, id1, a, b, c, d, z, y):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	z *= scale
	y *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(-v.px < room%d.w) {\n' % id0
	r[0] += '\t\tView door = View_through_lft(v, -room%d.w, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px += room%d.w + room%d.w;\n' % (id0, id1)
	r[0] += '\t\tdoor.py -= %ff;\n' % y
	r[0] += '\t\tdoor.pz -= %ff;\n' % z
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.pz >= %ff+d)\n' % a
	r[1] += '\tif(v.pz <= %ff-d)\n' % b
	r[1] += '\tif(v.py >= %ff+d)\n' % c
	r[1] += '\tif(v.py <= %ff-d)\n' % d
	r[1] += '\tif(v.px + x < -room%d.w + w) {\n' % id0
	r[1] += '\t\tif(v.px + x < -room%d.w) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px += room%d.w + room%d.w;\n' % (id0, id1)
	r[1] += '\t\t\tv.py -= %ff;\n' % y
	r[1] += '\t\t\tv.pz -= %ff;\n' % z
	r[1] += '\t\t\treturn room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.pz < %ff+d) v.pz = %ff+d, v.vz = 0;\n' % (a, a)
	r[1] += '\t\tif(v.pz > %ff-d) v.pz = %ff-d, v.vz = 0;\n' % (b, b)
	r[1] += '\t\tif(v.py < %ff+d) v.py = %ff+d, v.vy = 0;\n' % (c, c)
	r[1] += '\t\tif(v.py > %ff-d) v.py = %ff-d, v.vy = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'

def linkuwd(id0, id1, a, b, c, d, x, z):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	x *= scale
	z *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(+v.py < room%d.h) {\n' % id0
	r[0] += '\t\tView door = View_through_uwd(v, room%d.h, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px -= %ff;\n' % x
	r[0] += '\t\tdoor.py -= room%d.h + room%d.h;\n' % (id0, id1)
	r[0] += '\t\tdoor.pz -= %ff;\n' % z
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.px >= %ff+d)\n' % a
	r[1] += '\tif(v.px <= %ff-d)\n' % b
	r[1] += '\tif(v.pz >= %ff+d)\n' % c
	r[1] += '\tif(v.pz <= %ff-d)\n' % d
	r[1] += '\tif(v.py + y > room%d.h - w) {\n' % id0
	r[1] += '\t\tif(v.py + y > room%d.h) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px -= %ff;\n' % x
	r[1] += '\t\t\tv.py -= room%d.h + room%d.h;\n' % (id0, id1)
	r[1] += '\t\t\tv.pz -= %ff;\n' % z
	r[1] += '\t\t\treturn room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.px < %ff+d) v.px = %ff+d, v.vx = 0;\n' % (a, a)
	r[1] += '\t\tif(v.px > %ff-d) v.px = %ff-d, v.vx = 0;\n' % (b, b)
	r[1] += '\t\tif(v.pz < %ff+d) v.pz = %ff+d, v.vz = 0;\n' % (c, c)
	r[1] += '\t\tif(v.pz > %ff-d) v.pz = %ff-d, v.vz = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'

def linkdwn(id0, id1, a, b, c, d, x, z):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	x *= scale
	z *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(-v.py < room%d.h) {\n' % id0
	r[0] += '\t\tView door = View_through_dwn(v, -room%d.h, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px -= %ff;\n' % x
	r[0] += '\t\tdoor.py += room%d.h + room%d.h;\n' % (id0, id1)
	r[0] += '\t\tdoor.pz -= %ff;\n' % z
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.px >= %ff+d)\n' % a
	r[1] += '\tif(v.px <= %ff-d)\n' % b
	r[1] += '\tif(v.pz >= %ff+d)\n' % c
	r[1] += '\tif(v.pz <= %ff-d)\n' % d
	r[1] += '\tif(v.py + y < -room%d.h + w) {\n' % id0
	r[1] += '\t\tif(v.py + y < -room%d.h) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px -= %ff;\n' % x
	r[1] += '\t\t\tv.py += room%d.h + room%d.h;\n' % (id0, id1)
	r[1] += '\t\t\tv.pz -= %ff;\n' % z
	r[1] += '\t\t\treturn room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.px < %ff+d) v.px = %ff+d, v.vx = 0;\n' % (a, a)
	r[1] += '\t\tif(v.px > %ff-d) v.px = %ff-d, v.vx = 0;\n' % (b, b)
	r[1] += '\t\tif(v.pz < %ff+d) v.pz = %ff+d, v.vz = 0;\n' % (c, c)
	r[1] += '\t\tif(v.pz > %ff-d) v.pz = %ff-d, v.vz = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'
	
	r[2] += '\tif(v.px >= %ff)\n' % a
	r[2] += '\tif(v.px <= %ff)\n' % b
	r[2] += '\tif(v.pz >= %ff)\n' % c
	r[2] += '\tif(v.pz <= %ff) {\n' % d
	r[2] += '\t\tv.px -= %ff;\n' % x
	r[2] += '\t\tv.py += room%d.h + room%d.h;\n' % (id0, id1)
	r[2] += '\t\tv.pz -= %ff;\n' % z
	r[2] += '\t\treturn room%d_cast_down(v, d);\n' % id1
	r[2] += '\t}\n'

def linkfwd(id0, id1, a, b, c, d, x, y):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	x *= scale
	y *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(+v.pz < room%d.d) {\n' % id0
	r[0] += '\t\tView door = View_through_fwd(v, room%d.d, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px -= %ff;\n' % x
	r[0] += '\t\tdoor.py -= %ff;\n' % y
	r[0] += '\t\tdoor.pz -= room%d.d + room%d.d;\n' % (id0, id1)
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.px >= %ff+d)\n' % a
	r[1] += '\tif(v.px <= %ff-d)\n' % b
	r[1] += '\tif(v.py >= %ff+d)\n' % c
	r[1] += '\tif(v.py <= %ff-d)\n' % d
	r[1] += '\tif(v.pz + z > room%d.d - w) {\n' % id0
	r[1] += '\t\tif(v.pz + z > room%d.d) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px -= %ff;\n' % x
	r[1] += '\t\t\tv.py -= %ff;\n' % y
	r[1] += '\t\t\tv.pz -= room%d.d + room%d.d;\n' % (id0, id1)
	r[1] += '\t\t\tv = room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t\tv.vz -= room%d._d + room%d._d;\n' % (id0, id1) # velocity
	r[1] += '\t\t\treturn v;\n'
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.px < %ff+d) v.px = %ff+d, v.vx = 0;\n' % (a, a)
	r[1] += '\t\tif(v.px > %ff-d) v.px = %ff-d, v.vx = 0;\n' % (b, b)
	r[1] += '\t\tif(v.py < %ff+d) v.py = %ff+d, v.vy = 0;\n' % (c, c)
	r[1] += '\t\tif(v.py > %ff-d) v.py = %ff-d, v.vy = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'

def linkbwd(id0, id1, a, b, c, d, x, y):
	
	a *= scale
	b *= scale
	c *= scale
	d *= scale
	x *= scale
	y *= scale
	
	r = lsroom[id0]
	s = ', '.join(map(lambda x: "%ff" % x, (a, b, c, d)))
	
	r[0] += '\tif(-v.pz < room%d.d) {\n' % id0
	r[0] += '\t\tView door = View_through_bwd(v, -room%d.d, %s);\n' % (id0, s)
	r[0] += '\t\tdoor.px -= %ff;\n' % x
	r[0] += '\t\tdoor.py -= %ff;\n' % y
	r[0] += '\t\tdoor.pz += room%d.d + room%d.d;\n' % (id0, id1)
	r[0] += '\t\tif(--depth) room%d_render(door);\n' % id1
	r[0] += '\t\tdepth++;\n'
	r[0] += '\t}\n'
	
	r[1] += '\tif(v.px >= %ff+d)\n' % a
	r[1] += '\tif(v.px <= %ff-d)\n' % b
	r[1] += '\tif(v.py >= %ff+d)\n' % c
	r[1] += '\tif(v.py <= %ff-d)\n' % d
	r[1] += '\tif(v.pz + z < -room%d.d + w) {\n' % id0
	r[1] += '\t\tif(v.pz + z < -room%d.d) {\n' % id0
	r[1] += '\t\t\t*r = &room%d;\n' % id1
	r[1] += '\t\t\tv.px -= %ff;\n' % x
	r[1] += '\t\t\tv.py -= %ff;\n' % y
	r[1] += '\t\t\tv.pz += room%d.d + room%d.d;\n' % (id0, id1)
	r[1] += '\t\t\tv = room%d_update(v, r, w, d, dt);\n' % id1
	r[1] += '\t\t\tv.vz += room%d._d + room%d._d;\n' % (id0, id1) # velocity
	r[1] += '\t\t\treturn v;\n'
	r[1] += '\t\t}\n'
	r[1] += '\t\tv.px += x;\n'
	r[1] += '\t\tv.py += y;\n'
	r[1] += '\t\tv.pz += z;\n'
	
	r[1] += '\t\tif(v.px < %ff+d) v.px = %ff+d, v.vx = 0;\n' % (a, a)
	r[1] += '\t\tif(v.px > %ff-d) v.px = %ff-d, v.vx = 0;\n' % (b, b)
	r[1] += '\t\tif(v.py < %ff+d) v.py = %ff+d, v.vy = 0;\n' % (c, c)
	r[1] += '\t\tif(v.py > %ff-d) v.py = %ff-d, v.vy = 0;\n' % (d, d)
	
	r[1] += '\t\treturn v;\n'
	r[1] += '\t}\n'

def rgt(id0,z0,y0, id1,z1,y1, d,h):
	linkrgt(id0, id1, z0-d, z0+d, y0-h, y0+h, z0-z1, y0-y1)
	linklft(id1, id0, z1-d, z1+d, y1-h, y1+h, z1-z0, y1-y0)

def lft(id0,z0,y0, id1,z1,y1, d,h):
	linklft(id0, id1, z0-d, z0+d, y0-h, y0+h, z0-z1, y0-y1)
	linkrgt(id1, id0, z1-d, z1+d, y1-h, y1+h, z1-z0, y1-y0)

def uwd(id0,x0,z0, id1,x1,z1, w,h):
	linkuwd(id0, id1, x0-w, x0+w, z0-h, z0+h, x0-x1, z0-z1)
	linkdwn(id1, id0, x1-w, x1+w, z1-h, z1+h, x1-x0, z1-z0)

def dwn(id0,x0,z0, id1,x1,z1, w,h):
	linkdwn(id0, id1, x0-w, x0+w, z0-h, z0+h, x0-x1, z0-z1)
	linkuwd(id1, id0, x1-w, x1+w, z1-h, z1+h, x1-x0, z1-z0)

def fwd(id0,x0,y0, id1,x1,y1, w,h):
	linkfwd(id0, id1, x0-w, x0+w, y0-h, y0+h, x0-x1, y0-y1)
	linkbwd(id1, id0, x1-w, x1+w, y1-h, y1+h, x1-x0, y1-y0)

def bwd(id0,x0,y0, id1,x1,y1, w,h):
	linkbwd(id0, id1, x0-w, x0+w, y0-h, y0+h, x0-x1, y0-y1)
	linkfwd(id1, id0, x1-w, x1+w, y1-h, y1+h, x1-x0, y1-y0)

def room(w, h, d):
	
	w *= scale
	h *= scale
	d *= scale
	
	global header, lsroom
	index = len(lsroom)
	
	header+='fn void room%d_render(View v);\n' % index
	header+='fn View room%d_update(View v, Room **r'\
	', float w, float d, float dt);\n' % index
	header+='fn float room%d_cast_down(View v, float d);\n' % index
	header+='vr Room room%d =\n' %index
	header+='{ %f,%f,%f\n' % (w, h, d)
	header+=', 0, 0, 0\n'
	header+=', room%d_render\n' % index
	header+=', room%d_update\n' % index
	header+=', room%d_cast_down\n' % index
	header+='};\n'
	header+='\n'
	
	lsroom += [['', '', '']]
	return index

def out():
	index = 0
	print('// AUTOGEN //')
	print(header)
	for r, u, c in lsroom:
		s = "room%d.w, room%d.h, room%d.d" % (index, index, index)
		print('fn void room%d_render(View v) {' % index)
		print('\tif(v.xy[0] * v.xy[3] - v.xy[1] * v.xy[2] < 0) return;')
		print('\tif(v.yz[0] * v.yz[3] - v.yz[1] * v.yz[2] < 0) return;')
		print('\tif(v.zx[0] * v.zx[3] - v.zx[1] * v.zx[2] < 0) return;')
		# print('\tif(test_counter==select) {')
		print('\tglUniform4f(u_xy_id, v.xy[0], v.xy[1], v.xy[2], v.xy[3]);')
		print('\tglUniform4f(u_yz_id, v.yz[0], v.yz[1], v.yz[2], v.yz[3]);')
		print('\tglUniform4f(u_zx_id, v.zx[0], v.zx[1], v.zx[2], v.zx[3]);')
		#print('glUniform4f(u_xy_id,nor2(v.xy[0],v.xy[1]),nor2(v.xy[2],v.xy[3]));')
		#print('glUniform4f(u_yz_id,nor2(v.yz[0],v.yz[1]),nor2(v.yz[2],v.yz[3]));')
		#print('glUniform4f(u_zx_id,nor2(v.zx[0],v.zx[1]),nor2(v.zx[2],v.zx[3]));')
		# print('\tif(proggle) {')
		# print('\tglUniform4f(u_xy_id, 0, 0, 0, 0);')
		# print('\tglUniform4f(u_yz_id, 0, 0, 0, 0);')
		# print('\tglUniform4f(u_zx_id, 0, 0, 0, 0);')
		# print('\t}')
		print('\tglUniform4f(u_pos_id, v.px, v.py, v.pz, %d);' % index)
		# print('\tglUniform4f(u_pos_id, v.px, v.py, v.pz, %d + 0.1356f * _floorf(gtime + frand() * 0.5f));' % index)
		print('\tglUniform3f(u_scale_id, %s);' % s)
		print('\tglDrawArrays(GL_QUADS, 0, 4 * 6);')
		# print('\tglUniform3f(u_scale_id, -.1f, -.1f, -.1f);')
		# print('\tglDrawArrays(GL_QUADS, 0, 4 * 6);')
		
		# print('\tglUniform4f(u_xy_id, 0, 0, 0, 0);')
		# print('\tglUniform4f(u_yz_id, 0, 0, 0, 0);')
		# print('\tglUniform4f(u_zx_id, 0, 0, 0, 0);')
		# print('\tglDrawArrays(GL_LINES, 0, 4 * 6);')
		# print('\t}')
		
		print('\ttest_counter++;')
		print(r)
		# print('\tif(player_room!=&room%d) return;' % index)
		# print('\tglUniform4f(u_xy_id, v.xy[0], v.xy[1], v.xy[2], v.xy[3]);')
		# print('\tglUniform4f(u_yz_id, v.yz[0], v.yz[1], v.yz[2], v.yz[3]);')
		# print('\tglUniform4f(u_zx_id, v.zx[0], v.zx[1], v.zx[2], v.zx[3]);')
		# print('\tglUniform4f(u_pos_id, v.px-player_x, v.py-player_y, v.pz-player_z, -10);')
		# print('\tglUniform3f(u_scale_id, -.1, -.1, -.1);')
		# print('\tglDrawArrays(GL_QUADS, 0, 4 * 6);')
		print('}')
		print('fn View room%d_update(View v, Room **r'
		', float w, float d, float dt) {' % index)
		print('float x = v.vx * dt, y = v.vy * dt, z = v.vz * dt;')
		print('\tif(-room%d.w < v.px && v.px < room%d.w' % (index, index))
		print('\t&& -room%d.h < v.py && v.py < room%d.h' % (index, index))
		print('\t&& -room%d.d < v.pz && v.pz < room%d.d' % (index, index))
		print('\t);')
		# print('\t) {')
		print(u)
		# print('\t}')
		print('\tv.px += x;')
		print('\tv.py += y;')
		print('\tv.pz += z;')
		print('\tif(v.px > room%d.w-w) v.px=room%d.w-w, v.vx*=0;' % (index, index))
		print('\tif(v.py > room%d.h-w) v.py=room%d.h-w, v.vy*=-1;' % (index, index))
		print('\tif(v.pz > room%d.d-w) v.pz=room%d.d-w, v.vz*=0;' % (index, index))
		print('\tif(v.px < w-room%d.w) v.px=w-room%d.w, v.vx*=0;' % (index, index))
		print('\tif(v.py < w-room%d.h) v.py=w-room%d.h, v.vy*=0;' % (index, index))
		print('\tif(v.pz < w-room%d.d) v.pz=w-room%d.d, v.vz*=0;' % (index, index))
		print('\treturn v;')
		print('}')
		print('fn float room%d_cast_down(View v, float d) {' % index)
		print('\tif(d < v.py + room%d.h) return d;' % index)
		print(c)
		print('\treturn v.py + room%d.h;' % index)
		print('}')
		index += 1

scale = 1

a = room(4,4,4)
b0 = room(40,40,40)
b1 = room(400,40,40)
c = room(5,5,5)
d = room(50,4,50)
e = room(3,3,400)
f = room(9,3,3)
g = room(3,3,3)
h = room(3,3,3)
i = room(9,3,9)

dwn(a,3,3, b0,0,0, 1, 1)
fwd(b0,37,-37, c,2,-2, 3,3)
fwd(b0,31,-37, a,0,0, 3,3)
fwd(c,-4,-2, c,-4,-2, 1,4)
fwd(c,-2,-3, c,-2,3, 1,2)
rgt(c,0,-4, a,0,-3, 4,1)
lft(c,0,-1, d,0,0, 2,4)
dwn(d,0,0, a,0,0, 4,4)
lft(b0,37,37, b0,37,-37, 3,3)
dwn(b0,-37,37, b0,-37,37, 3,3)
fwd(b0,25,-37, b1,-396,-37, 3,3)
lft(b1,5,-37, e,397,0, 3,3)
lft(b1,-5,-37, e,-397,0, 3,3)
fwd(b1,-397,-37, f,-6,0, 3,3)
fwd(b1,397, -37, f,6,0, 3,3)
bwd(f,0,0, d,0,0, 3,3)
rgt(b0,0,-37, g,0,0, 3,3)
dwn(g,0,0, g,0,0, 3,3)
bwd(g,0,0, h,0,0, 3,3)
rgt(h,0,0, i,0,0, 3,3)
dwn(i,-6,0, h,0,0, 3,3)
fwd(g,0,0, h,0,0, 3,3)
lft(h,0,0, i,0,0, 3,3)

out()
import sys
sys.stdout = open('3_roomgen_output.h', 'w')
out()

