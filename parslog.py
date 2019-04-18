import re
from collections import Counter


FILENAME = r'maillog'

class ParserLog():

	re_from_send_email = r'''\bfrom=<(.+)>.+size=.+nrcpt='''
	re_to_send_email = r'''\bto=<(.+)>.+relay=.+dsn=.+status='''
	re_success_send = r'''\bto=<(.+)>.+relay=.+dsn=.+status=sent'''
	re_falled_send= r'''\bto=<(.+)>.+relay=.+dsn=.+status=(?!sent)'''

	def __init__(self, log):
		self.log = log

	def send_from(self):
		'''С какого ящика и сколько писем было отправлено'''
		mail_list = re.findall(self.re_from_send_email, self.log)
		count = Counter(mail_list)
		return dict(count)

	def count_send_to(self):
		'''Общее кол-во отправлений'''
		mail_list =re.findall(self.re_to_send_email, self.log)
		return len(mail_list)

	def count_success_send(self):
		'''Кол-во удачных отправлений'''
		mail_list = re.findall(self.re_success_send, self.log)
		# count = Counter(mail_list) # кто и сколько
		return len(mail_list) #, dict(count)

	def count_falled_send(self):
		'''Кол-во проваленных'''
		mail_list = re.findall(self.re_falled_send, self.log)
		# count = Counter(mail_list) # кто и сколько
		return len(mail_list) #, dict(count)

def reader(file):

	with open(file, 'r') as f:
		log = f.read()
	return log


def main():
	log = reader(FILENAME)
	resend = ParserLog(log)
	print( resend.send_from() )
	print('all sent :', resend.count_send_to() )
	print('success  :', resend.count_success_send() )
	print('falled   :', resend.count_falled_send())


if __name__ == '__main__':
	main()