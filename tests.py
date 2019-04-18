import unittest
from anguro_parslog import ParserLog




class TestLog(unittest.TestCase):


	def test_send_from_1(self):
		log = '''Jul 10 10:09:53 srv24-s-st postfix/qmgr[3043]: 5FEB2DF0506: from=<it@yc4.ru>, size=788, nrcpt=1 (queue active)'''
		pars = ParserLog(log)
		self.assertEqual(pars.send_from(), {'it@yc4.ru' : 1})

	def test_send_from_2(self):
		log = ''
		pars = ParserLog(log)
		self.assertEqual(pars.send_from(), {})

	def test_send_from_3(self):
		log = '''postfix/qmgr[3043]: 5FEB2DF0506: from=<it@yc4.ru>, '''
		pars = ParserLog(log)
		self.assertEqual(pars.send_from(), {})

	def test_send_from_4(self):
		log = '''ul 10 10:09:53 srv24-s-st postfix/qmgr[3043]: 5FEB2DF0506: from=<it@yc4.ru>, size=788, nrcpt=1 (queue active)
		Jul 10 10:09:53 srv24-s-st postfix/qmgr[3043]: 5FEB2DF0506: from=<it@yc.ru>, size=788, nrcpt=1 (queue active)
		Jul 10 10:09:52 srv24-s-st postfix/qmgr[3044]: 5FEB2DF0506: from=<it@yc.ru>, size=788, nrcpt=1 (queue active)
		Jul 10 10:09:22 srv24-s-st postfix/smtp[22635]: D69F5DF04F4: to=<krasteplokomplekt@yandex.ru>,'''
		pars = ParserLog(log)
		self.assertEqual(pars.send_from(), {'it@yc4.ru' : 1,
											'it@yc.ru'  : 2,
											})

class TestLogSetUp(unittest.TestCase):

	def reader(self):
		with open('test_log', 'r') as f:
			log = f.read()
		return log

	def setUp(self):
		log = self.reader()
		self.pars = ParserLog(log)


	def test_count_send_to_1(self):
		self.assertEqual(self.pars.count_send_to(), 3)

	def test_count_send_to_2(self):
		self.assertNotEqual(self.pars.count_send_to(), 2)

	def test_count_send_to_3(self):
		self.assertNotEqual(self.pars.count_send_to(), True)

	def test_count_success_send_1(self):
		self.assertNotEqual(self.pars.count_success_send(), 99 )

	def test_count_success_send_2(self):
		self.assertEqual(self.pars.count_success_send(), 2 )

	def test_count_falled_send_1(self):
		self.assertEqual(self.pars.count_falled_send(), 1 )

	def test_count_falled_send_2(self):
		self.assertNotEqual(self.pars.count_falled_send(), 15 )

	def test_contr_sum(self):
		summ = self.pars.count_success_send() + self.pars.count_falled_send()
		self.assertEqual(self.pars.count_send_to(), summ)





if __name__ == '__main__':
	unittest.main()