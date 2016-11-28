from datetime import datetime
import random
import time
import MySQLdb

fourteens = '''From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest thy content,
And, tender churl, mak'st waste in niggarding:
Pity the world, or else this glutton be,
To eat the world's due, by the grave and thee.
When forty winters shall besiege thy brow,
And dig deep trenches in thy beauty's field,
Thy youth's proud livery so gazed on now,
Will be a totter'd weed of small worth held:
Then being asked, where all thy beauty lies,
Where all the treasure of thy lusty days;
To say, within thine own deep sunken eyes,
Were an all-eating shame, and thriftless praise.
How much more praise deserv'd thy beauty's use,
If thou couldst answer 'This fair child of mine
Shall sum my count, and make my old excuse,'
Proving his beauty by succession thine!
This were to be new made when thou art old,
And see thy blood warm when thou feel'st it cold.
Look in thy glass and tell the face thou viewest
Now is the time that face should form another;
Whose fresh repair if now thou not renewest,
Thou dost beguile the world, unbless some mother.
For where is she so fair whose unear'd womb
Disdains the tillage of thy husbandry?
Or who is he so fond will be the tomb
Of his self-love, to stop posterity?
Thou art thy mother's glass and she in thee
Calls back the lovely April of her prime;
So thou through windows of thine age shalt see,
Despite of wrinkles this thy golden time.
But if thou live, remember'd not to be,
Die single and thine image dies with thee.
Unthrifty loveliness, why dost thou spend
Upon thy self thy beauty's legacy?
Nature's bequest gives nothing, but doth lend,
And being frank she lends to those are free:
Then, beauteous niggard, why dost thou abuse
The bounteous largess given thee to give?
Profitless usurer, why dost thou use
So great a sum of sums, yet canst not live?
For having traffic with thy self alone,
Thou of thy self thy sweet self dost deceive:
Then how when nature calls thee to be gone,
What acceptable audit canst thou leave?
Thy unused beauty must be tombed with thee,
Which, used, lives th' executor to be.
Those hours, that with gentle work did frame
The lovely gaze where every eye doth dwell,
Will play the tyrants to the very same
And that unfair which fairly doth excel;
For never-resting time leads summer on
To hideous winter, and confounds him there;
Sap checked with frost, and lusty leaves quite gone,
Beauty o'er-snowed and bareness every where:
Then were not summer's distillation left,
A liquid prisoner pent in walls of glass,
Beauty's effect with beauty were bereft,
Nor it, nor no remembrance what it was:
But flowers distill'd, though they with winter meet,
Leese but their show; their substance still lives sweet.'''.split('\n')

article_length = len(fourteens)

def show_fourteens():
	print(article_length)
	for i, line in enumerate(fourteens, 1):
		print(i, line)

def sample(k=3):
	lines = random.sample(fourteens, k)
	data = '%s' %(lines)
	return data

def formated_time():
	now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return now

def execute(sql, param):
	db = MySQLdb.connect(host="localhost",user="root",passwd="",db="test")
	cursor = db.cursor()
	try:
		cursor.execute(sql, param)
		db.commit()
	except Exception, e:
		print(e)
		db.rollback()
	cursor.close()
	db.close()

class DBUtil:
	"""docstring for DBUtil"""
	INSERT_SQL = 'INSERT INTO t_article(content, creation_time) VALUES(%s, %s)'
	db = MySQLdb.connect(host="localhost",user="root",passwd="",db="test")
	cursor = db.cursor()

	# def __init__(self, arg):
	# 	self.arg = arg

	@staticmethod
	def insert(sql, param):
		try:
			cursor.execute(sql, param)
			db.commit()
		except Exception, e:
			print(e)
			db.rollback()

	@staticmethod
	def init_db():
		cursor.execute("drop table if exists t_article")
		sql = '''CREATE TABLE t_article(
					id int(10) NOT NULL AUTO_INCREMENT,
					content text NOT NULL,
					creation_time datetime,
					PRIMARY KEY (id)
				) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;'''
		cursor.execute(sql)

	@staticmethod
	def close():
		cursor.close()
		db.close()


def run1(num_epochs=10, batch_size=1000):
	DBUtil.init_db()
	for i in range(num_epochs):
		start_time = time.time()
		for j in range(batch_size):
			execute(DBUtil.INSERT_SQL, [sample(), formated_time()])
		duration = time.time() - start_time
		print('step %d: %.1f sqls/sec; %.3f sec/batch' %(i, batch_size / duration, duration))

def run2(num_epochs=10, batch_size=1000):
	DBUtil.init_db()
	for i in range(num_epochs):
		start_time = time.time()
		for j in range(batch_size):
			DBUtil.insert(DBUtil.INSERT_SQL, [sample(), formated_time()])
		duration = time.time() - start_time
		print('step %d: %.1f sqls/sec; %.3f sec/batch' %(i, batch_size / duration, duration))


def run_benchmark():
	print('benchmark1:')
	run1()
	print('benchmark2:')
	run2()


if __name__ == '__main__':
	run_benchmark()