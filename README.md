# Calculadora de hipotecas

El caso que se trata en esta calculadora es el *préstamo con cuota de amortización constante*.

Un préstamo con cuota de amortización constante es un préstamo en el que se conviene
en devolver el capital prestado $C_0$ con un tipo de interés determinado $i$ a través de $N$
cuotas periódicas, que supondremos mensuales, con el mismo importe $c$. Como las cuotas
van a ser mensuales, supondremos por comodidad que $i$ es el tipo de interés efectivo
mensual aplicable.

El valor de la cuota $c$ viene dado por:

$$c = \frac{C_0i}{1-(1+i)^{-N}}$$

> - $C_0$ = Capital prestado
> - $i$ = Tipo de interes
> - $N$ = Cuotas


**Ejemplo** Un banco ofrece una hipoteca con un tipo de interés *Euribor* +0.39 y queremos
contratarla para financiar un capital de 200 000 € a devolver en 30 años (N = 360). Vamos a
determinar el importe de la cuota de la hipoteca tomando como valor del Euribor 1.231.
El interés nominal de la hipoteca es $j = 1.231 + 0.39 = 1.621$%, luego el interés efectivo
mensual es $i = 1.621$%$/12 = 0.1351$%. El importe de la cuota será:

$$c = \frac{200 000\cdot 0.001351}{1-1.001351^{-360}} = 701.91 €/mes$$


Ref: Carlos Ivorra https://www.uv.es/ivorra/