# Teoría de Lenguajes

Preguntas de final Julio 2024.

## Ejercicio 1

**Dar un algoritmo que decida si dos expresiones regulares denotan el mismo lenguaje. Justificar la correctitud. Analizar la complejidad computacional de peor caso.**

Sean $e$ y $f$ expresiones regulares. Construimos $M_e$ y $M_f$ AFDs a partir de cada expresión regular tal que $\mathcal{L}(M_e) = e$ y $\mathcal{L}(M_f) = f$.

**Opción 1**: comparar autómatas mínimos.

1. Calculamos $M_e'$ y $M_f'$ AFDs mínimos de $M_e$ y $M_f$ respectivamente.
2. Revisamos si $M_e' = M_f'$ salvo isomorfismo.

Complejidad $O(ns \text{ log } n)$ para minimizar los autómatas ($n$ cantidad de estados, $s$ símbolos del alfabeto).

**Opción 2**: por Lema de Pumping.

$M_e = \langle Q_e, \Sigma, \delta_e, q_0, F_e \rangle$ \
$M_f = \langle Q_f, \Sigma, \delta_f, p_0, F_f \rangle$

Tomamos $p = \text{max}(2|Q_e|-1, 2|Q_f|-1)$. Para toda cadena $w \in \Sigma^{\leq p}$ verificamos que se cumpla:

$\hat\delta_e(q_0, w) \in F_e \iff \hat\delta_f(p_0, w) \in F_f$

Por Lema de Pumping, si se cumple para todas las cadenas de longitud $\leq p$ entonces ambos autómatas reconocen el mismo lenguaje. Estas son todas las cadenas más chicas que pertenecen al languaje, y cualquier cadena de longitud mayor se obtiene pumpeando estas cadenas.

Cantidad de cadenas a revisar: $|\Sigma^{\leq p}| = \sum_{i=0}^p s^i = \frac{s^{p+1} - 1}{s - 1}$ son $s = |\Sigma|$.

**Opción 3**: por diferencia simétrica.

$\mathcal{L}(M_e) \Delta \mathcal{L}(M_f) = \emptyset$ \
$\iff \mathcal{L}(M_e) \cap \overline{\mathcal{L}(M_f)} = \emptyset \land \overline{\mathcal{L}(M_e)} \cap \mathcal{L}(M_f) = \emptyset$ \
$\iff \mathcal{L}(M_e) = \mathcal{L}(M_f)$

1. Construimos los AFDs $A_1$ y $A_2$ tales que $\mathcal{L}(A_1) = \mathcal{L}(M_e) \cap \overline{\mathcal{L}(M_f)}$ y $\mathcal{L}(A_2) = \overline{\mathcal{L}(M_e)} \cap \mathcal{L}(M_f)$.
2. Verificamos si $\mathcal{L}(A_1) = \emptyset$ y $\mathcal{L}(A_2) = \emptyset$, por ejemplo viendo que ningún estado final es alcanzable desde el estado inicial con DFS/BFS.

## Ejercicio 2

**Dar dos algoritmos distintos para determinar si el lenguaje aceptado por un autómata finito dado es el conjunto de todas las cadenas del alfabeto. Justificar cada uno y dar su complejidad algorítmica.**

Sea $M$ un autómata finito cualquiera. QVQ: $\mathcal{L}(M) = \Sigma^\ast$.

**Opción 1**

1. Determinizamos y minimizamos $M$ para obtener $M'$ AFD mínimo.
2. Revisamos si $M'$ contiene un único estado final, con transiciones a sí mismo para todos los símbolos del alfabeto.

**Opción 2**

Notemos que $\mathcal{L}(M) = \Sigma^\ast \iff \overline{\mathcal{L}(M)} = \emptyset$.

1. Construimos $M^c$ AFD tal que $\mathcal{L}(M^c) = \overline{\mathcal{L}(M)}$.
2. Revisamos si $\mathcal{L}(M^c) = \emptyset$.

## Ejercicio 3

**Dar un algoritmo que determine si un lenguaje regular dado es infinito. Justificar y dar la complejidad del algoritmo en el peor caso.**

Construimos $M = \langle Q, \Sigma, \delta, q_0, F \rangle$ AFD tal que reconoce el lenguaje regular dado. Por Lema de Pumping, $\mathcal{L}(M)$ es infinito si y solo si existe $w \in \Sigma^\ast$ tal que $\hat\delta(q_0, w) \in F$ y $n \leq |w| < 2n$ con $n = |Q|$.

Si existe tal cadena $w$ aceptada por $M$, entonces necesariamente se utiliza un ciclo de $M$ para aceptarla, pues $|w| \geq n$ y hay solo $n$ estados en $M$. Por lo tanto, por el Lema de Pumping podemos pumpear una cantidad arbitraria de veces la subcadena aceptada por el ciclo. Dicho de otra forma, podemos recorrer el ciclo una cantidad arbitraria de veces antes de continuar hacia el estado final, aceptando así cadenas arbitrariamente grandes. Luego $\mathcal{L}(M)$ resulta infinito.

