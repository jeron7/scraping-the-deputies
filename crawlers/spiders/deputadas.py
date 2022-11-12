import scrapy
from scrapy.selector import Selector

class DeputadasSpider(scrapy.Spider):
	name = 'deputadas'
	allowed_domains = ['www.camara.leg.br']
	start_urls = [
		'https://www.camara.leg.br/deputados/178989',
		'https://www.camara.leg.br/deputados/204525',
		'https://www.camara.leg.br/deputados/178945',
		'https://www.camara.leg.br/deputados/204357',
		'https://www.camara.leg.br/deputados/204535',
		'https://www.camara.leg.br/deputados/178961',
		'https://www.camara.leg.br/deputados/204360',
		'https://www.camara.leg.br/deputados/178946',
		'https://www.camara.leg.br/deputados/204534',
		'https://www.camara.leg.br/deputados/204464',
		'https://www.camara.leg.br/deputados/178901',
		'https://www.camara.leg.br/deputados/204466',
		'https://www.camara.leg.br/deputados/178862',
		'https://www.camara.leg.br/deputados/215044',
		'https://www.camara.leg.br/deputados/74075',
		'https://www.camara.leg.br/deputados/220008',
		'https://www.camara.leg.br/deputados/218086',
		'https://www.camara.leg.br/deputados/160575',
		'https://www.camara.leg.br/deputados/204407',
		'https://www.camara.leg.br/deputados/204354',
		'https://www.camara.leg.br/deputados/160598',
		'https://www.camara.leg.br/deputados/204447',
		'https://www.camara.leg.br/deputados/178966',
		'https://www.camara.leg.br/deputados/107283',
		'https://www.camara.leg.br/deputados/129618',
		'https://www.camara.leg.br/deputados/198197',
		'https://www.camara.leg.br/deputados/67138',
		'https://www.camara.leg.br/deputados/74848',
		'https://www.camara.leg.br/deputados/108338',
		'https://www.camara.leg.br/deputados/178839',
		'https://www.camara.leg.br/deputados/204468',
		'https://www.camara.leg.br/deputados/204546',
		'https://www.camara.leg.br/deputados/74856',
		'https://www.camara.leg.br/deputados/160534',
		'https://www.camara.leg.br/deputados/178832',
		'https://www.camara.leg.br/deputados/204375',
		'https://www.camara.leg.br/deputados/139285',
		'https://www.camara.leg.br/deputados/204405',
		'https://www.camara.leg.br/deputados/204410',
		'https://www.camara.leg.br/deputados/74784',
		'https://www.camara.leg.br/deputados/178866',
		'https://www.camara.leg.br/deputados/166402',
		'https://www.camara.leg.br/deputados/204458',
		'https://www.camara.leg.br/deputados/204471',
		'https://www.camara.leg.br/deputados/204430',
		'https://www.camara.leg.br/deputados/171619',
		'https://www.camara.leg.br/deputados/74398',
		'https://www.camara.leg.br/deputados/204540',
		'https://www.camara.leg.br/deputados/178956',
		'https://www.camara.leg.br/deputados/204428',
		'https://www.camara.leg.br/deputados/204432',
		'https://www.camara.leg.br/deputados/204453',
		'https://www.camara.leg.br/deputados/66179',
		'https://www.camara.leg.br/deputados/216198',
		'https://www.camara.leg.br/deputados/205535',
		'https://www.camara.leg.br/deputados/204377',
		'https://www.camara.leg.br/deputados/73943',
		'https://www.camara.leg.br/deputados/204529',
		'https://www.camara.leg.br/deputados/204565',
		'https://www.camara.leg.br/deputados/160639',
		'https://www.camara.leg.br/deputados/160641',
		'https://www.camara.leg.br/deputados/204467',
		'https://www.camara.leg.br/deputados/215361',
		'https://www.camara.leg.br/deputados/178925',
		'https://www.camara.leg.br/deputados/204528',
		'https://www.camara.leg.br/deputados/204545',
		'https://www.camara.leg.br/deputados/74057',
		'https://www.camara.leg.br/deputados/204353',
		'https://www.camara.leg.br/deputados/204400',
		'https://www.camara.leg.br/deputados/73696',
		'https://www.camara.leg.br/deputados/123756',
		'https://www.camara.leg.br/deputados/204509',
		'https://www.camara.leg.br/deputados/73701',
		'https://www.camara.leg.br/deputados/207176',
		'https://www.camara.leg.br/deputados/204374',
		'https://www.camara.leg.br/deputados/160589',
		'https://www.camara.leg.br/deputados/213762',
		'https://www.camara.leg.br/deputados/204507',
		'https://www.camara.leg.br/deputados/164360',
		'https://www.camara.leg.br/deputados/204369',
		'https://www.camara.leg.br/deputados/204380',
		'https://www.camara.leg.br/deputados/204462',
		'https://www.camara.leg.br/deputados/178928',
		'https://www.camara.leg.br/deputados/178939',
		'https://www.camara.leg.br/deputados/204459',
		'https://www.camara.leg.br/deputados/81297',
		'https://www.camara.leg.br/deputados/204434',
		'https://www.camara.leg.br/deputados/178994',
		'https://www.camara.leg.br/deputados/204421'
	]

	def parse(self, response):
		deputada = parse_deputy(response)
		deputada = {'genero': 'F'}

		print(deputada)

	# TODO: Refactor this method and remove code duplication 
	def parse_deputy(self, response):
		deputy = {}
		informacoes_dep = response.xpath('//ul[@class="informacoes-deputado"]').get()
		
		def info_pessoal(info):
			return Selector(text=informacoes_dep).xpath(f'//li[span[contains(text(), "{info}")]]/text()').get()[1:]

		deputy['nome'] = info_pessoal("Nome Civil:")
		deputy['data_nascimento'] = info_pessoal("Data de Nascimento:")

		def get_atuacao(contexto):
			return response.xpath(f'//a[@class="list-table__heading" and text()="{contexto}"]/following-sibling::dl').get()

		atuacao_plenario = get_atuacao("em Plenário")
		atuacao_comissao = get_atuacao("em comissões")

		def atuacao_by_column(contexto, column_text):
			value = Selector(text=contexto).xpath(f'//dt[contains(text(), "{column_text}")]/following-sibling::dd/text()').get()
			return value.replace("\n", "").strip()
		
		deputy['presença_plenario'] = atuacao_by_column(atuacao_plenario, "Presenças")
		deputy['ausencia_justificada_plenario'] = atuacao_by_column(atuacao_plenario, "Ausências justificadas")
		deputy['ausencia_plenario'] = atuacao_by_column(atuacao_plenario, "Ausências não justificadas")
		deputy['presença_comissao'] = atuacao_by_column(atuacao_comissao, "Presenças")
		deputy['ausencia_justificada_comissao'] = atuacao_by_column(atuacao_comissao, "Ausências justificadas")
		deputy['ausencia_comissao'] = atuacao_by_column(atuacao_comissao, "Ausências não justificadas")
		
		def recurso_gasto(recurso):
			return response.xpath(f'//h3[text()="{recurso}"]/following-sibling::div').get()

		verba_par = recurso_gasto("Cota parlamentar ")
		verba_gab = recurso_gasto("Verba de gabinete ")

		def salario_to_float(salario):
			if (salario is None):
				return 'NaN'
			return float(salario.replace("R$", "").replace(".", "").replace(",", "."))

		def percetual_gasto(verba, gasto):
			percentuais = Selector(text=verba).xpath('//div/p[contains(text(), "Percentual gasto")]/following-sibling::table/tbody').get()
			return salario_to_float(Selector(text=percentuais).xpath(f'//td[text()="{gasto}"]/following-sibling::td/text()').get())
		
		deputy['gasto_total_par'] = percetual_gasto(verba_par, "Total Gasto")

		meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']

		def gastos_mensais(verba, mes):
			gastos_mensais = Selector(text=verba_par).xpath('//div/p[contains(text(), "Gasto mensal")]/following-sibling::table/tbody').get()
			return salario_to_float(Selector(text=gastos_mensais).xpath(f'//td[text()="{mes}"]/following-sibling::td/text()').get())

		for mes in meses:
			key = f'gasto_{mes.lower()}_par'
			deputy[key] = gastos_mensais(verba_par, mes)
		
		deputy['salario_bruto_par'] = deputy['gasto_total_par'] + percetual_gasto(verba_par, "Total Disponível")
		
		deputy['gasto_total_gab'] = percetual_gasto(verba_gab, "Total Gasto")

		for mes in meses:
			key = f'gasto_{mes.lower()}_gab'
			deputy[key] = gastos_mensais(verba_gab, mes)

		deputy['salario_bruto'] = salario_to_float(response.xpath(f'//h3[text()="Salário mensal bruto "]/following-sibling::a[@class="beneficio__info"]/text()').get())

		return deputy