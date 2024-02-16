from src.utils import govmnt_taxes, get_amortization
import constants

if __name__ == "__main__":
    print("Calculadora de vivienda\n")
    # price = input("Introduce el precio de la vivienda: ")
    # handed = input("Si es primera mano escribe (1) y si es de segunda (2): ")
    # reduced = input("Tiene precio reducido? (<35 anos) y/n")
    
    price: int = constants.PRINCIPAL
    hand: int = 2
    reduced: bool = True
    years: int = constants.TERM
    year_interest: float = constants.APR
    
    taxes_1_hand = govmnt_taxes(hand=1, reduced=True)
    taxes_2_hand = govmnt_taxes(hand=2, reduced=True)
    taxed_price_1 = int(price * taxes_1_hand)
    taxed_price_2 = int(price * taxes_2_hand)
    
    # Deposit
    deposit = int(constants.DEPOSIT * price)
    
    # Expenses
    valuation = constants.VALUATION
    notary = int(constants.NOTARY * price)
    registry = int(constants.REGISTRY * price)
    administrator = constants.ADMINISTRATOR
    total_expenses = valuation + notary + registry + administrator
    total_cost = price + total_expenses + taxed_price_2
    mortgage_cost = total_cost - deposit
    
    # Mortgage monthly payment
    monthly_payment = get_amortization(mortgage_cost, years, year_interest)
    
    print(f'Precio de la vivienda (PVP): {price} €')
    print('-----------------------------------------------------\n')
    print(f'Entregando un deposito del {int(constants.DEPOSIT * 100)} %: {deposit} €')
    print('\n')
    print('---------- Gastos Admnistrativos: ----------')
    print(f'Tasacion (200-600 €): {valuation} €')
    print(f'Notaria (0.5 - 1 %): {notary} €')
    print(f'Registro de la propiedad (0.1 - 0.25 %): {int(constants.REGISTRY * price)} €')
    print(f'Gestoria: {administrator} €')
    print(f'*****Total en gastos administrativos: {total_expenses} €****')
    print('\n')
    print(f'Coste total del inmueble: {total_cost}')
    print('----------------- Impuestos -----------------')
    print(f'Si es 1 mano pagamos: {taxed_price_1} €')
    print(f'Si es 2 mano pagamos: {taxed_price_2} €')
    print('\n')
    print('-----------------------------------------------------\n')
    print('Tenemos que hacer una aportacion inicial de (deposito + gastos + impuestos):')
    print(f'Si es 1 mano: {deposit} + {total_expenses} + {taxed_price_1} = {deposit+total_expenses+taxed_price_1} €')
    print(f'Si es 2 mano: {deposit} + {total_expenses} + {taxed_price_2} = {deposit+total_expenses+taxed_price_2} €')
    print('-----------------------------------------------------\n')
    print(f'Para una hipoteca a {constants.TERM} años con un interes del {int(constants.APR * 100)} % vamos a pagar: ')
    print(f'{monthly_payment:,.2f} €')
    