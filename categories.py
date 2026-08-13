
salary_senders = ['randstad']
payback = ['gabriel marques berto','guilherme zanini da silva', 'vinicius zanini da silva','amanda valéria da silva gomes','gabriel araujo de souza','ayman guilherme sehn muhamad ali','luan de oliveira müller','julia low eizerik',]
tax_reimbursement = ['receita federal']
investment_withdraw = ['resgate']
investment_deposit = ['aplicação']


convenience_words = ['posto', 'combustivel', 'shell', 'ipiranga', 'petrobras','conveniencia','sapore','comb','posto de gasolina','pamela']

expense_categories = {
    'Transport': ['uber','posto', 'combustivel', 'shell', 'ipiranga', 'petrobras','conveniencia','sapore','comb','posto de gasolina','park','transportes'],
    'Supermarket': ['supermercado', 'rissul','bourbon','silui mercado das frut'],
    'Eat out' : ['gastronomia','sushi','restaurante','pizza','ifood','cozinha','xis','pizzaria','nonnaludovina','lanches','funnyfeelings','piatto di nono ristora','cavanhas','padaria','bistro','churrascaria','sorvetes'],
    'Pharmacy':['panvel','raia'],
    'Credit Card':['fatura'],
    'Alcohol' : ['sanlou','beer','cerveja','bar','majestic','hunsruck'],
    }

income_categories = [
    "Salary",
    "Pay back",
    "Tax reimbursement",
    "Post Graduation reimbursement",
    "Other income"
]

non_expense_categories = income_categories + ["Investment","Investment withdraw"]