El algoritmo consistente en probar una por una las cadenas $w \in \Sigma^\ast$ tal que $n \leq |w| < 2n$ hasta encontrar una que sea aceptada por $M$. En tal caso frenamos y respondemos que $\mathcal{L}(M)$ es infinito. Si probamos todas las cadenas y ninguna es aceptada, entonces respondemos que $\mathcal{L}(M)$ no es infinito.

Basta con encontrar una única cadena $w$ (pueden haber más). En el peor caso terminamos probando todas las cadenas: $\sum_{i=n}^{i=2n} |\Sigma|^i$.

## Ejercicio 4

**¿Cuántos autómatas finitos determinísticos con dos estados pueden construirse sobre el alfabeto {0, 1}?**

La cantidad de funciones de transición $\delta: Q \times \Sigma \rightarrow Q$ que podemos construir son:

- $|Q \times \Sigma| = |Q| \ast |\Sigma| = 2 \ast 2 = 4$
- $|Q| = 2$

Por cada uno de los $4$ elementos del dominio de $\delta$ hay $2$ posibles asignaciones. Luego hay $2^4 = 16$ funciones $\delta$ distintas. Al ser un AFD el formalismo requiere que el autómata sea completo (todos los estados deben tener transiciones para todos los símbolos del alfabeto).

Ahora contamos las posibles configuraciones de estados iniciales y finales:

- $2$ opciones para estado inicial.
- $2^{|Q|} = 2^2 = 4$ opciones para configuración de estados finales. Hay $2$ estados y cada uno puede o no ser final. Otra forma de pensarlo es: $F \in \mathcal{P}(Q)$ (el conjunto $F$ de estados finales pertenece a partes de $Q$), y $|\mathcal{P}(Q)| = 2^{|Q|} = 4$ (hay 4 posibles conjuntos $F$).

Entonces en total existen $16 \ast 2 \ast 4 = 128$ autómatas distintos. Muchos de estos autómatas son isomorfos y reconocen el mismo lenguaje, pero el enunciado solo pide contar autómatas (sin mencionar el lenguaje generado).

En general esta cuenta se obtiene así: $|Q|^{|Q|\ast|\Sigma|} \ast |Q| \ast 2^{|Q|} = |Q|^{|Q|\ast|\Sigma|+1} \ast 2^{|Q|}$.

**¿Cuántos autómatas finitos no determinísticos con dos estados pueden construirse sobre el alfabeto {0, 1}?**

La cuenta es parecida a la pregunta anterior. Lo que cambia es que en un AFND la función de transición tiene como codominio a $\mathcal{P}(Q)$, y entonces la cantidad de funciones de transición $\delta: Q \times \Sigma \rightarrow \mathcal{P}(Q)$ que podemos construir son: $|\mathcal{P}(Q)| ^ {|Q| \ast |\Sigma|}$.

La forma de contar las configuraciones de estados iniciales y finales es la misma. La fórmula general resulta: $|\mathcal{P}(Q)| ^ {|Q| \ast |\Sigma|} \ast |Q| \ast 2^{|Q|}$.

Para el caso puntual del enunciado:

- $|Q| = 2$
- $|\Sigma| = 2$
- $(2^2) ^ {2 \ast 2} \ast 2 \ast 2^{2} = 2048$

**¿Cuántos autómatas de pila con dos estados pueden construirse con alfabeto de entrada $\Sigma$, alfabeto de pila $\Gamma$, y una cantidad máxima de $M$ símbolos en cada transición?**

Contamos la cantidad de funciones de transición $\delta: Q \times (\Sigma \cup \{ \lambda \}) \times \Gamma \rightarrow \mathcal{P}(Q \times \Gamma^{\leq M})$. Notar el codominio de la función donde restringimos la cadena a escribir en la pila a $\Gamma^{\leq M}$ pues por enunciado se escriben como máximo $M$ símbolos.

- $|Q \times (\Sigma \cup \{ \lambda \}) \times \Gamma| = |Q| \ast (|\Sigma|+1) \ast |\Gamma|$
- $|\mathcal{P}(Q \times \Gamma^{\leq M})| = 2 ^ {|Q| \ast |\Gamma^{\leq M}|} = 2 ^ {|Q| \ast Z}$ con $Z = |\Gamma^{\leq M}| = \Sigma_{i=0}^{i=M} |\Gamma|^i$

La forma de contar las configuraciones de estados iniciales y finales es la misma que en las preguntas anteriores.

Asumiendo que el símbolo de inicio de la pila está fijo la fórmula es: $(2 ^ {|Q| \ast Z}) ^ {|Q| \ast (|\Sigma|+1) \ast |\Gamma|} \ast |Q| \ast 2^{|Q|}$.

Si queremos incluir la cantidad de símbolos distintos que podríamos usar para el inicio de la pila entonces: $(2 ^ {|Q| \ast Z}) ^ {|Q| \ast (|\Sigma|+1) \ast |\Gamma|} \ast |Q| \ast 2^{|Q|} \ast |\Gamma|$.
