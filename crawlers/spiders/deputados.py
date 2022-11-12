import scrapy
from scrapy.selector import Selector

class DeputadosSpider(scrapy.Spider):
	name = 'deputados'
	allowed_domains = ['www.camara.leg.br']
	start_urls = [
		'https://www.camara.leg.br/deputados/204554',
		'https://www.camara.leg.br/deputados/204521',
		'https://www.camara.leg.br/deputados/204379',
		'https://www.camara.leg.br/deputados/204560',
		'https://www.camara.leg.br/deputados/121948',
		'https://www.camara.leg.br/deputados/74646',
		'https://www.camara.leg.br/deputados/141372',
		'https://www.camara.leg.br/deputados/160508',
		'https://www.camara.leg.br/deputados/136811',
		'https://www.camara.leg.br/deputados/178835',
		'https://www.camara.leg.br/deputados/160527',
		'https://www.camara.leg.br/deputados/204495',
		'https://www.camara.leg.br/deputados/204549',
		'https://www.camara.leg.br/deputados/178836',
		'https://www.camara.leg.br/deputados/160559',
		'https://www.camara.leg.br/deputados/204413',
		'https://www.camara.leg.br/deputados/204501',
		'https://www.camara.leg.br/deputados/160511',
		'https://www.camara.leg.br/deputados/178972',
		'https://www.camara.leg.br/deputados/204571',
		'https://www.camara.leg.br/deputados/105534',
		'https://www.camara.leg.br/deputados/204544',
		'https://www.camara.leg.br/deputados/160545',
		'https://www.camara.leg.br/deputados/204503',
		'https://www.camara.leg.br/deputados/178833',
		'https://www.camara.leg.br/deputados/141431',
		'https://www.camara.leg.br/deputados/92699',
		'https://www.camara.leg.br/deputados/204427',
		'https://www.camara.leg.br/deputados/204411',
		'https://www.camara.leg.br/deputados/141434',
		'https://www.camara.leg.br/deputados/191923',
		'https://www.camara.leg.br/deputados/204392',
		'https://www.camara.leg.br/deputados/204510',
		'https://www.camara.leg.br/deputados/204494',
		'https://www.camara.leg.br/deputados/204393',
		'https://www.camara.leg.br/deputados/74200',
		'https://www.camara.leg.br/deputados/115746',
		'https://www.camara.leg.br/deputados/160669',
		'https://www.camara.leg.br/deputados/204473',
		'https://www.camara.leg.br/deputados/204484',
		'https://www.camara.leg.br/deputados/204527',
		'https://www.camara.leg.br/deputados/74374',
		'https://www.camara.leg.br/deputados/204394',
		'https://www.camara.leg.br/deputados/74383',
		'https://www.camara.leg.br/deputados/204575',
		'https://www.camara.leg.br/deputados/204491',
		'https://www.camara.leg.br/deputados/74270',
		'https://www.camara.leg.br/deputados/204365',
		'https://www.camara.leg.br/deputados/160673',
		'https://www.camara.leg.br/deputados/178996',
		'https://www.camara.leg.br/deputados/198783',
		'https://www.camara.leg.br/deputados/161550',
		'https://www.camara.leg.br/deputados/207309',
		'https://www.camara.leg.br/deputados/132504',
		'https://www.camara.leg.br/deputados/204537',
		'https://www.camara.leg.br/deputados/160640',
		'https://www.camara.leg.br/deputados/204482',
		'https://www.camara.leg.br/deputados/178871',
		'https://www.camara.leg.br/deputados/178930',
		'https://www.camara.leg.br/deputados/178953',
		'https://www.camara.leg.br/deputados/211866',
		'https://www.camara.leg.br/deputados/141428',
		'https://www.camara.leg.br/deputados/68720',
		'https://www.camara.leg.br/deputados/178969',
		'https://www.camara.leg.br/deputados/141427',
		'https://www.camara.leg.br/deputados/171623',
		'https://www.camara.leg.br/deputados/204368',
		'https://www.camara.leg.br/deputados/160587',
		'https://www.camara.leg.br/deputados/66828',
		'https://www.camara.leg.br/deputados/204477',
		'https://www.camara.leg.br/deputados/72442',
		'https://www.camara.leg.br/deputados/204398',
		'https://www.camara.leg.br/deputados/204371',
		'https://www.camara.leg.br/deputados/160666',
		'https://www.camara.leg.br/deputados/212504',
		'https://www.camara.leg.br/deputados/109429',
		'https://www.camara.leg.br/deputados/141335',
		'https://www.camara.leg.br/deputados/204358',
		'https://www.camara.leg.br/deputados/178948',
		'https://www.camara.leg.br/deputados/204388',
		'https://www.camara.leg.br/deputados/141513',
		'https://www.camara.leg.br/deputados/204561',
		'https://www.camara.leg.br/deputados/204397',
		'https://www.camara.leg.br/deputados/160538',
		'https://www.camara.leg.br/deputados/74052',
		'https://www.camara.leg.br/deputados/204551',
		'https://www.camara.leg.br/deputados/204502',
		'https://www.camara.leg.br/deputados/93083',
		'https://www.camara.leg.br/deputados/204352',
		'https://www.camara.leg.br/deputados/204572',
		'https://www.camara.leg.br/deputados/178829',
		'https://www.camara.leg.br/deputados/204531',
		'https://www.camara.leg.br/deputados/178924',
		'https://www.camara.leg.br/deputados/204487',
		'https://www.camara.leg.br/deputados/141401',
		'https://www.camara.leg.br/deputados/204361',
		'https://www.camara.leg.br/deputados/178962',
		'https://www.camara.leg.br/deputados/178993',
		'https://www.camara.leg.br/deputados/204460',
		'https://www.camara.leg.br/deputados/74262',
		'https://www.camara.leg.br/deputados/204516',
		'https://www.camara.leg.br/deputados/178927',
		'https://www.camara.leg.br/deputados/178937',
		'https://www.camara.leg.br/deputados/178881',
		'https://www.camara.leg.br/deputados/204356',
		'https://www.camara.leg.br/deputados/178831',
		'https://www.camara.leg.br/deputados/74471',
		'https://www.camara.leg.br/deputados/204423',
		'https://www.camara.leg.br/deputados/133439',
		'https://www.camara.leg.br/deputados/178882',
		'https://www.camara.leg.br/deputados/204515',
		'https://www.camara.leg.br/deputados/74212',
		'https://www.camara.leg.br/deputados/160553',
		'https://www.camara.leg.br/deputados/73433',
		'https://www.camara.leg.br/deputados/141391',
		'https://www.camara.leg.br/deputados/204414',
		'https://www.camara.leg.br/deputados/160541',
		'https://www.camara.leg.br/deputados/160600',
		'https://www.camara.leg.br/deputados/159237',
		'https://www.camara.leg.br/deputados/74090',
		'https://www.camara.leg.br/deputados/74459',
		'https://www.camara.leg.br/deputados/160665',
		'https://www.camara.leg.br/deputados/160512',
		'https://www.camara.leg.br/deputados/69871',
		'https://www.camara.leg.br/deputados/178975',
		'https://www.camara.leg.br/deputados/74060',
		'https://www.camara.leg.br/deputados/178916',
		'https://www.camara.leg.br/deputados/204367',
		'https://www.camara.leg.br/deputados/204454',
		'https://www.camara.leg.br/deputados/204409',
		'https://www.camara.leg.br/deputados/160528',
		'https://www.camara.leg.br/deputados/62881',
		'https://www.camara.leg.br/deputados/160552',
		'https://www.camara.leg.br/deputados/116379',
		'https://www.camara.leg.br/deputados/73891',
		'https://www.camara.leg.br/deputados/205548',
		'https://www.camara.leg.br/deputados/204511',
		'https://www.camara.leg.br/deputados/204451',
		'https://www.camara.leg.br/deputados/178908',
		'https://www.camara.leg.br/deputados/204512',
		'https://www.camara.leg.br/deputados/204569',
		'https://www.camara.leg.br/deputados/164359',
		'https://www.camara.leg.br/deputados/204542',
		'https://www.camara.leg.br/deputados/213856',
		'https://www.camara.leg.br/deputados/160588',
		'https://www.camara.leg.br/deputados/178929',
		'https://www.camara.leg.br/deputados/160599',
		'https://www.camara.leg.br/deputados/143632',
		'https://www.camara.leg.br/deputados/160758',
		'https://www.camara.leg.br/deputados/204450',
		'https://www.camara.leg.br/deputados/204426',
		'https://www.camara.leg.br/deputados/141398',
		'https://www.camara.leg.br/deputados/204499',
		'https://www.camara.leg.br/deputados/204370',
		'https://www.camara.leg.br/deputados/178876',
		'https://www.camara.leg.br/deputados/204488',
		'https://www.camara.leg.br/deputados/141405',
		'https://www.camara.leg.br/deputados/73441',
		'https://www.camara.leg.br/deputados/204496',
		'https://www.camara.leg.br/deputados/204504',
		'https://www.camara.leg.br/deputados/205476',
		'https://www.camara.leg.br/deputados/204490',
		'https://www.camara.leg.br/deputados/141439',
		'https://www.camara.leg.br/deputados/204476',
		'https://www.camara.leg.br/deputados/204440',
		'https://www.camara.leg.br/deputados/74537',
		'https://www.camara.leg.br/deputados/141408',
		'https://www.camara.leg.br/deputados/204376',
		'https://www.camara.leg.br/deputados/204378',
		'https://www.camara.leg.br/deputados/204514',
		'https://www.camara.leg.br/deputados/178963',
		'https://www.camara.leg.br/deputados/135054',
		'https://www.camara.leg.br/deputados/204355',
		'https://www.camara.leg.br/deputados/141411',
		'https://www.camara.leg.br/deputados/74467',
		'https://www.camara.leg.br/deputados/213854',
		'https://www.camara.leg.br/deputados/204518',
		'https://www.camara.leg.br/deputados/212625',
		'https://www.camara.leg.br/deputados/204481',
		'https://www.camara.leg.br/deputados/213679',
		'https://www.camara.leg.br/deputados/204439',
		'https://www.camara.leg.br/deputados/204351',
		'https://www.camara.leg.br/deputados/178830',
		'https://www.camara.leg.br/deputados/204412',
		'https://www.camara.leg.br/deputados/204562',
		'https://www.camara.leg.br/deputados/141417',
		'https://www.camara.leg.br/deputados/134812',
		'https://www.camara.leg.br/deputados/74655',
		'https://www.camara.leg.br/deputados/204541',
		'https://www.camara.leg.br/deputados/92346',
		'https://www.camara.leg.br/deputados/204552',
		'https://www.camara.leg.br/deputados/204500',
		'https://www.camara.leg.br/deputados/178977',
		'https://www.camara.leg.br/deputados/141421',
		'https://www.camara.leg.br/deputados/141422',
		'https://www.camara.leg.br/deputados/154919',
		'https://www.camara.leg.br/deputados/204364',
		'https://www.camara.leg.br/deputados/160532',
		'https://www.camara.leg.br/deputados/204389',
		'https://www.camara.leg.br/deputados/178854',
	]

	def parse(self, response):
		deputado = {'genero': 'M'}
		deputado = self.parse_deputy(response, deputado)

		print(deputado)

	def parse_deputy(self, response, deputy):
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