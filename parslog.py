import re
from collections import Counter


FILENAME = r'maillog'

class ParserLog():

	re_from_send_email = r'''\bfrom=(.+),.+size=.+nrcpt='''
	re_success_send = r''': (.+): to=.+,.+relay=.+dsn=.+status=sent'''
	re_falled = r''': (.+):.+to=.+,.+relay=.+dsn=.+status=(?!sent)'''
	re_removed = r''': (.+): removed'''

	def __init__(self, log):
		self.log = log

	def send_from(self):
		'''Количество писем с почтового ящика'''
		mail_list = re.findall(self.re_from_send_email, self.log)
		count = Counter(mail_list)
		return dict(count)

	def count_success_send(self):
		'''Кол-во удачных отправлений'''
		mail_list = re.findall(self.re_success_send, self.log)
		return len(mail_list)

	def count_falled_send(self):
		'''Кол-во проваленных'''
		list_falled = re.findall(self.re_falled, self.log)
		removed_list = re.findall(self.re_removed, self.log)
		removed_falled =[]
		for id_notsent in list_falled:
			try:
				index = removed_list.index(id_notsent)
			except ValueError:
				continue
			removed_falled.append(removed_list.pop(index))
		return len(removed_falled)


def reader(file):

	with open(file, 'r') as f:
		log = f.read()
	return log


def main():
	log = reader(FILENAME)
	resend = ParserLog(log)
	print('from', resend.send_from() )
	print('success  :', resend.count_success_send() )
	print('falled   :', resend.count_falled_send())



if __name__ == '__main__':
	main()